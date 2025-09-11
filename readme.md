# Report Read

Проект **Report Read** — сервис для отслеживания прочтения результатов отправки отчетов сотрудниками.

- Backend: FastAPI
- База данных: SQLite / Peewee
- Авторизация: JWT
- Схемы: Pydantic v2

---

## Функционал

1. **GET `/account/{year}/{month}/{user}/logo.png`**  
   - Анонимный доступ  
   - Кэширование через заголовки  
   - Сохраняет дату первого и последнего обращения  

2. **POST `/accounts/register`**  
   - Регистрация нового аккаунта  
   - Авторизация через admin JWT  
   - Параметры: `name`, `inn`, `secret_key`  

3. **GET `/stats`**  
   - Возвращает статистику по аккаунту за период  
   - JWT авторизация по аккаунту  

4. **GET `/healthcheck`**  
   - Проверка состояния сервиса  

---

## Примеры API

### Получение logo.png
curl -X GET "http://localhost:8000/<account_uuid>/<year>/<month>/<user_uuid>/logo.png"

### Регистрация аккаунта
curl -X POST "http://localhost:8000/accounts/register" \
     -H "Authorization: Bearer <admin_jwt>" \
     -H "Content-Type: application/json" \
     -d '{"name": "Test Corp", "inn": "1234567890", "secret_key": "abc123"}'

### Получение статистики
curl -X GET "http://localhost:8000/stats?start=2025-09-01&end=2025-09-30" \
     -H "Authorization: Bearer <account_jwt>"

### Healthcheck
curl http://localhost:8000/healthcheck

---

## Установка (локально)

1. Создать виртуальное окружение:
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows

2. Установить зависимости:
pip install -r requirements-dev.txt

3. Запустить приложение:
uvicorn main:app --reload --host 0.0.0.0 --port 8000

---

## Docker

Сборка контейнера:
docker build -t report_read .

Запуск контейнера:
docker run --rm -p 8000:8000 report_read

Запуск тестов в контейнере:
docker run --rm -v ${PWD}:/app -w /app report_read pytest tests

---

## Тестирование

pytest tests

---

## Pre-commit

Установить хуки:
pre-commit install
pre-commit run --all-files

---

## Лицензия

MIT License © 2025