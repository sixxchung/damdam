import json # import json module

# with statement
PATH = './20210818080000-10.json'
with open('json file path or name') as json_file:
    json_data = json.load(json_file)


import json
js1 = '{ 
  "id": 1, 
  "name": "helloalpaca"
}'
jsn1 = '{
  "id": 1,
  "name": "helloalpaca"
}'

# String으로 만들어 준다.
jsn2 = '{
  "id": 1,
  "name": ["helloalpaca", "choppermask"]
}'

aa=json.loads('./jsn1.json')

jsonFile = open('./jsn1.json', 'r')  # 'r'ead, 'w'rite, 'a'ppend
json_data = json.load(jsonFile)
jsonFile.close()

# with문을 나올 때 close를 자동으로 불러줍니다.
with open('./jsn2.json') as jsonFile:
    json_data = json.load(jsonFile)

json.dumps(json_data) 
print(json.dumps(json_data, indent='\t'))
