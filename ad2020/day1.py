f=open("input1", "r")
table=[]
for x in f:
    table.append(int(x))
print(table)
for x in table:
    for y in table:
        for z in table:
            if x+y+z==2020:
                print(x*y*z)
