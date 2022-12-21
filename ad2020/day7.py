def count(dict,key,number):
    result=0
    for val in dict[key]:
        if val!="no other bags":
            result2=number*int(" ".join(val.split()[0:1]))
            val=" ".join(val.split()[1:])
            result+=result2
            result+=count(dict,val,result2)
    return result
def contains(dict,key):
    result=0
    value=dict[key]
    for val in value:
        if val!="no other bags":
            number=int(" ".join(val.split()[0:1]))
            val = " ".join(val.split()[1:])
            result+=count(dict,val,number)
            result+=number
    return result

f=open("input7", "r")
dict={}
result=0
for x in f:
    key= " ".join(x.split()[0:2])
    values=" ".join(x.split()[4:])
    values=values.split(",")
    dict[key]=[]
    for value in values:
        val=" ".join(value.split()[0:3])
        val=val.replace(".","")
        dict[key].append(val)
result+=contains(dict,"shiny gold")
print(result)


