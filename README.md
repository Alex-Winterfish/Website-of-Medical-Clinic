# Cайт компании медицинской диагностики

Серверная часть выполнена с помощью вреймворка Django.
Пользовательская часть выполнена с помощью Bootstap.
В качестве базы данный используется Postgres

1. ## Структура проекта


```markdown
Website-of-Medical-Clinic/ 
├───.github
│   └───workflows
├───clinic
│   ├───management
│   │   ├───commands
|   |   |   ├──__init__.py 
|   |   |   ├──add_services.py
|   |   |   └──add_staff.py
|   |   └──__init__.py
│   ├───migrations
│   ├───templates
│   │   └───clinic
│   ├───tests
|   |   ├──__init__.py 
|   |   ├──test_appointment.py 
|   |   ├──test_results.py
|   |   ├──test_service.py
|   |   ├──test_staff.py
|   |   └──test_templates.py
│   ├───urls
|   |   ├──__init__.py 
|   |   ├──urls_appointment.py 
|   |   ├──urls_results.py
|   |   ├──urls_service.py
|   |   ├──urls_staff.py
|   |   └──urls_templates.py
│   ├───views
|   |   ├──__init__.py 
|   |   ├──appointment_views.py 
|   |   ├──results_views.py
|   |   ├──service_views.py
|   |   ├──staff_views.py
|   |   └──templates_view.py
|   ├──__init__.py 
|   ├──admin.py
|   ├──apps.py
|   ├──forms.py
|   └──models.py
|
├───config
├───media
├───nginx
├───static
├───staticfiles
|
├───users
│   ├───management
│   │   ├───commands
|   |   |   ├──__init__.py 
|   |   |   ├──add_group.py
|   |   |   └──add_users.py
|   |   └──__init__.py
│   ├───migrations
│   ├───templates
│   |   └───users
|   ├──__init__.py 
|   ├──admin.py 
|   ├──apps.py
|   ├──forms.py
|   ├──models.py
|   ├──tests.py
|   ├──urls.py
|   ├──validators.py
|   └──views.py
└───venv

```
Приложение clinic содержит следующие модели:

1.  #### MedStaffModel для создания медицинского специалиста.
    Поля модели:
 - name - Ф.И.О медицинского специалиста
 - title - должность. Вариаты: MD - врач, NURSE - медсетсра
 - speciality - специальность. Варианты:
         (GYNECOLOGIST, "гинеколог"),
         (CARDIOLOGIST, "кардиолог"),
         (NEUROSURGEON, "нейрохирург"),
         (NEUROLOGIST, "невролог"),
         (ENDOCRINOLOGIST, "эндокринолог"),
         (THERAPIST, "терапевт"),
         (ONCOLOGIST, "онколог"),
         (RHEUMATOLOGIST, "ревматолог"),
         (PHLEBOLOGIST, "флеболог"),
         (MAMMOLOG, "мамолог"),
         (RADIOLOGIST, "рентгенолог"),
 - photo - фотография специалиста

2. ### MedServiceModel для создания медицинской услуги.
    Поля модели:
 - name - название медицинской услуги
 - description - описание медицинской услуги
 - price - стоимость медицинской услуги
 - photo - иллюстрация медицинской услуги
 - med_spec - медицинский специалист. Внешний ключ на модель MedStaffModel.

3. ### AppointmentModel для создания назначения на медицинскую услуги.
    Поля модели:
 - ap_date - назначенная дата
 - ap_time - назначенное время
 - med_serv - медицинская услуга. Внешний ключ на модель MedSrviceModel
 - patient - пациент. Внешний ключ на модель CustomUser.

4. ### ResultModel для создания результатов медицинской услуги.
    Поля модели:
 - result_date - дата готовности результатов
 - appointment - назначение на медицинскую услугу. Внешний ключ на модель AppointmentModel.
 - result - текстовое поле, эпикриз.
 - patient - пациент. Внешний ключ на модель CustomUser.

Приложение Users содержит следующие модели:

