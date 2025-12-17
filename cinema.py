idade = int(input("poderia me dizer sua idade : "))

if idade < 12:
    print("a vida e uma festa, e moana 2")
elif 12 <= idade < 18:
    print("castelo animdo,a viagem de chihiro ")
else:
    print("rick morty,south park,simpsons")

quantidade_ibgressos = int(input("quantos ingresos vai querer? :"))
if quantidade_ibgressos > 0:
    print("disponivel")
else:
    print("tente de novo parceiro")