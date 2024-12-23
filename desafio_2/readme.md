# Desafio 2

## Visão Geral
Este script é responsável por processar arquivos `.xlsx` presentes na pasta `raw`, filtrar e renomear colunas específicas, e então salvar os arquivos preparados na pasta `prep`, com um sufixo `_preparado` no nome.

---

## Estrutura das Pastas

### Pasta `raw`
A pasta `raw` deve conter os arquivos Excel (`.xlsx`) que precisam ser processados.

**Exemplo da estrutura da pasta `raw`:**

desafio_2/raw/
arquivo1.xlsx
arquivo2.xlsx
arquivo3.xlsx


### Pasta `prep`
A pasta `prep` é onde os arquivos preparados serão salvos. O script verifica se o arquivo já foi processado (verificando se já existe com o sufixo `_preparado`). Se o arquivo já existir, ele será ignorado, evitando duplicação de trabalho.

**Exemplo da estrutura da pasta `prep`:**


desafio_2/prep/
arquivo1_preparado.xlsx
arquivo2_preparado.xlsx

---

## Como Usar
1. Certifique-se de ter as dependências instaladas:
   ```bash
   pip install -r requirements.txt
   ```
2. Execute o script:
   ```bash
   python desafio_2/script_prep_buser.py
   ```
---

## Resultado
   O script irá:

   * Ler todos os arquivos `.xlsx` na pasta `raw`.
   * Para cada arquivo que ainda não foi processado (sem o sufixo `_preparado`), ele:
     * Filtra e renomeia as colunas.
     * Cria duas novas colunas: `Data_Partida` e `Hora_Partida` a partir de `Data_Hora_Partida`.
     * Salva o arquivo na pasta `prep` com o sufixo `_preparado` no nome.

   * Após a execução do script, os arquivos preparados estarão na pasta `prep`, com a estrutura de colunas reorganizada.
