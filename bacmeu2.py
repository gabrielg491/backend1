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
tipo_sanguineo = cnx.cursor()

# Consulta
query = "select nome,idade  from aluno where tipo_sanguineo = b+;"



cursor.execute(query)

# Processar os resultados
tipo_sanguineo,nome,idaede = tipo_sanguineo.fetchall()

# Classificação dos alunos
for nome,idaede,tipo,sanguineo in aluno:
   print(nome,idaede)
# Fechando o cursor e a conexão
cursor.close()
cnx.close()
