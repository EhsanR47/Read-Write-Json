import json
  
# Data to be written
dictionary ={
    "Name" : "Ehsan",
    "Age" : 25,
    "Gender" : "male",
    "phonenumber" : "9976770500",
    "Email" : "ehsan1231ehsan@gmail.com"
}
  
# Serializing json 
json_object = json.dumps(dictionary, indent = 10)
  
# Writing to sample.json
with open("sample.json", "w") as outfile:
    outfile.write(json_object)

# Opening JSON file
with open('sample.json', 'r') as openfile:
    # Reading from json file
    json_object = json.load(openfile)
  
print(json_object)
print(type(json_object))