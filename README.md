# assimilate-databricks
A repo to assimilate databricks


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