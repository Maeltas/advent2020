f=open("input2", "r")
result=0
for x in f:
    x=x.split()
    numb=x[0].split("-")
    numb1=numb[0]
    numb2=numb[1]
    letter=x[1].replace(":","")
    hm=0
    word=x[2]
    if word[int(numb1)-1]==letter or word[int(numb2)-1]==letter:
        result+=1
        if word[int(numb1)-1]==letter and word[int(numb2)-1]==letter:
            result-=1
print(result)