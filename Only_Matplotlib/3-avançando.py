
import matplotlib.pyplot as plt
import numpy as np

# Dados para análise
meses = ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"] #messes a serem analisados
vendas = [120, 150, 135, 180, 210, 195] #quantidade de vendas por mes
metas = [130, 140, 150, 160, 180, 200] #a meta que cada mes tinha

# Criação da figura e dos espaços dos gráficos
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5)) #criação dos graficos e dimensão da figura

# Primeiro gráfico: barras
ax1.bar(meses, vendas, color="steelblue", label="Vendas") #grafico de barras com messes sendo as categorias e vendas sendo as vendas 

# Segundo gráfico: linhas
ax2.plot(meses, vendas, marker="o", color="green", label="Vendas") #dois graficos de linhas ambos usando messes como x o intuito é saber os messes que as vendas bateram as metas  
ax2.plot(meses, metas, marker="s", linestyle="--", color="red", label="Metas")

# Personalização do primeiro gráfico
ax1.set_title("Vendas por mês") #titulo do grafico 1
ax1.set_xlabel("Meses") # titulo do eixo x
ax1.set_ylabel("Quantidade de vendas") #label do eixo y
ax1.grid(axis="y", alpha=0.3) 

# Personalização do segundo gráfico
ax2.set_title("Vendas x Metas") #titulo do grafico 2
ax2.set_xlabel("Meses") #label do x no ax2
ax2.set_ylabel("Quantidade") #label do y no ax2
ax2.legend() #coloca legenda no canto do 

# Ajuste dos espaços entre os gráficos
plt.tight_layout() #faz o layout se ajustar

# Exibição
plt.show()
