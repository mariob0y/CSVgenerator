# Fake Data CSV Generator (Django, Celery)
Web generator of CSV files with fake data

## Demo

Live demo of project you may check here - https://csvfaker.herokuapp.com/

Login: test  
Password: test    



## Description

Online service for generating CSV files with fake (dummy)
data, developed with Python and Django.   


App lets you create .CSV file with data of choice. You may choose type of data, text of headers, order of columns and number of rows.   
This scheme may be later generated into .CSV file and downloaded.  

Task of file generation is handled via Celery, and code of task is stored at ```dummy_gen/tasks.py```.

## Built with
[Django](https://www.djangoproject.com/) - The web framework used  
[Celery](https://docs.celeryproject.org/en/stable/django/first-steps-with-django.html) - Distributing of tasks  
[Heroku Redis](https://elements.heroku.com/addons/heroku-redis) - Brocker  
[Faker](https://faker.readthedocs.io/en/master/) - Generator of data for .CSV files  
[Celery progress](https://github.com/czue/celery-progress) and [Django celery results](https://github.com/celery/django-celery-results)- for task progress tracking and task results storing, respectively  
[AWS S3](https://devcenter.heroku.com/articles/s3) - Storing generated .CSV files  
[Whitenoise](http://whitenoise.evans.io/en/stable/django.html) - Static files management  
[ElaAdmin Template](https://github.com/puikinsh/ElaAdmin) - Bootstrap template  


## Running locally
Please note, that this repo is configured for Heroku deploy.

To run project locally, you would need to perform following steps:
1. Pull repo. 
2. In ```settings.py```, change following configurations:
 * Change ```CELERY_BROKER_URL``` to your Redis, or delete this line if you are using RabbitMQ
 * Remove or comment lines:
 
 ```
 # AWS S3 SETTINGS
# AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
# AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
# AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
# AWS_URL = os.environ.get('AWS_URL')
# AWS_DEFAULT_ACL = None
# AWS_S3_SIGNATURE_VERSION = 's3v4'

# AWS_QUERYSTRING_AUTH = True
# AWS_S3_REGION_NAME = 'eu-central-1'
# AWS_S3_ADDRESSING_STYLE = "virtual"

# MEDIA_URL = AWS_URL + '/media/'
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

# django_heroku.settings(locals())

# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'static'),
# )
```
2. In a root folder (one where ```manage.py``` located) run commands:  
```
pip3 install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python createsuperuser
python manage.py runserver
```
3. Brocker server: 
 *  If you are using Redis, start worker (command for Windows below, run in root folder):  
    ``` celery -A planeks.celery worker -l --loglevel=info ```  
     - In case of trouble, check [this guide](https://youtu.be/BbPswIqn2VI)  
 * If you are using RabbitMQ, make sure that it's running on your machine.  
     - In case of trouble, check [this guide](https://youtu.be/fBfzE0yk97k)
     
4. Saving .CSV files:
 * To save .CSV files locally, ```open dummy_gen/tasks.py```
   - Comment section at lines 84-91 
   - Write where files should be saved on disk at line 42
