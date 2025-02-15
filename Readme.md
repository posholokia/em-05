# Практическая работа по 5 теме.
ТЗ: https://docs.google.com/document/d/1LckPIpHA-NONmRmZSRzbMITcT63Y520p2XO8-DEZK2I/edit?tab=t.0

## Подготовка к запуску.
1. Запустить парсер из проекта https://github.com/posholokia/ef-m2/tree/async-version

2. Подготовить переменные окружения:
 - в корне проекта создать файл `.env` с содержимым по примеру из `.env.example`. 
Данные для подключения к БД должны быть из БД с данными парсера.

## Запуск проекта
### Локально
Установка зависимостей:
```
pip install poetry
poetry install --no-cache --no-root
```

Запуск:
`python src/main.py`

### В докере
Запуск: 
`docker compose up -d --build`

Остановка: `docker compose down`
