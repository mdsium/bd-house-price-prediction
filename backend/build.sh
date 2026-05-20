#!/usr/bin/env bash

pip install -r requirements.txt
python manage.py migrate

python manage.py shell << END
from django.contrib.auth import get_user_model

User = get_user_model()

if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser(
        'admin',
        'admin@gmail.com',
        '1234'
    )
END