Table Relationship Extractor:

This is a Python script that reads one or more JSON files containing SQL queries and extracts the table relationships based on the FROM clause of each query. The output is a list of table dependencies for each table referenced in the query.

Solution Approach:

The script first loads the JSON file(s) and extracts the FROM clause of the SQL query. The FROM clause is then split into separate table joins based on the FULL OUTER JOIN keyword. The script then loops through each table join and extracts the dependent tables from the ON clause. The base table and schema for each dependent table is then extracted and added to a dictionary of dependencies. Finally, the script prints out the table dependencies in a tree-like format.

How to Use:

1.	Clone the repository to your local machine.
2.	Install Python if you haven't already done so.
3.	Install the json module if it's not already installed (it should be included with Python).
4.	Put your JSON files containing SQL queries in the same directory as the script.
5.	Open a terminal or command prompt and navigate to the directory containing the script and JSON files.
6.	Run the script using the command python table_relationship_extractor.py.
7.	The script will print out the table dependencies for each table referenced in the query.


Note: You may need to modify the code to suit the specific structure of your JSON files.


