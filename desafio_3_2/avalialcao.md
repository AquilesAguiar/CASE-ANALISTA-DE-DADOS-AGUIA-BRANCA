# Documentação da Avaliação de Serviços

## Objetivo

O objetivo deste trabalho é consolidar e analisar dados de serviços de transporte coletados em vários arquivos Excel (“.xlsx”) para identificar padrões e gerar insights sobre as operações de diferentes operadores, fontes e classes de serviço.

O resultado final inclui:

- Consolidação das informações.
- Análises de padrões observados.
- Visualizações gráficas.
- Geração de um arquivo Excel consolidado.

## Etapas Realizadas

### 1. Leitura e Consolidação dos Dados

Os dados foram extraídos de múltiplos arquivos localizados em uma pasta específica. Cada arquivo foi lido utilizando a biblioteca `pandas`, e os seguintes campos foram considerados como comuns entre os arquivos:

- **Fonte**: Fonte de origem do dado.
- **Operador**: Empresa responsável pelo serviço.
- **Data_Hora_Partida**: Data e hora da partida.
- **Data_Partida**: Apenas a data da partida.
- **Hora_Partida**: Apenas o horário da partida.
- **Classe**: Classe do serviço.
- **Origem**: Local de origem da viagem.
- **Destino**: Local de destino da viagem.
- **Preço**: Valor do serviço.
- **Capacidade**: Quantidade total de assentos no serviço.
- **Ocupacao**: Quantidade de assentos ocupados.
- **Data_Hora_Captacao**: Data e hora de captação do dado.
- **Arquivo**: Nome do arquivo de origem do dado.

### 2. Agrupamento e Consolidação

Os dados foram consolidados por:

- **Fonte de dados**.
- **Data de partida**.
- **Operador**.
- **Classe de serviço**.

As métricas calculadas incluem:

- **Total de Serviços**: Quantidade de serviços oferecidos no agrupamento.
- **Média de Ocupação**: Ocupação média dos serviços.
- **Preço Médio**: Valor médio dos serviços no agrupamento.
- **Menor Preço**: Menor preço registrado no agrupamento.

### 3. Análises Realizadas

#### 3.1. Dias com Maior Quantidade de Serviços

Identificamos os dias com maior oferta de serviços, considerando todas as fontes e operadores.

#### 3.2. Classes de Serviço Mais Utilizadas

Avaliamos as classes de serviço mais frequentes nos dados, ajudando a entender as preferências dos clientes.

#### 3.3. Menor Preço por Competidor e Dia da Semana

Comparamos os menores preços entre os operadores para cada dia da semana, oferecendo insights sobre a competitividade.

#### 3.4. Tendências Relevantes

Outras tendências, como relações entre ocupação e preço, foram observadas para auxiliar na tomada de decisão.

### 4. Geração de Visualizações

Foram criados gráficos para facilitar a compreensão dos dados:

1. **Dias com Maior Quantidade de Serviços**: Gráfico de barras mostrando a quantidade total de serviços por dia.
2. **Classes de Serviço Mais Utilizadas**: Gráfico de barras horizontais apresentando a frequência de cada classe de serviço.
3. **Menor Preço por Competidor e Dia da Semana**: Gráfico de barras agrupadas comparando os menores preços.

### 5. Geração do Arquivo Final

Os resultados foram salvos no arquivo `avaliacao_servicos.xlsx`, contendo as seguintes planilhas:

- **Consolidado**: Consolidação das informações.
- **Dias_Maior_Servico**: Dias com maior quantidade de serviços oferecidos.
- **Classes_Mais_Utilizadas**: Frequência das classes de serviço.
- **Menor_Preco_Competidor**: Comparativo de menores preços entre competidores por dia da semana.

## Tecnologias Utilizadas

- **Python**:
  - Biblioteca `pandas` para manipulação de dados.
  - Biblioteca `matplotlib` para visualizações gráficas.
- **Excel**:
  - Exportação de resultados usando `pandas.ExcelWriter`.

## Como Usar
1. Certifique-se de ter as dependências instaladas:
   ```bash
   pip install -r requirements.txt
   ```
2. Execute o script:
   ```bash
   python desafio_3_1/analise_viagens.py
   ```

## Conclusão

A consolidação e análise permitiram identificar padrões importantes nos serviços de transporte, oferecendo uma base para tomada de decisão com relação às operações e estratégias de precificação. Os gráficos e o arquivo gerado fornecem uma visão clara e acionável das informações coletadas.
