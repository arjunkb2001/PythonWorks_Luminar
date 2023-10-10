f=open("C:\\Users\\91974\\Desktop\\pythonwork\\012fileinput-output\\number.txt")
numbers=[line.rstrip("\n")for line in f]
# for n in numbers:
#     if n.startswith("kl"):

#         print(n)



keralanum=[n for n in numbers if n.startswith("kl")]
print(keralanum)