dicionario ={
  "Yoda": "Mestre Jedi",
  "Mace Windu": "Mestre Jedi",
  "Anakin Skywalker": "Cavaleiro Jedi",
  "R2-D2": "droide",
  "Dex": "Balconista"
  }

# for valor in dicionario.values():
#   print(valor)
  

# for chave in dicionario.keys():
#   print(chave)

# print (dicionario["R2-D2"])

for chave, valor in dicionario.items():
  print(f'{chave} -- {valor}')