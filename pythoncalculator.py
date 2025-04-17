a=int(input('Enter the value:'))
b=int(input('Enter the value:'))
x=input('Enter Operation:')

if x=="+":
    print("result:", a+b)
elif x=="-":
    print("result", a-b)
elif x=="*":
    print("result:", a*b)
elif x=="/":
    print("result", a/b)
else:
    print("Invalid Operation")