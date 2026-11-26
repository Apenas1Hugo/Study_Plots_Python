import matplotlib.pyplot as plt

categorias = ["Maça","Uva", "morango"] 

qtd = [10,5,3]

fig, (fig1, fig2) = plt.subplots(1,2) #cria dois graficos e diz suas posiçoes 

fig1.bar(categorias, qtd); #grafico de barras
fig2.pie(qtd, labels=categorias, autopct="%.1f%%"); #grafico de pizza

plt.tight_layout()
plt.show()