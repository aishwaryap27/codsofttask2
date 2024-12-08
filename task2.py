a=int(input("enter one number"))
b=int(input("enter another number"))
print("1.addition +\n2.subtraction -\n3.multiplication *\n 4.exponential **\n 5.division /\n 6.modulus %") 
c=input("enter operator")


#print("enter 100 to exit")
if(c=='+'):
    res=a+b
elif(c=='-'):
    res=a-b
elif(c=='*'):
    res=a*b
elif(c=='/'):
    res=float(a/b)
elif(c=='%'):
    res=float(a%b)
elif(c=="**"):
    res=a**b
print("result is",res)
