import json
import sys

json_path = sys.argv[1]

with open(json_path) as f:
    data = json.load(f)

message = data ["firstName"]

print (message)