# Recipes App

Веб-сайт с рецептами блюд, созданный для того, чтобы больше не хранить рецепты в скриншотах и избранных сообщениях.

## Технологии
- **Python 3.14**
- **Django**
- **PostgreSQL**
- **Docker & Docker Compose**
- **Bootstrap 5**

## Как запустить локально

1. **Клонируйте репозиторий:**
   ```bash
   git clone <ссылка_на_ваш_репозиторий>
   cd <папка_проекта>
   ```

2. **Создайте файл `.env` в корне проекта и заполните его:**
   ```env
    DJANGO_SECRET_KEY=your_secret
    
    DB_ENGINE=django.db.backends.postgresql
    DB_NAME=recipes
    DB_USER=postgres
    DB_PASSWORD=your_password
    DB_HOST=db
    DB_PORT=5432
   ```

3. **Запустите проект через Docker Compose:**
   ```bash
   docker-compose up -d --build
   ```

4. **Cоздайте администратора:**
   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```

## Доступ к приложению
- **Сайт доступен по адресу:** [http://localhost:9090](http://localhost:9090)
- **Админ-панель:** [http://localhost:9090/admin/](http://localhost:9090/admin/)
