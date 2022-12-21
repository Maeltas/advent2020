def fnc(intr,rpinstr,i):
    acc=0
    while i not in rpinstr or i > len(intr):
        print(intr[i])
        rpinstr.append(i)
        if "acc" in intr[i]:
            numb = " ".join(intr[i].split()[1:])
            if "+" in numb:
                numb = numb.replace("+", "")
                numb = int(numb)
                acc += numb
            else:
                numb = numb.replace("-", "")
                numb = int(numb)
                acc -= numb
            i += 1
        elif "jmp" in intr[i]:
            numb = " ".join(intr[i].split()[1:])
            if "+" in numb:
                numb = numb.replace("+", "")
                numb = int(numb)
                i += numb
            else:
                numb = numb.replace("-", "")
                numb = int(numb)
                i -= numb

        else:
            i += 1
f=open("input8", "r")
acc=0
intr=[]
rpinstr=[]
for x in f:
    intr.append(x)
i=0
acc+=fnc(intr,rpinstr,i)
print(acc)
