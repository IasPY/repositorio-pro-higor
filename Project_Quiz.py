nome = input("Qual o seu nome?:")
lista1 = ["sim", "Sim", "SIM", "sIm", "siM", "Sim"]
lista2 = ["não", "nao", "NÂO", "NAO", "Não", "NÃo", "NãO", "NaO", "nAO", "nÃO", "naO", "nAo", "nÃo"]
print(f"Bem-vindo ao quiz {nome}")
while True:
    p1 = input("Você se sente preparado? ")
    if p1 in lista1:
        print("Excelente!, vamos começar")
        break
    elif p1 in lista2:
        print(f"Vamos começar mesmo assim, {nome}")
        break
    else:
        print("Resposta inadequada")
while True:
    p2 = input("Qual a definição de versionamento de código esta correta?: \n Opção a)Gerenciamento de alterações no "
               "código-fonte ao longo do tempo"
               "\n Opção b)Técnica para atualizar automaticamente o código em diferentes idiomas\n Opção c) Processo "
               "para"
               "compactar arquivos de código antes da distribuição\n Opção d)Método para criar backups de documentos de"
               " texto.").lower()
    if p2 == "a":
        print("Exatamente!")
        break
    elif p2 in ["b", "c", "d"]:
        print("Errou!,  Tente de novo")
    else:
        print("É SÉRIO?")
while True:
    p3 = input("Escreva o verbo da frase?: Os jogadores foram para o jogo. ").lower()
    if p3 == "foram":
        print("Fez o mínimo")
        break
    elif p3 != "foram":
        print("COMO VOCÊ ERROU ISSO?, Tente de novo")
while True:
    p4 = input("Qual é a capital do Brasil em 1615?: \n a)Säo Paulo\n b) Rio de Janeiro\n c) Brasília\n d) Salvador"
               ).lower()
    if p4 == "d":
        print("Parabéns, seguimos")
        break
    elif p4 in ["a", "b", "c"]:
        print("Errou!, tente novamente")
while True:
    p5 = input("Quem pintou a Monalisa?: \n a)Pablo Picasso\n b)Van gogh\n c) Leonardo da Vinci\n "
               "d) Michelangelo").lower()
    if p5 == "c":
        print("`Parabéns!")
        break
    elif p5 in ["a", "b", "d"]:
        print("Errou!, tente de novo")
print(f"Finalmente chegamos ao fim {nome}, espero que tenha gostado do quiz! ")
