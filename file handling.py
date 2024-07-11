


f=open('myfile.txt','r')#opening a file
print(f)
# reading a file
text=f.read()
print(text)
f.close()
# writing a file
f=open('myfile.txt','a')
f.write("hello ashok ")
f.close()
print(f)
