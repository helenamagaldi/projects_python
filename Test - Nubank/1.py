n = 16
pontuacao_array = np.random.randint(1,50,16)
pontuacao = pontuacao_array.tolist()

print(pontuacao)
tamanho_do_time = 6
k = 4
escolhidos = [] * tamanho_do_time
print(escolhidos)

sliced1 = pontuacao[0:3]
value1 = max(pontuacao[0:3])
index_value1 = sliced1.index(max(sliced1))

sliced2 = pontuacao[12:15]
value2 = max(pontuacao[12:15])
index_value2 = sliced2.index(max(sliced2))

print(value1, value2)
# print(sliced1, sliced2, value1, value2, index_value1, index_value2)

if value1 > value2:
  escolhidos.append(value1)
  pontuacao.pop(index_value1)
else:
  escolhidos.append(value2)
  pontuacao.pop(index_value2)


print(pontuacao)
print(escolhidos)