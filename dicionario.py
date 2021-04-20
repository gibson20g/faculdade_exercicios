import pandas as pd
nomes = str(input('Infome Nome Funcionario teste: '))
senha = int(input('Informe a senha: '))
funcionario = {'Nome': [nomes],
               'Senha': [senha],
               }
df = pd.DataFrame(data=funcionario, columns=['Nome', 'Senha'])
print(df)
