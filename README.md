# output-Visualisation-of-SQL-query
This repository is a small python snippet that demonstrates how you can visualize an output of your SQL query on your browser. 

# Pre-requisite:
1. MySql: [Download](https://www.liquidweb.com/kb/install-mysql-windows)
2. Pandas : `pip install pandas`
3. plotly : `pip install plotly`

# How to use? 
1. Once your MySql workbench is ready to be used upload the dump file into a new or existing database. It is important to choose a database before importing the sql file. 
2. Figureout your SQL query you want to plot. 
3. In `extract.py` change your root password so that it can connect to you database. 
4. Insert the query you need.
5. Insert the column names that you want to plot here: `fig = px.bar(df, x="CustomerName", y="Total")`


# Output Looks something like this
![Opera Snapshot_2021-06-29_152603_127 0 0 1](https://user-images.githubusercontent.com/51456430/123778082-626c1a80-d8ee-11eb-8fdc-825c5568ffcb.png)
