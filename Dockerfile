# Stage 1: Build
FROM python:3.11-alpine AS builder
WORKDIR /app

# Установка зависимостей сборки
RUN apk add --no-cache build-base libffi-dev

# Копируем зависимости
COPY requirements.txt .
RUN pip install --prefix=/install -r requirements.txt

# Stage 2: Runtime
FROM python:3.11-alpine
WORKDIR /app

# Копируем установленные пакеты из builder
COPY --from=builder /install /usr/local

# Копируем исходники
COPY . .

# expose port
EXPOSE 8000

# Команда запуска
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
