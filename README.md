# Backend Movies

Steps for start Backend application



1)Build and start django and PostgreSQL

    docker-compose up --build -d


In case where you have an issue for running the next steps, you need verify the correct name of the container where is running django. And for this you can see the name of your container where you have running django, with the next steps.

A) List containers
 
        docker ps
 
 And with this, you need see for the image backend_web which is the name for your local env. In my case (backend_web_1).  if you have other name, you need replace this where we will be using in the next steps.

2)For make Migrations of models

    docker exec -it backend_web_1 python manage.py makemigrations

3)For migrate to database
     
    docker exec -it backend_web_1 python manage.py migrate  


4)For create a super user, for access to admin of Django
 
    docker exec -it backend_web_1 python manage.py createsuperuser

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
