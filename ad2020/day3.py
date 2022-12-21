f=open("input3", "r")
table=[]
trees=0
for x in f:
    table.append(x)
i=0
for x in table:
    table[i]=table[i].replace("\n","")
    i+=1
i=0
for x in table:
    for y in range (len(table)):
        table[i]+=x
    i+=1
x_change=1
y_change=2
x=0
y=0
result=0
print(table)
while y< len(table):
    if table[y][x]=="#":
        result+=1
    y+=y_change
    x+=x_change
print(result)