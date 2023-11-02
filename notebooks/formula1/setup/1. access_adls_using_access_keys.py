# Databricks notebook source
# MAGIC %md
# MAGIC #### Access Azure Datalake using Access Keys
# MAGIC
# MAGIC - set spark config fs.azure.account.key
# MAGIC - list all files from demo container
# MAGIC - read data from circuits.csv file

# COMMAND ----------

spark.conf.set("fs.azure.account.key.formula1dlakhil1.dfs.core.windows.net", 
               "k+1iHeRy2OUqFq26WjgZydTuT0UcPP4BRI4I6ta3bl4WrKGpvzloRn0KzJ4rCkyBkvOsUgduemBy+AStH9v9Dw==")

# COMMAND ----------

display(dbutils.fs.ls("abfss://formula1@formula1dlakhil1.dfs.core.windows.net"))

# COMMAND ----------

display(dbutils.fs.ls("abfss://nfl@formula1dlakhil1.dfs.core.windows.net/raw"))

# COMMAND ----------

display(spark.read.option('header', 'True').csv("abfss://nfl@formula1dlakhil1.dfs.core.windows.net/raw/tracking/tracking_week_1_1.csv"))

# COMMAND ----------

