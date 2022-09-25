#!/bin/bash

./wait-for-it.sh skeat-db:5432

if [ $? -ne 0 ] ; then
   echo db not started, aborting
   exit
fi

python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
