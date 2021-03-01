#!/usr/bin/python3


from .iccql import *


parser = argparse.ArgumentParser(description="""
        ICCQL for CLI

        """)



parser = argparse.ArgumentParser(description='Add some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='interger list')parser.add_argument('--sum', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')