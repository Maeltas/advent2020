def fFunc(x1,x2,y1,y2):
    x2=x1+x2
    x2/=2
    return x2
def bFunc(x1,x2,y1,y2):
    x1=x1+x2
    x1/=2
    x1+=1
    return x1
def lFunc(x1,x2,y1,y2):
    y2=y1+y2
    y2/=2
    return y2
def rFunc(x1,x2,y1,y2):
    y1=y1+y2
    y1/=2
    y1+=1
    return y1
f=open("input5", "r")
result=0
seats=[]
for string in f:
    x1=0
    x2=127
    y1=0
    y2=7
    for x in string:
        print(x)
        if x=="B":
            x1=int(bFunc(x1,x2,y1,y2))
        elif x=="F":
            x2=int(fFunc(x1,x2,y1,y2))
        elif x=="L":
            y2=int(lFunc(x1,x2,y1,y2))
        elif x=="R":
            y1=int(rFunc(x1,x2,y1,y2))
    id=x1*8+y1
    seats.append(id)
seats.sort()
result=[]
bigger=False
smaller=False
i=0
for seat in seats:
    if seats[i+1]!=seat+1:
        result=seat+1
        break
    i+=1
print(result)