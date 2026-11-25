
'''print(10)
a="Good Morning"
a='hello'
print(a[3:1-1:-1])
print(a[-2:-5:-1])
print(a[::-1])

a='Good Morning'
print(a[1:5])
print(a[1:5:2])
print(a[5:10:3])
print(a[-7:-4:3])

print(a[-7::3])
print(len(a))

a=input("enter:")
print(type(a))

a=input("enter:")
print(type(a))
print(type(a))

a=eval(input("enter:"))
print(a,type(a))'''

'''a=int(input("enter:"))
if a%2==0:
    print("even")
else:
    print("odd")'''

'''l=eval(input("enter list:"))

if len(l)==5:
    print("yes")
else:
    print("no")'''

'''print(chr(52))
print(ord('5'))
print(ord('A'))
print(ord('a'))

ch=input("enter:")
if ord(ch)>=65 and ord(ch)<=90:
    print("uppercase")
elif ord(ch)>=97 and ord(ch)<=122:
    print("Lowwercase")
elif ord(ch)>=48 and ord(ch)<=57:
    print("digit")'''


'''ch=input("enter:")
if "A"<=ch<="Z":
    print("uppercase")
elif "a"<=ch<="z":
    print("lowercase")
else:
    print("not an alphabet")'''

'''un=input("enter username:")
if un=='jeevitha':
    print('correct username:')
    pw=input("enter password:")
    if pw=='jeevitha123':
        print("Login successful")
    else:
        print("incorrect password")
else:
    print("incorrect username")'''

'''i=1
while i<=5:
    print(i)
    i+=1'''
'''i=1
while i<=8:
    print(i)
    i+=1'''
'''i=1
while i<=50:
    even=i%2==0
    if even:
        print("eve")
    else:
        print("")'''

'''n=int(input("enter:"))
rev=0
while n>0:
    r=n%10
    rev=rev*10+r
    n=n//10
    print(rev)'''

'''n=int(input("enter number:"))
rev=0
while n>0:
    ld=n%10
    n=n//1052
    rev=rev*10+ld
print(rev)'''

'''for i in range(1,101):
    print(i)'''

'''l=[10,20,30]
for i in l:
    print(i)'''

'''a="jeevitha"
for i in a:
    print(i)'''

'''s=input('enter:')
output=''
for i in s:
    if "A"<=i<="Z":
        output+=chr(ord(i)+32)
    elif 'a'<=i<='z':
        output+=chr(ord(i)-32)
    else:
        output+=i
        print(output)'''

'''s=input("enter:")
output=''
for i in s:
    rev=i+output
    output=rev
    print(output)'''

'''for i in range(1,6):
    for j in range(1,6):
        print('*',end='')
        print()'''

'''for i in range(1,6):
    for j in range(1,6):
        if i==j:
            print('1',end=' ')
        else:
            print('@',end=' ')
        print()'''

'''a=10,20,30
print(a,type(a))'''

'''a='happy birthday'
print(a[0:8+1:8])
print(a[-4:-7:-1])'''

'''def convert(s,out):
    for i in s:
        if 'a'<=i<='z':
            out+=chr(ord(i)-32)
        else:
            out+=i
        return out
    print(convert(input('enter a string:'),''))'''

#wih arg without retrun value

'''def convert(s,out):
    for i in s:
        if 'a'<=i<='z':
            out+=chr(ord(i)-32)
        else:
            out+=i
        print(out)
    convert(input('enter a string:'),'')'''
'''print("hello")
print(25)'''

'''def convert(s,out):
    for i in s:
        if 'a'<=i<='z':
            out+=chr(ord(i)-32)
        else:
            out+=i
        print(out)
        return 10
    print(convert(input('enter a string:'),''))'''

'''def convert():
a=input('enter a string:')
out=''
for i in a:
    if 'a'<=i<='z':
        out+=chr(ord(i)-32)
    else:
        out+=i
return out
    
print(convert())'''

'''class college:
    cname="GCEM"
    cloc="hoodi"
s1=college()
print(s1.cname,s1.cloc)
college.cloc="kr puram"
print(college.cloc)
print(s1.cloc)
print("changeing location of college")
s1.cloc="hoodi"
print(s1.cloc)
print(college.cloc)'''

'''class student:
    sname="jeevitha"
    sloc="banglore"
s1=student()
print(s1.sname,s1.sloc)
student.sloc="mumbai"
print(student.sloc)
print(s1.sloc)'''

'''class college:
    cname="GCEM"
    loc="banglore"
s1=college()
s1.name="jeevitha"
s1.phone=1234567890
s1.loc="banglore"
s2=college()
s2.name="pallavi"
s2.phone=1987654321
s2.loc="Tiblisi"
print(s1.name,s1.phone)
print(s2.name,s2.phone)
print(s1.loc)
print(s2.loc)
print(s1.name,s1.phone,s1.loc)
print(s2.name,s2.phone,s2.loc)'''

'''class college:
    def __init__(self,name,phone,usn):
        self.usn = usn
        self.name = name
        self.phone = phone
    def display(self):
        print(self.name,self.phone,self.usn)

    def change_name(self,new):
        self.name = new
    def change_usn(self,new):
        self.usn = new

s1=college('jeevitha','12345','20')
s2=college('pallavi','152627','09')
print(s1.name)
print(s2.name)
s1.display()
s2.display()
s1.change_name("siya")
s1.change_usn("05")
s1.display()'''









