import os
import pandas as pd
import matplotlib.pyplot as plt

pasta_prep = "desafio_3_2/prep"

dataframes = []

for arquivo in os.listdir(pasta_prep):
    if arquivo.endswith(".xlsx"):
        caminho_arquivo = os.path.join(pasta_prep, arquivo)
        print(f"Processando arquivo: {caminho_arquivo}")

        df = pd.read_excel(caminho_arquivo)
        df['Arquivo'] = arquivo
        dataframes.append(df)

df_total = pd.concat(dataframes, ignore_index=True)

df_total['Data_Partida'] = pd.to_datetime(df_total['Data_Partida'])
df_total['Preco'] = pd.to_numeric(df_total['Preco'])
df_total['Dia_Semana'] = df_total['Data_Partida'].dt.day_name()

consolidado = df_total.groupby(
    ['Fonte', 'Data_Partida', 'Operador', 'Classe']
).agg(
    Total_Servicos=('Data_Hora_Partida', 'count'),
    Media_Ocupacao=('Ocupacao', 'mean'),
    Preco_Medio=('Preco', 'mean'),
    Menor_Preco=('Preco', 'min'),
).reset_index()

dias_maior_servico = (
    df_total.groupby('Data_Partida')
    .size()
    .reset_index(name='Total_Servicos')
    .sort_values(by='Total_Servicos', ascending=False)
)

classes_mais_utilizadas = (
    df_total['Classe']
    .value_counts()
    .reset_index(name='Frequencia')
    .rename(columns={'index': 'Classe'})
)

menor_preco_por_competidor = (
    df_total.groupby(['Operador', 'Dia_Semana'])
    .agg(Menor_Preco=('Preco', 'min'))
    .reset_index()
)

plt.figure(figsize=(10, 6))
plt.bar(dias_maior_servico['Data_Partida'].dt.strftime('%Y-%m-%d'), dias_maior_servico['Total_Servicos'])
plt.title("Dias com Maior Quantidade de Serviços")
plt.xlabel("Data de Partida")
plt.ylabel("Total de Serviços")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("desafio_3_2/mat_plot_imgs/dias_maior_servico.png")

plt.figure(figsize=(10, 6))
plt.barh(classes_mais_utilizadas['Classe'], classes_mais_utilizadas['Frequencia'])
plt.title("Classes de Serviço Mais Utilizadas")
plt.xlabel("Frequência")
plt.ylabel("Classe de Serviço")
plt.tight_layout()
plt.savefig("desafio_3_2/mat_plot_imgs/classes_mais_utilizadas.png")

pivot = menor_preco_por_competidor.pivot(index='Dia_Semana', columns='Operador', values='Menor_Preco')
pivot.plot(kind='bar', figsize=(17, 13))
plt.title("Menor Preço por Competidor e Dia da Semana")
plt.xlabel("Dia da Semana")
plt.ylabel("Menor Preço")
plt.xticks(rotation=45)
plt.legend(title="Operadores")
plt.tight_layout()
plt.savefig("desafio_3_2/mat_plot_imgs/menor_preco_por_competidor.png")

with pd.ExcelWriter("desafio_3_2/avaliacao_servicos.xlsx") as writer:
    consolidado.to_excel(writer, sheet_name="Consolidado", index=False)
    dias_maior_servico.to_excel(writer, sheet_name="Dias_Maior_Servico", index=False)
    classes_mais_utilizadas.to_excel(writer, sheet_name="Classes_Mais_Utilizadas", index=False)
    menor_preco_por_competidor.to_excel(writer, sheet_name="Menor_Preco_Competidor", index=False)

print("Análises concluídas! Resultados salvos em 'avaliacao_servicos.xlsx' e gráficos gerados.")
