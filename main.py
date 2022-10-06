import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Yindi1',
    database='bdyindi',
)

#Cria a conexão ele tbm irá executar os comandos da conexão
cursor = conexao.cursor()

# CRUD
#CREATE
comando = '' #escreve o comando
cursor.execute(comando) #mando o comando ser executado
conexao.commit() #edita o banco de dados
resultado = cursor.fetchall() #armazena o resultado do comando q nesse caso é de leitura do banco


#A conexão e o cursor devem ser fechados ao final da aplicação
cursor.close()
conexao.close() 