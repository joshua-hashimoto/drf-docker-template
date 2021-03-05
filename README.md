# django-docker-template

## docker-compose.yml

```yml
version: "3"

services: 
    web:
        build: .
        command: gunicorn core.wsgi -b 0.0.0.0:8000 # gunicorn対応
        environment: 
            APPLICATION_NAME: django-docker-template
            ENVIRONMENT: development
            SECRET_KEY:
            DEBUG: 1
        volumes: 
            - .:/app
        ports: 
            - 8000:8000
        depends_on:
            - db
    db:
        image: postgres:11
        volumes:
            - postgres_data:/var/lib/postgresql/data/
        environment:
            - "POSTGRES_HOST_AUTH_METHOD=trust"

volumes:
    postgres_data:
```
