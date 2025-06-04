<h1 align="center">✅ ToDo App (Django REST API)</h1>
<p align="center">
  Простое REST API-приложение для управления задачами (ToDo), созданное с использованием Django и Django REST Framework.
</p>

<p align="center">
  <img src="https://img.shields.io/github/languages/top/MuratOfficial/todo-django-rest?style=flat-square" />
  <img src="https://img.shields.io/github/license/MuratOfficial/todo-django-rest?style=flat-square" />
  <img src="https://img.shields.io/github/stars/MuratOfficial/todo-django-rest?style=flat-square" />
</p>

---

## 🚀 О проекте

**ToDo Django REST** — это минималистичный RESTful API-сервис для управления списком задач. Реализована базовая функциональность CRUD: создание, просмотр, обновление и удаление задач через API.

Отлично подходит в качестве обучающего проекта для знакомства с Django REST Framework.

---

## 🧰 Стек технологий

- **Язык**: Python 3  
- **Фреймворк**: Django  
- **REST API**: Django REST Framework  
- **База данных**: SQLite (по умолчанию)  
- **Управление окружением**: `pip`, `venv`, `requirements.txt`

---

## ⚙️ Функциональность

- ✅ Получение списка задач  
- ✅ Создание новой задачи  
- ✅ Обновление задачи  
- ✅ Удаление задачи  
- ✅ Отображение API-интерфейса через browsable DRF UI  
- ⏳ Возможности аутентификации (в будущем)

---

## 📦 Установка и запуск

```bash
# 1. Клонируйте репозиторий
git clone https://github.com/MuratOfficial/todo-django-rest.git
cd todo-django-rest

# 2. Создайте виртуальное окружение
python -m venv venv
source venv/bin/activate  # Для Windows: venv\Scripts\activate

# 3. Установите зависимости
pip install -r requirements.txt

# 4. Примените миграции
python manage.py migrate

# 5. Запустите сервер разработки
python manage.py runserver
```

**Теперь API будет доступен по адресу:**
```http
http://localhost:8000/api/
```

## 🧪 Примеры API-запросов

* GET `/api/tasks/` — Получить список задач
* POST `/api/tasks/` — Создать задачу
* GET `/api/tasks/<id>/` — Получить конкретную задачу
* PUT `/api/tasks/<id>/` — Обновить задачу
* DELETE `/api/tasks/<id>/` — Удалить задачу

Пример JSON-запроса на создание задачи:
```json
{
  "title": "Сделать домашку",
  "completed": false
}
```

## 📁 Структура проекта

```text
todo-django-rest/
├── manage.py
├── requirements.txt
├── todo/               # Основное Django-приложение
│   ├── admin.py
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   └── urls.py
├── todo_drf/           # Настройки проекта
│   ├── settings.py
│   └── urls.py
```

## 📌 Планы на будущее

* Авторизация пользователей (Token / JWT)
* Фильтрация и поиск задач
* Дата выполнения и приоритет
* Swagger или Redoc документация
* Интеграция с фронтендом (React / Vue / Svelte)

## 🤝 Вклад

Хочешь поучаствовать в развитии проекта? Добро пожаловать:
```bash
# Форкни репозиторий
# Создай новую ветку
git checkout -b feature/my-feature

# Внеси изменения и закоммить
git commit -m "Добавил новую фичу"

# Запушь изменения
git push origin feature/my-feature

# Создай Pull Request
```

<p align="center"><b>Сделано с ❤️ by <a href="https://github.com/MuratOfficial">MuratOfficial</a></b></p>
