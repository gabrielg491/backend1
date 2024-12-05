import mysql.connector

# Conexão com o banco de dados
cnx = mysql.connector.connect(
    user="exemploaulagb",
    password="Gb@32387506",
    host="aulaexemplogb.mysql.database.azure.com",
    port=3306,
    database="escola",  
    ssl_disabled=True     
)
# Criação do cursor
cursor = cnx.cursor()

# Consulta
query = "SELECT cpf,cpf_responsavel1,cpf_responsavel2 FROM escola.aluno;;"

cursor.execute(query)

# Processar os resultados
resultados = cursor.fetchall()

# Classificação dos alunos
for  CPF,cpf_reponasvel1, cpf_reponasvel2 in resultados:
    print(CPF,cpf_reponasvel1,cpf_reponasvel2)

        
        
      
  
# Fechando o cursor e a conexão
cursor.close()
cnx.close()
