import os 
os.system ("cls") 

nome=input("Digite seu nome:")
peso=float(input("Digite seu peso:"))
altura=float(input("Digite sua altura:"))

imc =  peso/ (altura** 2)

print (f"Seu IMC é: {imc:.2f}")

if imc < 18.9:
    print("Abaixo do peso")
elif imc < 24.9:
    print("Peso normal")
elif imc < 29.9:
    print("Sobrepeso")
elif imc < 34.9:
    print("Obesidade Grau I")
elif imc < 39.9:
    print("Obesidade Grau II")
elif imc < 40.0:
    print("Obesidade Grau III ")
else:
    print("Procure um médico")
     