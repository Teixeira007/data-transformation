# Extração de Dados de Tabela PDF, Conversão para CSV e Compactação em ZIP

Este script Python foi desenvolvido para extrair dados da tabela "Rol de Procedimentos e Eventos em Saúde" presente no PDF do Anexo I. Ele realiza a extração de todas as páginas, ele substitui as abreviações das colunas OD e AMB pelas descrições completas, salva os dados em um arquivo CSV, e, em seguida, compacta o CSV em um arquivo ZIP.

## Requisitos
 - Python 3.x
 - Bibliotecas Python: tabula-py, pandas
 
Você pode instalar as bibliotecas necessárias utilizando o seguinte comando:
```bash
pip install tabula-py pandas
```
## Como Usar
1. Clone o repositório ou faça o download do script Python.
   ```bash
   https://github.com/Teixeira007/data-transformation.git
   ```
2. Execute o script Python.
   ```python
   python dataTransformation.py
   ```
   O script realizará a extração das tabelas do arquivo PDF, renomeará as colunas conforme especificado, salvará os dados em um arquivo CSV chamado "AnexoI.csv" e, finalmente, compactará o CSV em um arquivo ZIP chamado "Teste_{seu_nome}.zip".

## Estrutura do Código
### Bibliotecas Utilizadas

```python
import tabula
import pandas as pd
import zipfile
import os
```
### Função para Zipar o Arquivo
```python
def create_zip(filename, name_file_csv):
    with zipfile.ZipFile(filename, "w") as zip_file:
        zip_file.write(name_file_csv, arcname=os.path.basename(name_file_csv))
```
Esta função cria um arquivo ZIP (Teste_{seu_nome}.zip) contendo o arquivo CSV gerado.
### Extração de Tabelas do PDF e Conversão para CSV
```python
# Extraindo todas as tabelas do arquivo AnexoI
tables = tabula.read_pdf("AnexoI.pdf", pages='all', lattice=True)

# Juntando todas as tabelas em uma só
combined_table = pd.concat(tables, ignore_index=True)

# Renomeando as colunas OD e AMD para suas descrições completas
final_table = combined_table.rename(columns={'OD': 'Seg. Odontológica', 'AMB': 'Seg. Ambulatorio'})

# Salvando a tabela em formato CSV
final_table.to_csv("AnexoI.csv", index=False)
```
Este trecho de código realiza a extração de todas as tabelas do arquivo PDF, junta-as em uma tabela única, renomeia as colunas conforme necessário e, por fim, salva os dados em um arquivo CSV chamado "AnexoI.csv".
### Chamada da Função de Zipagem
```python
# Nome do arquivo CSV
name_file_csv = 'AnexoI.csv'
# Nome do arquivo ZIP
filename = "Teste_Vinicius_Teixeira.zip"

# Chamando a função que vai realizar a zipagem
create_zip(filename, name_file_csv)
```
Estas linhas de código definem o nome do arquivo CSV gerado e o nome do arquivo ZIP a ser criado. Em seguida, chamam a função create_zip para realizar a zipagem.
## Observações
 - Certifique-se de que o arquivo PDF do Anexo I está na mesma pasta do script para garantir uma execução adequada.
 - Os dados extraídos da tabela incluem todas as páginas do PDF.






