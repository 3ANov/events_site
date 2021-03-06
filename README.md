### Проект “Афиша” (Тестовое задание):

Для запуска проекта:  
**python manage.py runserver** - backend  
**npm run serve** - frontend

Использованы:  
* backend: **Django, Django REST framework** 
* frontend: **Vue.js**

#### ОПИСАНИЕ ЗАДАНИЯ
Стоит задача создать web-приложение “Афиша” на **Django** с хранением данных в БД 
**PostgreSQL**. 
 
1. Используя Django ORM, создайте следующую схему:

    Сервис хранит список событий(например, туры, концерты, выставки, и т.д.). 
    Каждое событие имеет список “инстансов” имеющих дату начала/конца и место проведения.
   
    Например:  
     * Событие: тур группы Metallica  
         * Инстансы:  
             ● Air Canada Center, Toronto, 2015-09-15 19:00  
             ● Scotiabank Saddledome, Calgary, 2015-09-20 20:00  
    * Место проведения имеет следующие аттрибуты:  
          ● Название  
          ● Город  
          ● Координаты(используется для geo запросов)  
   
    * Event имеет следующие аттрибуты:  
          ● Название  
          ● Опасание  
          ● Список “Категорий”  
          ● Список “Инстансов”  
         
 
2. Используя django-rest-framework создайте следующие ресурсы:
 
 
`GET /api/events?page=1&per_page=10&category=3` (Список событий отфильтрованный по категориям)    
`GET /api/events/geosearch?lat=&long=&radius=&page=1&per_page=10` (Список событий которые будут проведены в местах, которые расположены не дальше от указанной точки)  

```JSON
{ 
  "pagination": { 
    "has_next": true, 
    "has_prev": false 
  }, 
  "data": [ 
    { 
      "id": 123, 
      "title": "Metallica Tour", 
      "description": "Some description" 
    }, 
    ... 
  ] 
} 
```
 
`GET /api/events/123` (Детальная информация о событии) 
```JSON
{ 
  "id": 123, 
  "title": "Metallica Tour", 
  "desctription": "Some description", 
  "instances": [ 
    {
      "start": "2015-09-15 19:00", 
      "end": "", 
      "place": {
        "id": 1, 
        "name": "Air Canada Center", 
        "lat": 43.643466, 
        "long": 79.379099, 
        "city": { 
          "id": 1, 
          "Name": "Toronto"
        } 
      } 
    }, 
    ... 
  ] 
} 
```

`POST /api/events` (Создать новый объект из JSON'а и вернуть созданый объект с деталями, или вернуть ошибку 400 со списком ошибок валидации)   
`PUT /api/events/123`        (Изменить объект с id=123 из JSON'а и вернуть обновлённый объект с деталями, или вернуть ошибку 400 со списком ошибок валидации) 
 
3. Используя любой javascript фреймворк, создать приложение для
отображения списка событий с pagination’ом, при клике на event отобразить
детали event’а со списком инстансов:
    ![](/docs/example.png)

