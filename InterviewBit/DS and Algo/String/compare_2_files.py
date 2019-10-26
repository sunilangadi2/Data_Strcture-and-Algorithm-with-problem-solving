import difflib
f1=open('a.txt','r')  #open a file
f2=open('b.txt','r') #open another file to compare
str1=f1.read()
str2=f2.read()
str1=str1.split()  #split the words in file by default through the spce
str2=str2.split()
d=difflib.Differ()     # compare and just print
diff=list(d.compare(str2,str1))
print('\n'.join(diff))