import json
from pprint import pprint

json_data_file = open('experiment_archival.json')
json_object = json.load(json_data_file)
pprint(json_object)

project_name = json_object["project_name"]
print(project_name)
experiment_archival = json_object["experiment_archival"]
print(experiment_archival)
for i in range(0, len(experiment_archival)):
    print(experiment_archival[i]["pipeline_name"])
    print(experiment_archival[i]["pipeline_runs"])