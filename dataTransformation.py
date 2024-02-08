import tabula
import pandas as pd
import zipfile
import os

#Função para zipar o arquivo
def create_zip(filename, name_file_csv):
    with zipfile.ZipFile(filename, "w") as zip_file:
        zip_file.write(name_file_csv, arcname=os.path.basename(name_file_csv))

#Extraindo todas as tabelas do arquivo AnexoI
tables = tabula.read_pdf("AnexoI.pdf", pages='all', lattice=True)

#Juntando todas as tabelas em uma só
combined_table = pd.concat(tables, ignore_index=True)

#Renomeando as colunas OD e AMD para sua descrição completa
final_table = combined_table.rename(columns={'OD': 'Seg. Odontológica', 'AMB': 'Seg. Ambulatorio'})

#Salvando a tabela em formtato csv
final_table.to_csv("AnexoI.csv", index=False)

#nome do arquivo csv
name_file_csv = 'AnexoI.csv'
#nome do arquivo zipado
filename = "Teste_Vinicius_Teixeira.zip"

#chamando função que vai realizar a zipagem
create_zip(filename, name_file_csv)