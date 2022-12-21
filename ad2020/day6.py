def count(group):
    letters=[]
    letters1=[]
    result=0
    i=0
    for x in group:
        for y in x:
            if y not in letters and y != "\n" and i==0:
                letters.append(y)
            if i>0 and y not in letters1 and y != "\n":
                letters1.append(y)
        if i>0:
            res_letters=[]
            for lt in letters1:
                if lt in letters:
                    res_letters.append(lt)
            letters=res_letters
        i+=1
        letters1=[]
    print(letters)
    result=len(letters)
    return result

f=open("input6", "r")
group=[]
result=0
for x in f:
    if x!="\n":
        group.append(x)
    else:
        result+=count(group)
        group=[]
result+=count(group)
print(result)