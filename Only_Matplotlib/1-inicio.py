import matplotlib.pyplot as plt

#dados do grafico que serão usados para construir a linha
y = [2,4,6,8,10,12,14,-16,18,20,22]

#dados do eixo X para mostrar a historia da linha pois se trata de um histograma  
x = [1,2,3,4,5,6,7,8,9,10,11]

#função de criar o grafico 
plt.plot(x,y);

#função de mostrar o grafico 
plt.show()