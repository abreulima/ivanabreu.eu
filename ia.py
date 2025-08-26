import pandas as pd
import matplotlib.pyplot as plt

# ------------------------------
# 1. Criar CSV com 30 registros
# ------------------------------

dados = """Nome,Idade,Plataforma,Gênero
Ana,15,Netflix,Ação
Bruno,16,Amazon Prime,Terror
Carlos,15,Disney+,Animação
Duda,17,Netflix,Romance
Eduardo,14,HBO Max,Terror
Fernanda,16,Netflix,Ação
Gustavo,17,Disney+,Aventura
Helena,15,Amazon Prime,Romance
Igor,14,HBO Max,Aventura
Julia,17,Netflix,Animação
Karla,16,HBO Max,Aventura
Luis,13,Disney+,Animação
Marta,15,Netflix,Romance
Nina,16,Amazon Prime,Terror
Otávio,14,HBO Max,Terror
Paula,17,Netflix,Ação
Quintino,15,Netflix,Ação
Rafaela,14,Disney+,Animação
Samuel,13,HBO Max,Terror
Tatiana,16,Amazon Prime,Aventura
Ubirajara,15,Disney+,Romance
Viviane,17,Netflix,Animação
Willian,14,HBO Max,Aventura
Xuxa,13,Amazon Prime,Animação
Yasmin,16,Netflix,Romance
Zeca,15,Disney+,Ação
Amanda,14,Netflix,Terror
Brenda,17,HBO Max,Romance
Caio,13,Amazon Prime,Aventura
Daniela,15,Disney+,Ação
"""

# Salvar o arquivo
with open("filmes.csv", "w", encoding="utf-8") as f:
    f.write(dados)

# ------------------------------
# 2. Carregar e explorar os dados
# ------------------------------

df = pd.read_csv("filmes.csv")

print("Primeiras linhas:")
print(df.head())

print("\nContagem de plataformas:")
print(df["Plataforma"].value_counts())

print("\nContagem de gêneros:")
print(df["Gênero"].value_counts())

# ------------------------------
# 3. Visualizações simples
# ------------------------------

# Gráfico de barras - plataformas
plataformas = df["Plataforma"].value_counts()
plt.bar(plataformas.index, plataformas.values)
plt.title("Plataformas Favoritas")
plt.xlabel("Plataforma")
plt.ylabel("Quantidade")
plt.show()

# Gráfico de pizza - gêneros
generos = df["Gênero"].value_counts()
plt.pie(generos.values, labels=generos.index, autopct='%1.1f%%')
plt.title("Gêneros Favoritos")
plt.show()

# ------------------------------
# 4. Previsão simples com regras
# ------------------------------

def prever_plataforma(idade):
    if idade <= 14:
        return "HBO Max"
    elif idade <= 16:
        return "Netflix"
    else:
        return "Disney+"

df["Plataforma_Prevista"] = df["Idade"].apply(prever_plataforma)
df["Acertou?"] = df["Plataforma"] == df["Plataforma_Prevista"]

print("\nPrevisões:")
print(df[["Nome", "Idade", "Plataforma", "Plataforma_Prevista", "Acertou?"]])

# Gráfico de acertos
acertos = df["Acertou?"].value_counts()
plt.bar(acertos.index.astype(str), acertos.values)
plt.title("Acertos na Previsão")
plt.xlabel("Acertou?")
plt.ylabel("Quantidade")
plt.show()

# ------------------------------
# 5. Mini-desafio: melhor plataforma para ação
# ------------------------------

acao = df[df["Gênero"] == "Ação"]
plataformas_acao = acao["Plataforma"].value_counts()

print("\nPlataformas preferidas por fãs de Ação:")
print(plataformas_acao)

plt.bar(plataformas_acao.index, plataformas_acao.values)
plt.title("Plataforma dos fãs de Ação")
plt.xlabel("Plataforma")
plt.ylabel("Quantidade")
plt.show()
