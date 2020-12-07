import random
import os

palavras = ["helena", "raira", "magaldi"]
palavra_secreta = random.choice(palavras)


def iniciar_jogo():
    numero_de_letras = len(palavra_secreta)
    tracos = "-" * numero_de_letras
    print(tracos)
    tentativas = 10

    while tentativas > 0 and tracos != palavra_secreta:
      print(tracos)
      print(tentativas)

      letra = input("Adivinhe uma letra: ")

      os.system("clear")
      
      if len(letra) != 1:
        print("você deve chutar apenas uma letra")
        tracos = atualizar_tracos(palavra_secreta, tracos, letra)

      elif letra in palavra_secreta:
        print("A letra está na palavra")
        tracos = atualizar_tracos(palavra_secreta, tracos, letra)

      else:
        print("A letra não está na palavra")
        tentativas -= 1
    
    if tentativas == 0:
      print("voce perdeu. A palavra era: " + palavra_secreta)

    else:
      print("parabens, voce ganhou!")

def atualizar_tracos(palavra_secreta, tracos, letra):
  resultado = ""

  # nome = "novs"
  # nome[0] = "n"
  for i in range(len(palavra_secreta)):
    if palavra_secreta[i] == letra:
      resultado += letra

    else:
      resultado += tracos[i]

  return resultado

iniciar_jogo()

print(palavra_secreta)