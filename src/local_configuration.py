import json

# Do I look like I know python? :)
local_configuration = {}

x = input("Bitte gebe den Namen der Config mit den Accounts und der Target CU an: ")

with open(f'/home/placebot/{x}.json', 'r') as f:
    local_configuration = json.load(f)