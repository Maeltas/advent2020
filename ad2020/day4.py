import re
def isValid(passport):
    byr=False
    iyr=False
    eyr=False
    hgt=False
    hcl=False
    ecl=False
    pid=False
    for x in passport:
        x=x.split()
        for y in x:
            if "byr:" in y:
                val=int(y.split(":")[1])
                if val <=2002 and val >=1920:
                    byr=True
            if "iyr:" in y:
                val = int(y.split(":")[1])
                if val <= 2020 and val >= 2010:
                    iyr = True
            if "eyr:" in y:
                val = int(y.split(":")[1])
                if val <= 2030 and val >= 2020:
                    eyr=True
            if "hgt:" in y:
                val = y.split(":")[1]
                if "cm" in val:
                    val=val.replace("cm","")
                    val=int(val)
                    if val>=150 and val<=193:
                        hgt=True
                elif "in" in val:
                    val=val.replace("in", "")
                    val = int(val)
                    if val <= 76 and val >= 59:
                        hgt = True
            if "hcl:" in y:
                val = y.split(":")[1]
                if re.match("#[0-9a-f]{6}", val):
                    hcl=True
            if "ecl:" in y:
                val = y.split(":")[1]
                if val=="amb" or val=="blu" or val=="brn" or val=="gry" or val=="grn" or val=="hzl" or val=="oth":
                    ecl=True
            if "pid:" in y:
                val = y.split(":")[1]
                if re.match("[0-9]{9}$",val):
                    pid=True
    if byr==True and iyr==True and eyr==True and hgt==True and hcl==True and ecl==True and pid==True:
        return 1
    return 0

f=open("input4", "r")
passport=[]
result=0
for x in f:
    print("Teraz: "+x)
    if x!="\n":
        passport.append(x)
    else:
        result+=isValid(passport)
        passport=[]
result+=isValid(passport)
print(result)


