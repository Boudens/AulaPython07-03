import os

def MediaNotas(nota1_,nota2_,nota3_,char):

    if(char == 's'):
        media = (nota1_ + nota2_ + nota3_)/3
    else:
        media = (nota1_ + nota2_ + 0)/2

    return media

nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))

print("O aluno fez 3 avaliações (s para sim / n para não) ?")
opcao = input()[0]

if(opcao == 's' or opcao == 'S'):
    nota3 = float(input("Informe a terceira nota: "))
    media = MediaNotas(nota1,nota2,nota3,'s')
else:
    media = MediaNotas(nota1,nota2,0,'n')


os.system('cls')
if(opcao == 'S' or 's'):
    print(f"Os números foram {nota1:.1f} e {nota2:.1f} e {nota3:.1f} ")
else:
    print(f"Os números foram {nota1:.1f} e {nota2:.1f}")

print(f"A média é {media:.1f}")

