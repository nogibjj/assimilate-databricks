import dask.dataframe as dd
from dask.distributed import Client

def dask_client():
    """Create a dask client"""

    client = Client()
    return client


def query_s3_tutorial():
    """Query the s3 tutorial dataset
    https://tutorial.dask.org/00_overview.html
    """

    ddf = dd.read_parquet(
    "s3://dask-data/nyc-taxi/nyc-2015.parquet/part.*.parquet",
    columns=["passenger_count", "tip_amount"],
    storage_options={"anon": True},
    )

    return ddf


