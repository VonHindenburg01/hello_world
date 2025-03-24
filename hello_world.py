print("Hello Class")
print("Hello dev")
A = float(input("Input A: "))
B = float(input("Input B: "))  
operator = input("Operator (+, -, *, /): ")
if operator == '+':
    result=A+B 
elif operator == '-':
    result=A-B
elif operator == '*':
    result=A*B
elif operator =='/':
    result=A/B
else:
    result="Erreur: Division par zéro"
       