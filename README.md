JSONPlaceholder API Automation Project

  Описание проекта:
	Автоматизированное тестирование REST API сервиса JSONPlaceholder
	Покрытие основных CRUD операций
	Валидация ответов API
	Генерация Allure отчётов
	Настроен CI/CD pipeline


  Технологический стек
	Python 3.10
	Pytest
	requests
	pydantic
	allure-pytest
	GitHub Actions


  Структура проекта
	- api/ — HTTP клиент и API endpoints
	- models/ — Pydantic модели
	- tests/ — автотесты (posts, users, comments)
	- utils/ — вспомогательные модули
	- pytest.ini — конфигурация pytest
	- requirements.txt — зависимости
	- .github/workflows/tests.yml — CI/CD pipeline
	- README.md — документация


  Установка
	1. Клонировать репозиторий
	2. Создать и активировать виртуальное окружение
	3. Установить зависимости из requirements.txt
  

Запуск тестов

  Запуск всех тестов: pytest
  Запуск с генерацией Allure результатов: pytest --alluredir=allure-results
  Просмотр Allure отчёта: allure serve allure-results

Примеры команд
	pytest tests/test_posts.py
	pytest tests/test_users.py
	pytest tests/test_comments.py
	allure serve allure-results

Allure отчёт
	Отображает шаги выполнения тестов
	Содержит HTTP request / response
	Показывает статус и severity тестов
	В README добавлены скриншоты Allure отчёта
  
CI/CD
	Реализован с помощью GitHub Actions
	Pipeline включает:
	установку зависимостей
	запуск pytest
	генерацию Allure results
	сохранение артефактов
	Триггеры:
	push в main / master
	•	pull request
	•	ручной запуск (workflow_dispatch)
	•	Используемая версия Python в CI:
	•	Python 3.10
