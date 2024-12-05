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
query = "select nome,endereco from aluno;"



cursor.execute(query)

# Processar os resultados
resultados = cursor.fetchall()

# Classificação dos alunos
for nome, inderco in resultados:
  print(nome,inderco)
# Fechando o cursor e a conexão
cursor.close()
cnx.close()
