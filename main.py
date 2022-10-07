import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='Yindi1',
    database='bdyindi',
)

#Cria a conexão ele tbm irá executar os comandos da conexão
cursor = conexao.cursor()

#Dados:
'''nome_produto = 'tenis Adidas'
valor = '650'''

# CRUD
#CREATE - Inserir informação na tabela
def InsereDados(nome_produto, valor):
    comando = f'INSERT INTO vendas(nome_produto, valor) VALUES ("{nome_produto}", {valor})' #escreve o comando
    cursor.execute(comando) #mando o comando ser executado 
    conexao.commit() #edita o banco de dados    
#InsereDados("prancha de surf DMS", 400)

#READ - Ler informções de uma tabela
def LeDados(vendas): #vendas é o nome da tabela q desejo ler.
    comando = f'SELECT * FROM vendas' #escreve o comando
    cursor.execute(comando) # executa o comando   
    resultado = cursor.fetchall() #armazena o resultado do comando q nesse caso é de leitura do banco
    print(resultado)
#LeDados("vendas")

#UPDATE - Editar o banco de dados
def AtualizaDados(nome_produto, valor):
    comando = f'UPDATE vendas SET valor={valor} WHERE nome_produto="{nome_produto}"'
    cursor.execute(comando)
    conexao.commit()   
#AtualizaDados("prancha de surf DMS", 450)

#DELETE - Exclui um dado de uma tabela (exclui repetidos também)
def DeletaDados(tabela, nome_produto):
    comando = f'DELETE FROM {tabela} WHERE nome_produto="{nome_produto}"' #Deleta produto pelo nome. Pode criar outras condições
    cursor.execute(comando)
    conexao.commit()   
#DeletaDados("vendas", "prancha de surf DMS")

#A conexão e o cursor devem ser fechados ao final da aplicação
cursor.close()
conexao.close() 