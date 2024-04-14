# Hackaton ITLab

**[DRF](https://www.django-rest-framework.org/)**\
**[Django](https://www.djangoproject.com/)**

**Error: That port is already in use. In MACOS**
sudo lsof -t -i tcp:8000 | xargs kill -9

# Fixtures
Фикстуры на ходятся в папек **fixtures** в формате json.\
**Создание фикстур** происходит в shell, кроме user, так как там кодируется пароль.\
!Загрузка фикструр должна проводиться после создание db.

```./manage.py loaddata fixtures/'name_fixture.json'```

## Venv
**Создаем виртуальное окружение в искомой папке**, там где файл _.git_

```
python3 -m venv venv
```
**Активация venv**

В IDE можно выбрать в ручную созданный вами venv или исп. консоль.\
Для консоли:
```
Linux/MacOS : $ source venv/bin/activate
Window : $ venv\Scripts\activate
```

Обратите внимание на консоль -> после активации перед тестом строки ввода должна появится надпись `(venv)`. Это значит, что виртуальное окружение активно.

**Деактивация**
```
$ deactivate
```


## Установление библиотек

```
pip install -r requerements.txt
```
**!** Если просит обновить **pip** - обновите.

`./manage.py shell` - работа с Django через терминал.



## Команды для работы с Django  DRF

`python manage.py runserver` - запуск сервера\
`python manage.py migrate` - отвечает за применение и отмену миграции\
`python manage.py makemigrations` - обновляет/добавляет миграции при изменение моделей

`pip install djangorestframework`
```python
#settings.py
    REST_FRAMEWORK = {
        'DEFAULT_RENDERER_CLASSES': [
            'rest_framework.renderers.JSONRenderer',
        ],
        'DEFAULT_PARSER_CLASSES': [
            'rest_framework.parsers.JSONParser',
        ]
    }
```

## REACT

**[NPM](https://docs.npmjs.com/)**\
`npm install`\
`npm install vita`\
``

![alt text](<Screenshot 2024-04-08 at 21.52.15.png>)