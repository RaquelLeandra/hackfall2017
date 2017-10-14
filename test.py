import json

with open('data.txt') as data_file:
    data = json.load(data_file)

print(data['recognitionResult']['lines'][0].keys())

for line in range(0,len(data['recognitionResult']['lines'])):
    print(data['recognitionResult']['lines'][line]['text'] + '\n')