import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('dados/ecommerce_preparados.csv')

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

print(df.head())
print(df.tail())

#campos para uso
# Nota, N_Avaliações, Marca, Material, Qtd_Vendidos, Preço

# Possíveis campos para one hot/comparação
# Temporada_Cod, Marca_Freq, Material_Freq

# Histograma básico de notas
sns.histplot(data=df, x='Nota', kde=True)
plt.title('Distribuição de Notas')
plt.xlabel('Nota')
plt.ylabel('Quantidade')
plt.show()

# Scatterplot básico de notas x quantidade de avaliações
sns.scatterplot(data=df, x='Nota', y='N_Avaliações')
plt.title('Distribuição de Notas')
plt.xlabel('Nota')
plt.ylabel('Quantidade de Avaliações')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

# Heatmap
corr = df[['Nota', 'N_Avaliações', 'Marca_Freq', 'Qtd_Vendidos_Cod', 'Preço']].corr()

corr.columns = ['Nota', 'Nº Avaliações', 'Freq Marca', 'Qtd Vendidos', 'Preço']
corr.index = ['Nota', 'Nº Avaliações', 'Freq Marca', 'Qtd Vendidos', 'Preço']

sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title('Heatmap')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Barra
sns.barplot(data=df, x='Nota', y='Qtd_Vendidos_Cod', errorbar=None)
plt.title('Vendas por Nota')
plt.xlabel('Nota')
plt.ylabel('Quantidade Vendida')
plt.grid(True, linestyle='--', alpha=0.6)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Pizza
# Gráfico de Pizza (Pie Chart) com agrupamento "Outros"
gen_count = df['Gênero'].value_counts()

# 1. Calcular a porcentagem de cada categoria
total = gen_count.sum()
percentages = (gen_count / total) * 100

# 2. Filtrar quem é maior ou igual a 5% e quem é menor
mask_maiores = percentages >= 5.0
maiores = gen_count[mask_maiores]
outros_valor = gen_count[~mask_maiores].sum()

# 3. Criar a nova série de dados para o gráfico
if outros_valor > 0:
    # Criamos um objeto Series para o "Outros" e concatenamos com as categorias maiores
    outros_serie = pd.Series({'Outros': outros_valor})
    dados_pizza = pd.concat([maiores, outros_serie])
else:
    dados_pizza = maiores

plt.figure(figsize=(10, 6))
plt.pie(dados_pizza, labels=dados_pizza.index, autopct='%.1f%%', startangle=90)
plt.title('Distribuição por gênero')
plt.axis('equal')
plt.tight_layout()
plt.show()

# Densidade
plt.figure(figsize=(10, 6))
sns.kdeplot(df['Nota'], fill=True, color='#863e9c')
plt.title('Densidade de Notas')
plt.xlabel('Nota')
plt.ylabel('Densidade')
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()


# Regressão
plt.figure(figsize=(10, 6))
sns.regplot(x='Preço_MinMax', y='Desconto_MinMax', data=df, scatter_kws={'alpha': 0.5})
plt.title('Regressão entre Desconto e Preço')
plt.xlabel('Preço')
plt.ylabel('Desconto')
plt.grid(True, linestyle='--', alpha=0.6)
plt.tight_layout()
plt.show()

