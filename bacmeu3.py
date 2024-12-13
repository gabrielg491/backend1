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
query = "SELECT nome,naturalidade,sexo  FROM aluno;"

cursor.execute(query)

# Processar os resultados
resultados = cursor.fetchall()

# Classificação dos alunos
for nome,sexo,naturalida in resultados:
    if sexo =="M" and naturalida == "rio de janeiro" and sexo:
        print(f"o aluno {nome} é sua naturalidade é {naturalida} e o seu sexo é {sexo}")

for nome,sexo,naturalida in resultados:
    if sexo =="F" and naturalida == "são paulo" and sexo:
        print(f"a aluna {nome} é sua naturalidade é {naturalida} e seu sexo é {sexo} ")         
        
      
  
# Fechando o cursor e a conexão
cnx.commit()       
cursor.close()
cnx.close()
