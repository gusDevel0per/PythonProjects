palavra_chave="Babaisyou"
palavra=["_","_","_","_","_","_","_","_","_",]

print(palavra)

acertou=False
enforcou=False
erros=0
while not acertou and not enforcou:

    chute = input("Digite uma letra ")

    for i,letra in enumerate(palavra_chave):
        if chute.upper()==letra.upper():
            palavra[i]=chute

        if chute not in palavra_chave:
            erros+=1

        acertou = not '_' in palavra
        enforcou = erros==5

        print(palavra)
