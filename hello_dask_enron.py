from dblib.enron import dask_query_enron

ddf = dask_query_enron()
print("One record from the enron dataset without compute:")
print(ddf["message"][0])
print("One record from the enron dataset with compute:")
print(ddf["message"][0].compute())