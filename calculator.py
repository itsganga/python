print(
    '''
    ADD
    SUBTRACT
    MULTIPLE
    DIVIDE
    '''
)
num1 = int(input("Enter The Value1: "))
num2 = int(input("Enter The Value2: "))
opr = input("Enter the Operation.. (+, -, *, / ):")
if opr == "+":
    print(num1+num2)
elif opr =="-":
    print(num1-num2)
elif opr == "*":
    print(num1*num2)
elif opr == '/':
    print(num1/num2)
else: print("Invalid Operation")