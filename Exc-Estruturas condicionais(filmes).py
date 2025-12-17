filmes = ["malevola","moana","os elementos","rapunzel"," os incriveis "]
["malevola","moana","os elementos","rapunzel","os incriveis"]
print("vamos jogar um jogo de classificar filmes")
print("você tem alguns filmes para classificar. ")
print("quando quiser sair aperte 0.\n")

for filme in filmes:
    classificação = input(f"como você classifica o '{filme}' de 1 a 5 ?")

    if classificação == '0':
        print("goodbye")
        break
    classificação = int(classificação)

    if classificação < 1 or classificação > 5:
        print("Tankyou, rate ")
    else:
        print(f"você classificou '{filme}'com '{classificação} estrelas. \n")

print("obrigado por classificar os filmes <3")