1. ### CustomUser для создания пользователя.
    Поля модели:
 - last_name - Фамилия пользователя
 - first_name - Иля пользователя
 - patronymic - Отчество пользователя
 - email - Электронная почта пользователя
 - phone - Телефон пользователя
 - country - Страна 

2. ### FeedBackModel для сохранения замечаний пользователя
    Поля модели:
 - theme - тема отзыва
 - feed_back - текст отзыва
 - email - электронная почта для связи

3. ### ContentModel для сохранения информации о компании. Контент для отображения на сайте.
    Поле модели:
 - company - название компании
 - about - информация о компании
 - email - электронная почта компании 
 - history - история компании
 - values - ценности и миссия компании
 - address - адрес компании
 - map_address - карта проезда. iframe со ссылкой на карту

2. ## Запуск проекта.

Указать переменные окружения в файл .env. Примеры указаны в файле .env.sample в корне проекта.

Установить зависимости:
```commandline
pip install -r requirements.txt
```

Для контейниризации проекта в корне находяться файлы:
docker-compose.yml - для запуска на удаленном сервере
docker-compose.local.yml - для запуска проекта локально

Для локального запуска проекта выполнить команду:
```commandline
docker-compose -f docker-compose.local.yml up -d --build
```

При запуске сервиса clinic в базу данных добавляются экземпляр модели ContentModel, примеры модели
MedStaffModel и MedServiceModel.

Также добавляются пользователи:
 
 - user_1@mail.com пароль 12345
 - user_2mail.com пароль 12345
 - moder_1@mail.com пароль 12345 - пользователь с правами администратора

3. ## Тестирование

Результаты тестирования можно посмотреть, выполнив команду:
```commandline
coverage report
```
Покрытие тестами 87
Name                                     Stmts   Miss  Cover
------------------------------------------------------------
clinic\__init__.py                           0      0   100%
clinic\admin.py                             22      0   100%
clinic\apps.py                               4      0   100%
clinic\forms.py                             14      0   100%
clinic\management\__init__.py                0      0   100%
clinic\management\commands\__init__.py       0      0   100%
clinic\migrations\0001_initial.py            5      0   100%
clinic\migrations\0002_initial.py            7      0   100%
clinic\migrations\__init__.py                0      0   100%
clinic\models.py                            59      6    90%
clinic\tests\__init__.py                     0      0   100%
clinic\tests\test_appointments.py           37      0   100%
clinic\tests\test_results.py                35      0   100%
clinic\tests\test_services.py               25      0   100%
clinic\tests\test_staff.py                  21      0   100%
clinic\tests\test_templates.py               0      0   100%
clinic\urls\__init__.py                      0      0   100%
clinic\urls\urls_appointment.py              6      0   100%
clinic\urls\urls_results.py                  6      0   100%
clinic\urls\urls_services.py                 6      0   100%
clinic\urls\urls_staff.py                    6      0   100%
clinic\urls\urls_templates.py                5      0   100%
clinic\views\__init__.py                     0      0   100%
clinic\views\appointment_views.py           31      8    74%
clinic\views\result_views.py                47     14    70%
clinic\views\service_views.py               11      0   100%
clinic\views\staff_views.py                 16      0   100%
clinic\views\templates_views.py             35     15    57%
config\__init__.py                           0      0   100%
config\settings.py                          32      0   100%
config\urls.py                               7      1    86%
manage.py                                   11      2    82%
users\__init__.py                            0      0   100%
users\admin.py                              17      0   100%
users\apps.py                                4      0   100%
users\forms.py                              29     13    55%
users\management\__init__.py                 0      0   100%
users\management\commands\__init__.py        0      0   100%
users\migrations\0001_initial.py             8      0   100%
users\migrations\0002_contentmodel.py        5      0   100%
users\migrations\__init__.py                 0      0   100%
users\models.py                             40      3    92%
users\tests.py                               0      0   100%
users\urls.py                                6      0   100%
users\validators.py                          6      3    50%
users\views.py                              42     14    67%
------------------------------------------------------------
TOTAL                                      605     79    87%
