
num1 = float(input("Sisesta esimene number: "))  
matapask = input("Sisesta (+, -, *, /): ")      
num2 = float(input("Sisesta teine number: "))    

if matapask == "+":
    mata = num1 + num2
    print("Tulemus on:", mata)

elif matapask == "-":
    mata = num1 - num2
    print("Tulemus on:", mata)

elif matapask == "*":
    mata = num1 * num2
    print("Tulemus on:", mata)

elif matapask == "/":
    if num2 != 0:
        mata = num1 / num2
        print("Tulemus on:", mata)
    else:
        print("Pole võimalik bro!")  

else:
    print("Nii pole võimalik teha.")  
