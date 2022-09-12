import os

from databricks_cli.sdk.api_client import ApiClient
from databricks_cli.clusters.api import ClusterApi

api_client = ApiClient(
    host=os.getenv("DATABRICKS_HOST"), token=os.getenv("DATABRICKS_TOKEN")
)

clusters_api = ClusterApi(api_client)
clusters_list = clusters_api.list_clusters()

print("Cluster name, cluster ID")

for cluster in clusters_list["clusters"]:
    print(f"{cluster['cluster_name']}, {cluster['cluster_id']}")
