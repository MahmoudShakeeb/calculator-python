import math


while True:

  print("---------------------------------")
  print("Standard calculator   press 1 ")
  print("programmer Calculator press 2 ")
  print("exit                  press 0 ")
  print("---------------------------------")
  Mode = int(input("enter your choice: "))
  print("---------------------------------")
#   num1 = int(input("Enter num1: "))
#   num2 = int(input("Enter num2: "))
  print("---------------------------------")
 
  if Mode == 1:
    print("_____This is Standard Mode_____")
    num1 = int(input("please Enter num1 :"))
    num2 = int(input("please Enter num2 :"))
    print('''1.Add 
             2.sub 
             3.Mul 
             4.div 
             5.power 
                         '''  )
    operation = int(input("please Enter The operation :"))
    if operation == 1:
        result = int(num1) + int(num2)
        print("The Add = ",result) 
    elif operation == 2:
        result = int(num1) - int(num2)
        print("The sub = ",result) 
    elif operation == 3 :
        result = int(num1) * int(num2)
        print("The Mul = ",result) 
    elif operation == 4 :
        if num2 == 0:
            print("you cant divid by zero ")
        else:    
           result = float(num1) / float(num2)
           print("The Add = ",float(result)) 
    elif operation == 5 :
        result = int(num1) ** int(num2)
        print("The power = ",result) 
    else: 
        print("invalid Operation")                
  elif Mode == 2:
    print("_____This is programmer Mode_____")
    print("------------------------------------------------")
    print("AND operator                         press 1 ")
    print("OR operator                          press 2 ")
    print("XOR operator                         press 3 ")
    print("NOT operator                         press 4 ")
    print("convert from decimal to binary       press 5 ")
    print("convert from decimal to hexadecimal  press 6 ")
    print("convert from decimal to octal        press 7 ")
    print("Exit                                 press 0 ")
    print("------------------------------------------------")
    operation = int(input("please Enter your choice :"))
    if operation == 1:
        result = num1 & num2
        print("And op = ",result) 
    elif operation == 2 :
        result = num1 | num2
        print("OR op = ",result)
    elif operation == 3 :
        result = num1 ^ num2
        print("XOR op = ",result)
    elif operation == 4 :
        print("--------------------------------------------")
        print("Do u want to use NOT operator on num1  press 1 ")
        print("Do u want to use NOT operator on num2  press 2 ")
        print("--------------------------------------------")
        not_op_num = int(input("Your choice : "))
        if not_op_num == 1:
            result = ~num1
            print("NOt Op for num1 = ",result)
        elif not_op_num == 2:
            result = ~num2
            print("NOt Op for num2 = ",result)
    elif operation == 5:
        print("--------------------------------------------")
        print("Do u want to convert from decimal to binary for num1 press 1 ")
        print("Do u want to convert from decimal to binary for num2 press 2 ")
        print("--------------------------------------------")
        dec_bin_num = int(input("Your choice : "))
        if dec_bin_num == 1:
             result = bin(num1)
             print("from decimal to bin for num 1 = ",result)
        elif dec_bin_num == 2:
             result = bin(num2)
             print("from decimal to bin for num 2 = ",result)                                 
    elif operation == 6:
        print("--------------------------------------------")
        print("Do u want to convert from decimal to hexa for num1 press 1 ")
        print("Do u want to convert from decimal to hexa for num2 press 2 ")
        print("--------------------------------------------")
        dec_hex_num = int(input("Your choice : "))
        if dec_hex_num == 1:
             result = hex(num1)
             print("from decimal to hexa for num 1 = ",result)
        elif dec_hex_num == 2:
             result = hex(num2)
             print("from decimal to hexa for num 2 = ",result)     
    elif operation == 7:
        print("--------------------------------------------")
        print("Do u want to convert from decimal to oct for num1 press 1 ")
        print("Do u want to convert from decimal to oct for num2 press 2 ")
        print("--------------------------------------------")
        dec_oct_num = int(input("Your choice : "))
        if dec_oct_num == 1:
             result = oct(num1)
             print("from decimal to oct for num 1 = ",result)
        elif dec_oct_num == 2:
             result = oct(num2)
             print("from decimal to oct for num 2 = ",result)
    elif operation == 0:
        exit()              
    else:
        print("invaled operation")
        exit()
