import sixx
import json

inline_JSON = '{"id":1, "name": ["abc", "xyz"]}'

jsonData = json.loads(inline_JSON)
jsonData.get("name")
json.dumps(jsonData)
print(json.dumps(jsonData, indent='\t'))

path_JSON = './jsondata/jsn2.json' # String
### Read File <way1>
jsonFile = open(path_JSON,'r') #'r'ead,'w'rite,'a'ppend
jsonData = json.load(jsonFile)
jsonFile.close()

### Read File <way2>
# with문을 나올 때 close를 자동으로 불러줍니다.
with open(path_JSON) as jsonFile:
    jsonData = json.load(jsonFile)


