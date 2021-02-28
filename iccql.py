#!/usr/bin/python3
from os import listdir, getcwd, chdir
from sys import argv
import requests
import json
import base64

def encode_cql(cql_file):

    with open(_temp + "/" + cql_file, 'r') as f:
        return base64.b64encode((f.read()).encode('ascii'))

current_dir = getcwd()

fhir_endpoint = argv[2]
path = argv[1]

chdir("{}".format(path))

_temp = getcwd()
_name = _temp.split('/')[-1:][0]

measure_resource_file = "{}-Measure.json".format(_name)
library_resource_file = "{}-Library.json".format(_name)
cql_source = "{}.cql".format(_name)


# read input files
with open(_temp + "/" + measure_resource_file, 'r') as f:
    measure_resource = json.loads(f.read())

with open(_temp+ "/" + library_resource_file, 'r') as f:
    library_resource = json.loads(f.read())


library_resource['content'][0]['data'] = encode_cql(cql_source).decode('utf-8')

with open(_temp+ "/" + library_resource_file, 'w') as f:
    f.write(json.dumps(library_resource))

# print(type(library_resource))

r = requests.put("{}/Library/{}".format(fhir_endpoint, _name), json=library_resource)
print("^^ - uploaded library resource: S: ", r.status_code)
# upload resources
r = requests.put("{}/Measure/{}".format(fhir_endpoint, _name), json=measure_resource)
print("^^ - uploaded measure resource: S: ", r.status_code)



# run measure 
# r = requests.get("{}/cqf-ruler-r4/fhir/Measure/{}/$evaluate-measure?periodStart=2020-01-01&periodEnd=2020-12-31".format(fhir_endpoint, _name))

r = requests.get("{}/Measure/{}/$evaluate-measure?periodStart=2020-01-01&periodEnd=2020-12-31".format(fhir_endpoint, _name))

print('\n\n\n')
print(":: -- :: \n:: evaluate measure results")
print(r.text)