
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# messes
dados = {
    "mes": ["Jan", "Fev", "Mar", "Abr", "Mai", "Jun"],
    "vendas": [120, 150, 135, 180, 210, 195],
    "meta": [130, 140, 150, 160, 180, 200]
}
#cria dataframe com os messes 
df = pd.DataFrame(dados)

#coluna resultado vai ter "atingiu" se vendas for maior que meta se não "abaixou"
df["resultado"] = np.where(
    df["vendas"] >= df["meta"],
    "Atingiu",
    "Abaixo"
)
#diferença é colunas vendas - meta
df["diferenca"] = df["vendas"] - df["meta"]

# condicional para cores 
cores = np.where(
    df["resultado"] == "Atingiu",
    "seagreen",
    "indianred"
)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(13, 5))

#grafico de barras vendas por mes 
ax1.bar(df["mes"], df["vendas"], color=cores)

#grafico de linhas metas wm cada mes
ax1.plot(
    df["mes"],
    df["meta"],
    color="black",
    linestyle="--",
    marker="o",
    label="Meta"
)

#personalizaçoes dos graficos 
ax1.set_title("Vendas e metas por mês")
ax1.set_xlabel("Meses")
ax1.set_ylabel("Quantidade")
ax1.legend()
ax1.grid(axis="y", alpha=0.3)

#segundo grafico de barras diferença dos messes
ax2.bar(
    df["mes"],
    df["diferenca"],
    color=np.where(df["diferenca"] >= 0, "seagreen", "indianred")
)
#personalização do ax2
ax2.axhline(y=0, color="black", linewidth=0.8)
ax2.set_title("Diferença entre vendas e metas")
ax2.set_xlabel("Meses")
ax2.set_ylabel("Diferença")
ax2.grid(axis="y", alpha=0.3)

plt.tight_layout()
plt.show()