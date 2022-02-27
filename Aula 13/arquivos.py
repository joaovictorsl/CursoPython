# Usando o módulo csv para escrever arquivos csv
import csv

with open('teste.csv', 'a', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(
        [['teste', 'oi', 'sal'], ['segunda', 'linha', 'para escrever']])
