Desenvolvido por Weslei Santos de Jesus 
## Subindo o projeto

# O projeto é multplataforma porém partimos do principio que iremos sempre executar uma API em um servidor Linux seja em algum cloud ou local, lembrando que vamos virtualizar com a ajuda do Docker.

python3 -m venv venv  
source venv/bin/activate

Se for Windows python -m venv venv   
python -m venv venv  
venv\Scripts\activate


# Ambiente ativado vamos as dependencias
``` 
Se não tem o docker instalado essas são as versões usadas no desenvolvimento:

Docker Compose version v2.10.2
Docker version 20.10.17, build 100c701

https://docs.docker.com/engine/install/ubuntu/
``` 

# Subindo o Docker

``` 
docker-compose up
Ou se preferir docker-compose up --build 
``` 

# Os containers iram subir e instalar todas as dependencias

## Para aplicar as migrations no banco de dados

``` 
docker-compose exec web python3 manage.py migrate 
``` 
## Para criar um super usuario

``` 
docker-compose exec web python3 manage.py createsuperuse
``` 
Depois disso so testar a API

# Testes 

docker-compose exec web python3 manage.py test
