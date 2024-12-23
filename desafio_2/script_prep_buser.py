import os
import pandas as pd

pasta_raw = "desafio_2/raw"
pasta_prep = "desafio_2/prep"

colunas_desejadas = {
    "Fonte": "modelo_venda_x",
    "Operador": "company_name_x",
    "Data_Hora_Partida": "datetime_ida_x",
    "Classe": "tipo_assento_x",
    "Origem": "origem.name",
    "Destino": "destino.name",
    "Preco": "preco_rodoviaria_x", 
    "Capacidade": "vagas_y",
    "Ocupacao": "pessoas",
    "Data_Hora_Captacao": "data_captacao"
}
ordem_colunas = [
    "Fonte", "Operador", "Data_Hora_Partida", "Data_Partida", "Hora_Partida",
    "Classe", "Origem", "Destino", "Preco", "Capacidade", "Ocupacao",
    "Data_Hora_Captacao", "Arquivo"
]

for arquivo in os.listdir(pasta_raw):
    if arquivo.endswith(".xlsx"):
        caminho_arquivo = os.path.join(pasta_raw, arquivo)
        print(f"Processando arquivo: {caminho_arquivo}")
        
        novo_nome = f"{os.path.splitext(arquivo)[0]}_preparado.xlsx"
        caminho_novo = os.path.join(pasta_prep, novo_nome)
        
        if os.path.exists(caminho_novo):
            print(f"Arquivo '{novo_nome}' já existe na pasta 'prep'. Pulando...")
            continue

        df = pd.read_excel(caminho_arquivo)
        
        df_filtrado = df[list(colunas_desejadas.values())]
        
        df_filtrado.columns = list(colunas_desejadas.keys())
        
        df_filtrado["Arquivo"] = arquivo
        df_filtrado["Data_Partida"] = pd.to_datetime(df_filtrado["Data_Hora_Partida"]).dt.date
        df_filtrado["Hora_Partida"] = pd.to_datetime(df_filtrado["Data_Hora_Partida"]).dt.time
        
        df_filtrado = df_filtrado[ordem_colunas]
        df_filtrado.to_excel(caminho_novo, index=False)
        print(f"Arquivo preparado e movido para: {caminho_novo}")
