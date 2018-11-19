# Weather
## Start project

1. Install requremints:
  * pip install -r requirements.txt  
2. Create DB:
  * python manage.py migrate


### Оценка времени выполнения

| # | Этап  | Описание | Min | Max | Real | 
|---|-----|-----------|-----|-----|-----|
|1 |Настройка проекта|Подготовка окружение, установка зависимостей| 0.5 | 1 | 0.5 |
|2 |Построение архитектуры БД| Проектирование и описание моделей и их зависимостей| 1 | 2 | 1 |
|3 |Авторизация| | 2 | 4 | 1 |
|4 |Реализация страницы с функционалом|Написание views, templates, urls. Отображение таблицы с данными из БД. | 6 | 12 |
|5 |Скрипт|Написание скрипта для запуска обновления данных| 1| 3 |
|6 |Celery|Настройка Celery, для автоматического запуска всех тасков |2| 4 |