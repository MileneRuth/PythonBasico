peso = float(input("Qual e o seu peso em KG: "))
altura = float(input("Qual sua altura em metros: "))
imc = peso / (altura ** 2)
print(f"Seu IMC é: {imc:.2f}")

if imc < 18.5:
     print("Abaixo do peso.")
elif 18.5 <= imc < 24.9:
     print("Seu peso esta normal")
elif 25 <= imc < 29.9:
     print(" Sua classificação: sobrepeso ")
else:
     print("Sua classificação: Obesidade ")