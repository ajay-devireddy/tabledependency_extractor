Table Relationship Extractor:

This is a Python script that reads one or more JSON files containing SQL queries and extracts the table relationships based on the FROM clause of each query. The output is a list of table dependencies for each table referenced in the query.

Prerequisites:

•	Python 3.x 
•	A list of JSON files containing SQL queries

Usage:

1.	Clone or download this repository.
2.	Install Python if you haven't already done so.
3.	Install the json module if it's not already installed (it should be included with Python).
4.	Open your terminal and navigate to the directory containing the repository.
5.	Run the script using the command python table_relationship_extractor.py.
6.	Enter the path to the directory containing the JSON files when prompted.
7.	The script will print out the table dependencies for each table referenced in the query.


Solution Approach:

The script takes a folder path containing a list of JSON files as input. It then searches through each file to find SQL queries that reference tables, and identifies the dependencies between those tables. The approach can be broken down into the following steps:
1.	Collect all JSON files in the specified folder: The script uses the glob module to search for all files with a .json extension in the specified folder.
2.	Iterate through each JSON file: For each JSON file, the script loads the data as a Python dictionary using the json module.
3.	Identify SQL queries: The script searches for SQL queries in the loaded data by checking for the presence of a query key in the dictionary and a L key within the query key. This is because L contains a list of all the queries in the file.
4.	Identify tables in SQL queries: For each SQL query found, the script identifies the tables being referenced by checking for the presence of a select key within a M key of a query in L. The first table listed after the SELECT keyword is used as the table name.
5.	Identify table dependencies: Once the table name is identified, the script looks for the table in the FROM clause of the query to identify its dependencies. The dependencies are any tables that are listed in the JOIN clauses of the FROM clause.
6.	Recursively identify dependent tables: If a table has dependencies, the script calls the get_dependent_tables function recursively to find the dependencies of those dependent tables.
7.	Print table dependencies: Once all table dependencies have been identified, the script prints the dependencies as a tree structure, with each table's immediate dependencies listed below it.

This approach is recursive, allowing it to handle complex table dependencies that span multiple levels. The get_dependent_tables function recursively calls itself to identify all dependent tables for a given table, even if those dependencies have dependencies of their own. The final output is a clear and concise tree structure that shows the dependencies for each table.


Output:

The script outputs a tree structure of the table dependencies for each table in the JSON files. For each table, it shows its immediate dependencies as well as any dependencies of its dependencies. Here's an example output:

Table dependencies: 
table1: 
  |-dependent_table1 
  |+dependent_table2 
table2: 
  |-dependent_table3 
table3: 

In this example, table1 depends on dependent_table1 and dependent_table2, table2 depends on dependent_table3, and table3 has no dependencies.


License
This code is licensed under the MIT License. See the LICENSE file for more information.


