#line by line read karne ke liye ham ise use karte h
f=open('file.txt','r')
i=0
while True:
    i=i+1
    line=f.readline()
    if not line:
        print(line,type(line))
        break
    m1=line.split(",")[0]
    m2=line.split(",")[1]
    m3=line.split(",")[2]
    print(f"Marks of student {i}in maths is:{m1}")
    print(f"Marks of student {i}in english is:{m2}")
    print(f"Marks of student {i}in SST is:{m3}")

    print(line)


