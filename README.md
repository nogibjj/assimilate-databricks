# assimilate-databricks
A repo to assimilate databricks

## API Getting Started

![databricks-api](https://user-images.githubusercontent.com/58792/189719737-fcdaf61f-93d2-415b-8eea-ebb96143187d.png)



## Setup auth

[databricks-python](https://docs.microsoft.com/en-us/azure/databricks/dev-tools/python-api)

Place in Codespace secrets
* [unix, linux, mac](https://docs.microsoft.com/en-us/azure/databricks/dev-tools/python-api#unixlinuxandmacos)

```bash
DATABRICKS_HOST
DATABRICKS_TOKEN
```


## Test out CLI

```
databricks clusters list --output JSON | jq
databricks fs ls dbfs:/
databricks jobs list --output JSON | jq
```
## Remote connect

[databricks-connect](https://docs.databricks.com/dev-tools/databricks-connect.html)

## Databricks SQL Connector

[Setup table first!](https://docs.databricks.com/dbfs/databricks-datasets.html)

[sql remote](https://docs.databricks.com/dev-tools/python-sql-connector.html)
https://docs.databricks.com/integrations/bi/jdbc-odbc-bi.html#connection-details-cluster


## Comparing to Dask

An alternative solution to Databricks is https://tutorial.dask.org/00_overview.html[Dask] or [Ray](https://docs.ray.io/en/latest/data/dask-on-ray.html).

