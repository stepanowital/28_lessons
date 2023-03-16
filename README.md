# Урок 28
Для начала работы скопируйте репозиторий на локальную машину с помощью команды в терминале:

`https://github.com/skypro-008/lesson28-and-tests.git`

Откройте с клонированный репозиторий в PyCharm.

### Создайте виртуальное окружение:

#### Простой вариант:
Pycharm может предложить вам сделать это после того, как вы откроете папку с проектом.
В этом случае после открытия папки с проектом в PyCharm.
Появляется всплывающее окно, Creating virtual environment c тремя полями.
В первом поле выбираем размещение папки с виртуальным окружением, как правило, это папка venv
в корне проекта
Во втором поле выбираем устанавливаемый интерпретатор по умолчанию (можно оставить без изменений)
В 3 поле выбираем список зависимостей (должен быть выбран файл requirements.txt, 
находящийся в корне папки проекта)

#### Если этого не произошло, тогда следует выполнить следующие действия вручную:
#### Установка виртуального окружения:
1. Во вкладке File выберите пункт Settings
2. В открывшемся окне, с левой стороны найдите вкладку с именем
вашего репозитория (Project: lesson28-and-tests)
3. В выбранной вкладке откройте настройку Python Interpreter
4. В открывшейся настройке кликните на значок ⚙ (шестеренки) 
расположенный сверху справа и выберите опцию Add
5. В открывшемся окне слева выберите Virtualenv Environment, 
а справа выберите New Environment и нажмите ОК

#### Установка зависимостей:
Для этого можно воспользоваться графическим интерфейсом PyCharm,
который вам предложит сделать это как только вы откроете файл с заданием.

Или же вы можете сделать это вручную, выполнив следующую команду в терминале:
`pip install -r requirements.txt`

*У владельцев операционной системы MacOS могут возниктут сложности с установкой зависимостей.
Если возникла ошибка - сначала выполните в терминале команду brew install postgresql.
После её выполнения ошибок с установкой зависимостей быть не должно.
#### Настройка виртуального окружения завершена!
### Подготовка проекта django
После того как Вы установили все зависимости, необходимо подготовить django к работе:
для этого нам потребуется:

1. Иметь возможность запуска на локальной машине docker-контейнера 
(необходимо для запуска контейнера с базы данных):
- переходим в каталог `postgres_l28` и выполняем команду `docker-compose up`.

2. Выполнить необходимые команды для подготовки базы данных к работе:
Текущий проект уже содержит настроенную базу данных, но пока еще она 
пустая, не содержит таблиц, а всё её наполнение
находится в фикстурах (в django - файлы в формате json содержащие данные для наполнения БД).

Для начала нужно создать необходимые таблицы в базе данных с помощью команды:
python manage.py migrate (находясь в папке `my_project_part_1`)
а затем выполнить команду `python manage.py loadall` из этой же директории
   (для загрузки всех объектов в базу данных).
Уточним, что loadall является кастомной командой которая представляет
собой несколько идущих подряд команд
`python manage.py loaddata file.json` где file.json - файл с данными для БД
Если команда выполнена успешна вы увидите следующий текст:
```
Installed 2 object(s) from 1 fixture(s)
Installed 6 object(s) from 1 fixture(s)
Installed 3 object(s) from 1 fixture(s)
Installed 3 object(s) from 1 fixture(s)
Installed 3 object(s) from 1 fixture(s)
Installed 3 object(s) from 1 fixture(s)
Installed 1 object(s) from 1 fixture(s)
Installed 3 object(s) from 1 fixture(s)
Installed 3 object(s) from 1 fixture(s)
Installed 11 object(s) from 1 fixture(s)
```
После того как все подготовительные мероприятия выполнены - можно приступать к работе.

Первое, что необходимо сделать - изучить представленный проект.
Здесь одно Джанго-приложение соответствует одному заданию тренажера
ознакомится с адресами приложений можно всё также в файле `my_project/urls.py`
*Обратите внимание, что часть адресов, представленных в заданиях ниже уже реализованы
и здесь Вам требуется только дополнить их соответствующим образом.*


