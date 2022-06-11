dicionario = {}


#inserir elemento

dicionario['andre sales'] = 'estudante sofrido'

#inserindo a partir do input

nome_colaborador = input('por favor informe o nome do colaborador: ')
cargo_colaborador = input('por favor informe o cargo do colaborador: ')

dicionario[nome_colaborador] = cargo_colaborador

for nome, cargo in dicionario.items():
  print(f'o colaborador {nome} atua no cargo de {cargo}')