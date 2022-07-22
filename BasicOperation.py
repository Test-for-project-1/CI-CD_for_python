"""
Basic math operation
"""

def add(first, second):
    return first+second

def sub(first, second):
    return first-second

def mul(first,second):
    return first*second

if __name__ == "__main__":
    print("select the operation:\n 1->Add\n 2->Subration\n 3->Multiplication")
    operator = input()
    if(operator=='1'):
        func=add
    elif(operator=='2'):
        func=sub
    elif(operator=='3'):
        func=mul
    else:
        raise ValueError(f'Supported options are 1, 2 and 3 but you entered {operator}')
    value1= int(input('Enter the first value: '))
    value2= int(input('Enter the second value: '))
    result= func(value1,value2)
    print(f'Result is: {result}')