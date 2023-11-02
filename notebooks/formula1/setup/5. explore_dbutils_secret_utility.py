# Databricks notebook source
# MAGIC %md
# MAGIC ###### Explore_dbutils_secret_utility
# MAGIC

# COMMAND ----------

dbutils.secrets.help()

# COMMAND ----------

dbutils.secrets.listScopes()

# COMMAND ----------

dbutils.secrets.get(scope = "formula1-scope", key = 'formula1dl-account-key')