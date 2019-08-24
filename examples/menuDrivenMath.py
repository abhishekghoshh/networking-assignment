print "Choose from the option below"
print "1.Addition"
print "2.Substraction"
print "3.Multiplication"
print "4.Divison"
print "5.Exit"

op=int(raw_input("Enter your option from 1 to 5 : "))

if(op==5):
    exit()
    
num1=float(raw_input("Enter number one : "))
num2=float(raw_input("Enter number one : "))



if(op==1):
    add= float(num1+num2)
    print "The addition is ",add
if(op==2):
    sub= float(num1-num2)
    print "The substraction is ",sub
if(op==3):
    mul= float(num1*num2)
    print "The multiplication is ",mul
if(op==4):
    div= float(num1/num2)
    print "The division is ",div
