# TriviaApp

## Instalación con Git
```
git clone https://github.com/jhernandez02/trivia-django.git
```
### Instalación dependiencias
```
pip install -r requirements.txt
```
### Levantar el proyecto
```
python manage.py runserver
```

## Usuarios de Prueba
| User    | Password |
|---------|----------|
| udemo01 | demo1234 |
| udemo02 | demo1234 |

## Descripción API

### Documentación
```
http://localhost:8000/docs/
```

### Login
> POST `/api/login/`
```
{
	"username": "udemo01@mail.com",
	"password": "demo1234"
}
```


### Crear una trivia
> POST `/api/trivias/`
```
{
    "name": "Trivia de Historia",
    "description": "Trivia sobre eventos históricos importantes",
    "questions": [1, 2, 3],
}
```

### Visualizar opciones de una trivia
> GET `/api/trivias/<id>/`


### Asignar Usuarios a una Trivia
> POST `/api/trivias/<id>/assign_users/`
```
{
    "user_ids": [1, 2, 3]
}
```

### Crear una participación
> POST `/api/participations/`
```
{
    "user": 1,
    "trivia": 1
}
```

### Enviar respuestas de una trivia
> POST `/api/participations/<id>/submit_answers/`
```
{
    "answers": [
        {"question_id": 1, "option_id": 3},
        {"question_id": 2, "option_id": 5}
    ]
}
```

### Ver el ranking de una trivia
> GET `/api/participations/ranking/?trivia_id=<id>`
```
{
	"answers": [
		{"question_id": 1, "option_id": 1},
		{"question_id": 2, "option_id": 5},
		{"question_id": 2, "option_id": 7}
	]
}
```
