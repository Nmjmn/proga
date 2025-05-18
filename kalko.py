num1 = float(input("Sisesta esimene number: "))  
mata1 = input("Sisesta (+, -, *, /): ")      
num2 = float(input("Sisesta teine number: "))    

if mata1 == "+":
    mata2 = num1 + num2
    print("Tulemus on:", mata2)

elif mata1 == "-":
    mata2 = num1 - num2
    print("Tulemus on:", mata2)

elif mata1== "*":
    mata2 = num1 * num2
    print("Tulemus on:", mata2)

elif mata1 == "/":
    if num2 != 0:
        mata2 = num1 / num2
        print("Tulemus on:", mata2)
    else:
        print("Pole võimalik bro!")  

else:
    print("Nii pole võimalik teha.")  
