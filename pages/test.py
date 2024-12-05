import pandas as pd

dados = {
    'Nome': ['Lucas', 'Ana', 'Pedro'],
    'Idade': [25, 30, 22],
    'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte']
}

# Criando o DataFrame
df = pd.DataFrame(dados)

# Salvando no arquivo CSV
df.to_csv('dados.csv', index=False, encoding='utf-8')