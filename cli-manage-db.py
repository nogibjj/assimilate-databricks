#!/usr/bin/env python

from dblib.manage_databricks import list_clusters
import click


#build click group
@click.group()
def cli():
    """Manage Databricks"""

#build click command
@cli.command("list-clusters")
def list_clusters_command():
    """List Databricks clusters
    
    Example:
    ./cli-manage-db.py list-clusters
    """
    list_clusters()

#run click group
if __name__ == "__main__":
    cli()