### Порядок выполнения заданий

## Часть 1. my_project_part_1

### Задание opinion ("Ваше мнение очень важно для нас")
Перейдите в файл tours/models.py и напишите модель в соответствии со спецификацией
указанной в TODO - комментариях

Для проверки запустите: `python manage.py test tours` из директории `my_project_part_1`
*Далее, для проверки других заданий просто измените название приложения
шаблон команды для запуска тестов `python manage.py test <app>`*


### Задание edits ("Снова правки")
Перейдите в файл edits/models.py и напишите модель в соответствии со спецификацией
указанной в TODO - комментариях.

### Задание discounts ("Скидочки")
Дана следующая документация
#### GET /discount/
```json
[
 {
     "id": 1,
     "tour": 1,
     "category": "promo",
     "discount": 10,
     "code": "SkyPro",
     "starts_at": "",
     "ends_at": ""
 }, 
   {
     "id": 2,
     "tour": 2,
     "category": "promo",
     "discount": 20,
     "code": "SkyPro2",
     "starts_at": "",
     "ends_at": ""
  }
]
```
#### GET /discount/1/
```json
{
   "id": 1,
   "tour": 1,
   "category": "promo",
   "discount": 10,
   "code": "SkyPro",
   "starts_at": "",
   "ends_at": ""
}
```
Внесите соответствующие изменения в модель Discounts приложения discounts,
а также напишите view-функции и настройте urls.py так,
чтобы возвращаемые данные соответствовали примерам, представленным выше.


### Задание along_neva_channels ("По каналам Невы")
Дана следующая документация:
#### GET /neva_tours/
```json
[
 {
     "id": 1,
     "name": "По каналам Невы",
     "starts_at": "",
     "ends_at": "",
     "points": [
        {"name": "Канал Грибоедова"},
        {"name": "Синий мост"}
     ]
 },
    {
     "id": 2,
     "name": "По каналам Невы",
     "starts_at": "",
     "ends_at": "",
     "points": [
        {"name": "Фонтанка 38"},
        {"name": "Красный мост"}
     ]
    }
]
```
 
#### GET /neva_tours/1/
```json
 {
     "id": 1,
     "name": "По каналам Невы",
     "starts_at": "",
     "ends_at": "",
     "points": [
        {"name": "Канал Грибоедова"},
        {"name": "Синий мост"}
     ]
 }
```
Внесите соответствующие изменения в модель Tour приложения along_neva_channels,
а также напишите view-функции и настройте urls.py так,
чтобы возвращаемые данные соответствовали примерам, представленным выше.


### Задание feedback ("Оставьте отзыв")
Ознакомьтесь с приложением feedback.
Используя знания из урока, напишите ручку для создания отзыва.
Ссылка на тур передается как число, и возвращаться должно то же число. Дата публикации не обрабатывается.
Попробуйте добавить новый отзыв с помощью `POST` запроса на адрес `/feedback/ `
```json
{
    "tour": 1,
    "author": "Я",
    "content": "Мне понравилось! Отличный тур",
    "rate": 4,
    "is_published": true
}
```

Если всё хорошо, Вы должны получить такой ответ:
```json
{
    "id": 1,
    "author": "test",
    "tour": 1,
    "content": "Мне понравилось! Отличный тур",
    "rate": 4,
    "published_at": null,
    "is_published": true
}
```
(Доступные ID можно подсмотреть в фикстурах ("`fixtures/feedback_tours.json", "fixtures/feedback_cities.json`"))

### Задание forgotten ("Что-то забыли?")
Ознакомьтесь с приложением forgotten
Используя знания из урока, напишите эндпоинт для редактирования комментария. 
Редактировать можно только текст (content) и рейтинг (rate).
А вот возвращать надо все поля. 
Тур, как и раньше, возвращается целым числом — id соответствующей модели.
Если вы выполнили команду `python manage.py loadall` то в этом приложении в базе уже имеется одно ревью, которое
можно попробовать отредактировать. Для редактирования мы будем использовать url `feedback-update/<pk:int>`


