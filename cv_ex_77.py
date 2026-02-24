palavras = ('arroz', 'feijao','mulher','nix','julio','python','mochila','morango','aprender')
for p in palavras:
    print(f'\nNa palavras {p} temos ', end='')
    for letras in p :
        if letras in ('aeiou'):
            print(letras, end=' ')