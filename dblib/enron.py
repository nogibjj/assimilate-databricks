"""
Some ideas are taken from the following sources:
    https://www.kaggle.com/code/zichen/explore-enron/notebook

See this thread about unique problems with dask and data formatting:
    https://github.com/dask/dask/issues/4145

"""

import pandas as pd
import dask.dataframe as dd


def pandas_load_enron(location="datasets/emails.csv"):
    """Load the enron dataset into a pandas dataframe

    Assumes the dataset is in the datasets folder in the root of the project
    """
    return pd.read_csv(location)


def pandas_print_enron(location="datasets/emails.csv", record_number=0):
    """Display the enron dataset

    print and returns a single email record from the enron dataset
    """

    df = pd.read_csv(location)
    record = df["message"][record_number]
    print(record)
    return record


def dask_query_enron(location="datasets/emails.csv"):
    """Query the enron dataset

    Assumes the dataset is in the datasets folder in the root of the project
    """

    ddf = dd.read_csv(location, blocksize=None)
    return ddf
