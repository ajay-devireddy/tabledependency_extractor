import glob
import json


def get_dependent_tables(table_name, json_files, dependencies=None):
    """
    Recursively get all dependent tables for a given table name
    in a list of JSON files
    """
    if dependencies is None:
        dependencies = set()

    for file in json_files:
        with open(file) as f:
            data = json.load(f)
        if "query" not in data or "L" not in data["query"]:
            continue
        for table in data["query"]["L"]:
            if "M" not in table or "select" not in table["M"]:
                continue
            if table_name in table["M"]["select"]["S"]:
                from_clause = table["M"]["from"]["S"]
                dependent_tables = [join_clause.strip().split()[0] for join_clause in from_clause.split("JOIN")[1:]]
                for dependent_table in dependent_tables:
                    if dependent_table not in dependencies:
                        dependencies.add(dependent_table)
                        get_dependent_tables(dependent_table, json_files, dependencies)

    return dependencies


if __name__ == "__main__":
    folder_path = input("Enter the folder path where JSON files are stored: ")
    json_files = glob.glob(folder_path + '/*.json')
    if len(json_files) == 0:
        print("No JSON files found in the specified folder.")
    else:
        all_dependencies = {}
        for file in json_files:
            with open(file) as f:
                data = json.load(f)
            if "query" not in data or "L" not in data["query"]:
                continue
            for table in data["query"]["L"]:
                if "M" not in table or "select" not in table["M"]:
                    continue
                table_name = table["M"]["select"]["S"].split(",")[0].strip()
                dependencies = get_dependent_tables(table_name, json_files)
                if dependencies:
                    all_dependencies[table_name] = list(dependencies)
        if not all_dependencies:
            print("No dependencies found.")
        else:
            print("Table dependencies:")
            for table, dependencies in all_dependencies.items():
                print(table + ':')
                for i, dep_table in enumerate(dependencies):
                    if i == len(dependencies) - 1:
                        print('  ' + '|-' + dep_table)
                    else:
                        print('  ' + '|+' + dep_table)
