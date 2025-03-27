file1=open('codingal.txt','r')
file2=open('file.txt','w')
content=file1.readlines()
for i in range(1,len(content)):
    if i%2!=0:
       file2.write(content[i])
file1.close()
file2.close()