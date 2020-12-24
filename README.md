# Backend Movies

Steps for start Backend application


1)Build and start django and PostgreSQL

    docker-compose up --build -d

2)For make Migrations of models

    docker exec -it backendmovies_web_1 python manage.py makemigrations

3)For migrate to database
     
    docker exec -it backendmovies_web_1 python manage.py migrate  


4)For create a super user, for access to admin of Django
 
    docker exec -it backendmovies_web_1 python manage.py createsuperuser

5)Complete form


---------------------------------
ENDPOINTS

GET:
http://0.0.0.0:8000/api/movies/

POST:
http://0.0.0.0:8000/api/movies/

PUT:
http://0.0.0.0:8000/api/movies/{id}/


BODY:
{

"title": string,

"description": string,

"duration": number,

"yearOfPublished": number

}
