#!/usr/bin/env python

import click
from dblib.querydb import querydb

#build a click group
@click.group()
def cli():
    """A simple CLI to query a SQL database"""

#build a click command
@cli.command()
@click.option("--query", default="SELECT * FROM default.diamonds LIMIT 2", help="SQL query to execute")
def cli_query(query):
    """Execute a SQL query"""
    querydb(query)
  
  #run the CLI
if __name__ == "__main__":
    cli()