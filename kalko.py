
num1 = float(input("Sisesta esimene number: "))  
mata = input("Sisesta (+, -, *, /): ")      
num2 = float(input("Sisesta teine number: "))    

if mata1 == "+":
    mata2 = num1 + num2
    print("Tulemus on:", mata)

elif mata == "-":
    mata2 = num1 - num2
    print("Tulemus on:", mata)

elif mata1== "*":
    mata2 = num1 * num2
    print("Tulemus on:", mata)

elif mata1 == "/":
    if num2 != 0:
        mata2 = num1 / num2
        print("Tulemus on:", mata)
    else:
        print("Pole võimalik bro!")  

else:
    print("Nii pole võimalik teha.")  
