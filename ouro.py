import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FormatStrFormatter

def limpar_valores_high(dataframe): oi
def limpar_valores_high(dataframe): 
    """Remove casas decimais extras da coluna High"""
    mapeamento_valores = {
        '1064.5999755859375': '1064.5',
        '1068.4000244140625': '1068.4',
        '1066.199951171875': '1066.1',
        '5586.2001953125': '5586.2',
        '5303.7998046875': '5303.7',
        '5301.60009765625': '5301.6'
    }
    
    for valor_original, valor_limpo in mapeamento_valores.items():
        dataframe.loc[dataframe['High'] == valor_original, 'High'] = valor_limpo
    
    return dataframe

def gerar_grafico(ano, valores, titulo, tipo_venda):
    """Gera gráfico com os dados fornecidos"""
    plt.figure(figsize=(10, 6))
    plt.bar(ano, valores)
    plt.plot(ano, valores)
    plt.scatter(ano, valores)
    plt.ylabel('Valores')
    plt.xlabel('Ano')
    plt.xticks(ano)
    plt.title(titulo)
    plt.show()

while True:
    print('1) Maiores vendas do ouro')
    print('2) Menores vendas do ouro')
    perg = int(input('Oque você deseja:? '))

    # Carregar dados
    info = pd.read_csv('Gold_Data.csv')
    
    # Limpar valores com casas decimais extras
    info = limpar_valores_high(info)

    # Filtrar e ordenar dados
    filtro_maiores = info.sort_values('High', ascending=False).head(6)
    filtro_menores = info.sort_values('High', ascending=True).head()

    if perg == 1:
        ano = filtro_menores['Price']
        valores = filtro_menores['High']
        gerar_grafico(ano, valores, 'Menores vendas do ouro', 'menores')

    elif perg == 2:
        ano = filtro_maiores['Price']
        valores = filtro_maiores['High']
        gerar_grafico(ano, valores, 'Maiores vendas do ouro', 'maiores')

    else:
        print('Opção inválida')



