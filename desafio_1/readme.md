# Desafio 1

## Visão Geral
Este script coleta dados de viagens de ônibus do site ClickBus e gera um relatório em formato Excel.

---

## Etapas

### 1. Geração da URL
A função `generate_url` cria uma URL dinâmica para buscar dados, baseando-se na data atual e na data de retorno (15 dias após).

### 2. Coleta de Dados
A função `clickbus_data` realiza os seguintes passos:
1. Faz uma requisição HTTP para a URL gerada.
2. Analisa o HTML da página para encontrar um JSON com os dados das viagens.
3. Extrai informações como preços, horários e locais usando a função `extract_data`.

### 3. Criação do Relatório
A função `generate_excel` gera um arquivo Excel com os dados coletados.

---

## Como Usar
1. Certifique-se de ter as dependências instaladas:
   ```bash
   pip install -r requirements.txt
   ```
2. Execute o script:
   ```bash
   python desafio_1/main.py
   ```

---

## Resultado
- Um arquivo `desafio_1/relatorio_viagens.xlsx` será gerado contendo os dados das viagens coletadas.

