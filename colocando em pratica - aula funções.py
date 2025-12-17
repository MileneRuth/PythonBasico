notas = [7.5,8.0,6.5,3]
def calcularMedia(notas):
    total = sum(notas)
    media = total / len(notas)
    return media
arredondar = lambda media: round(media,2)

media = calcularMedia(notas)
arredondar = arredondar(media)

situacao = "Aprovado" if arredondar >= 7 else "Reprovado"

print("notas do estudante", notas)
print("media das notas",arredondar)
print("situação do aluno ",situacao)