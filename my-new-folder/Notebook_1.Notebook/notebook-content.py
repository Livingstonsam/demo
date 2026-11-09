# Fabric notebook source

# METADATA ********************

# META {
# META   "kernel_info": {
# META     "name": "synapse_pyspark"
# META   },
# META   "dependencies": {
# META     "lakehouse": {
# META       "default_lakehouse": "449407cc-bdbd-48dc-914b-0ed8ae960a6c",
# META       "default_lakehouse_name": "test",
# META       "default_lakehouse_workspace_id": "60a0c169-41d6-4661-a4e8-e3de06bb0ca1",
# META       "known_lakehouses": [
# META         {
# META           "id": "449407cc-bdbd-48dc-914b-0ed8ae960a6c"
# META         }
# META       ]
# META     },
# META     "warehouse": {
# META       "known_warehouses": []
# META     }
# META   }
# META }

# CELL ********************

df = spark.read.format("csv").option("header","true").load("Files/Sales.csv")
# df now is a Spark DataFrame containing CSV data from "Files/Sales.csv".
display(df)

# METADATA ********************

# META {
# META   "language": "python",
# META   "language_group": "synapse_pyspark"
# META }
