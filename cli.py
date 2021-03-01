#!/usr/bin/python3
import click

@click.command()
@click.option("--url", default="http://localhost:8080/cqf-ruler-r4/fhir", help="Number of greetings.")
@click.option("--id", prompt="id of the resource", help="The id to be allocated to the resources (Measure and Library).")
@click.option("--dir", default=1, help="Directory containing ")
def package_and_deploy(url, id, dir):
    """ICCQL is a CQL packaging and deployment tool"""

if __name__ == '__main__':
    package_and_deploy()