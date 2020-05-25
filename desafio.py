import json

# open json file and load
with open('example.json', 'r') as myfile:
    data = myfile.read()

# parse json to a object
my_obj = json.loads(data)

# create dicts to manage data
managers = {}
watchers = {}

# iterate object to manage data
for obj in my_obj:

    # for each manager name in object
    for managerName in obj['managers']:

        # verifies if key managerName already exists and add the tuple to the dict
        if managerName not in managers.keys():
            managers[managerName] = []
        managers[managerName].append((obj['priority'], obj['name']))

    # for each watcher name in object
    for watcherName in obj['watchers']:

        # verifies if key watcherName already exists and add the tuple to the dict
        if watcherName not in watchers.keys():
            watchers[watcherName] = []
        watchers[watcherName].append((obj['priority'], obj['name']))

# order by priority and create a new dict without priority label
for key in managers.keys():
    managers[key].sort(key=lambda x: x[0])
    managers[key] = [k[1] for k in managers[key]]

# order by priority and create a new dict without priority label
for key in watchers.keys():
    watchers[key].sort(key=lambda x: x[0])
    watchers[key] = [k[1] for k in watchers[key]]

# create managers.json file
with open('managers.json', 'w') as json_file:
    json.dump(managers, json_file)

# create watchers.json file
with open('watchers.json', 'w') as json_file:
    json.dump(watchers, json_file)