### Задание moderation ("Модерация")
Ознакомьтесь с приложением moderation
Используя знания из урока, напишите эндпоинт, который удаляет отзыв.
Для удаления используйте, пожалуйста, url `feedback-delete/<pk:int>`
Для практики в базу данных залито 11 объектов (значения id с 1 по 11)
Если для экспериментов этого будет недостаточно - пополните базу с помощью команды
`python manage.py loadall`


## Часть 2
Перед тем как приступить к заданиям не забудьте подготовить Джанго-проект к работе.

### Задание new_horizonts ("Новые горизонты")
Перейдите в файл views приложения new_horizonts во второй части тренажера.
Перед вами код view, который создает новые города или возвращает уже созданные. 
Перепишите его с использованием коротких функций из урока.

### Задание reforms ("Реформы")
Перейдтие в файл views приложения reforms.
Напишите эндпоинт, который при post-запросе на адрес /city/
обновляет описание города или создает новый по переданному ей названию.
Например запрос:
```json
{
    "city": "Санкт-Петербург",
    "description": "Санкт-Петербург - Северная Венеция" 
}
```
Обновит в БД информацию об описании Санкт-Петербурга,
а если в поле name передать город, которого нет в БД
тогда должна быть создана новая строка с названием этого города и его описанием.

### Задание alphabet ("Алфавит")
Перейдите в приложение alphabet.
Напишите СBV для выдачи списка городов.
Также измените модель городов так, чтобы по умолчанию 
города всегда были отсортированы в алфавитном порядке.

### Задание opened_first ("Сначала открытые")
Перейдите в приложение opened_first
Используя метод order_by, выведите CityListView сначала все города со статусом “open”, 
а потом — “closed”. При этом сами названия городов должны быть отсортированы в алфавитном порядке.
Например:
```json
[
  {
    "id": 1, 
    "name": "Абакан",
    "status": "open"
  },
  {
    "id": 3, 
    "name": "Ялта", 
    "status": "open"
  },
  {
    "id": 4,
    "name": "Казань",
    "status": "closed"
  },
  {
    "id": 2,
    "name": "Москва",
    "status": "closed"
  }
]
```

### Задание pages ("Странички")
Перейдите в приложение pages.
Добавьте в список городов пагинацию. Должен получиться примерно следующий ответ:
Максимальный размер одной страницы должен содержать не более 5 объектов.
Также убедитесь, что страницу можно открыть по её номеру. 
Например, вторая страница открывается по ссылке /pages/?page=2
```json
{
    "total": 20, 	
    "num_pages": 4, 
    "items": [ 			
        { 					
            "id": 1, 	
            "name": "Казань",
            "status": "open"
        },
        { 					
            "id": 2, 	
            "name": "Москва",
            "status": "open"
        }
    ]
} 
```
### Задание counting_rhyme ("Считалочка")
Создайте view, которая выведет общее количество городов и пользователей на сайте.
Ответ должен выглядеть следующим образом:
```json
{
   "cities": 20, 
   "users": 60
}
```
### Задание users_geography ("География пользователей")
Перейдите в приложение users_geography.
Выведите JSON со списком, в котором для каждого города будут следующие поля: 
id — id города;
name — название города;
status — статус города;
users — количество жителей в городе (сколько записей из модели User ссылается на этот город);
users_percent — процентное соотношение жителей города (предыдущее значение поделить на общее количество записей в модели User).

Переходите к запуску тестов только после выполнения всех заданий.
Для запуска тестов воспользуйтесь командой `python3 manage.py test` (находясь в папке `my_project_part_1`)
Также вы можете проверить правильность работы приложения - для этого используйте команду
`python3 manage.py test <app>`
