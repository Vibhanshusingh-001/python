f = open('myfile2.txt', 'w')
lines = ['line 1\n', 'line 2\n', 'line 3\n']
f.writelines(lines)
f.close()
# lines jo iterable object hai iske saare elements ko 1 by one
# 1-1 karke us file me chipka dega

#Keep in mind that the writelines() method does not add newline characters between the strings in the sequence.
# If you want to add newlines between the strings, you can use a loop to write each string separately