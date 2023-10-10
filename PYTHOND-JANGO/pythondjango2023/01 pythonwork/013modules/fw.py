from json import load

path="C:\\Users\\91974\\Desktop\\pythonwork\\013modules\\readfromjson\\data.json"
# open (path,mode,encodinhg)

with open(path)as f:
    records=load(f)
# print(records)    

# for f in encoding :
# print (f.get("name"))

fw_names=[f.get("name")for f in records]

print(fw_names)

# top rated framework

top_fw=max(records,key=lambda d :d.get("rating"))
print(top_fw)

# frontend framework names

# python framework names

