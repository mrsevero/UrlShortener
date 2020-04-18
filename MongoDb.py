from pymongo import MongoClient

## Iniciar conexão com o banco de dados
client = MongoClient("localhost", 27017)

##bancos de dados disponiveis
##print(client.list_database_names())

## cria base de dados
db = client.database_urls


## Inserir varios dados e criando documento urls
db.urls.insert_many(
    [
        {"id":"1","url":"google.com"}
    ]
)
## Inserir apenas um dado/linha
db.urls.insert_one({"id":"2","url":"youtube.com"})

## Selecionar um dado especifico


