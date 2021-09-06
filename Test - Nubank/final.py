n = 16
pontuacao_array = np.random.randint(1,50,16)
pontuacao = pontuacao_array.tolist()

print(pontuacao)
tamanho_do_time = 6        
k = 4
escolhidos = []
print(escolhidos)

for vagas in range(tamanho_do_time):
  start_slice = pontuacao[0:4]
  end_slice = pontuacao[-4:]

  max_start_slice = max(pontuacao[0:4])
  index_max_start = pontuacao.index(max(start_slice))

  max_end_slice = max(pontuacao[-4:])
  index_max_ending = pontuacao.index(max(end_slice))  

  if max_start_slice > max_end_slice:
    escolhidos.append(max_start_slice)
    pontuacao.pop(index_max_start) 
  else:
    escolhidos.append(max_end_slice)
    pontuacao.pop(index_max_ending)


sum(escolhidos)
