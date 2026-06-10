# 1. variables is a container which stores data 
a=10 #there is no need to write data type in python 
b=5.5
name ="vivek"

print(type(a))#print the type 
print(type(b))
print(type(name))

isPass=True#boolean 

x=3+4j#complex

a="10"
b=int(a)

print(b)
print(type(b))

name="vivek"
age=20

print(name,age)
print("my name is {name} and age is { age}")

a=int(input("enter first number :"))
b=float(input("enter second number :"))

a=10
b=5
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a//b)
print(a**b)

print(a>b)
print(b<a)
print(a==b)
print(a!=b)

x = True
y = False

print(x and y)
print(x or y)
print(not x)

age = 18;

if age >= 18:
    print("Adult")
else :
    print("minor")



marks = 85
if marks>90:
    print("GRADE IS A:")
elif marks>80:
    print("GRADE IS B:")
elif marks>70:
    print("GRADE IS C:")
else 
    print("FAIL:")


#file handling 

f=open("data.txt","w")
f.write("Hello my name is vivek :")
f.close()

f=open("data.txt","r")
print(f.read())
f.close()

#read line by line in file 
f=open("data.txt","r")
for line in f:
    print(line)
f.close()

#append mode (kisi file me last me data add krne k liye use hota hai)

f=


