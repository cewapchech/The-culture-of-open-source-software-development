# Переменные окружения (Stateless подход)
VENV = .venv
PYTHON = $(VENV)/bin/python
PIP = $(VENV)/bin/pip
MYPY = $(VENV)/bin/mypy
RUFF = $(VENV)/bin/ruff

# Объявление фиктивных целей (чтобы Make не искал файлы с такими именами)
.PHONY: all venv install run typecheck lint format check-requirements check clean

# Цель по умолчанию (запускается при вводе просто 'make')
all: venv install check

# Управление окружением
venv:
	@echo "Создание виртуального окружения..."
	python3 -m venv $(VENV)

install: venv
	@echo "Установка зависимостей..."
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

# Запуск проекта
run: install
	@echo "Запуск приложения..."
	$(PYTHON) src/app.py

# Проверка качества кода
typecheck: install
	@echo "Проверка типов (mypy)..."
	$(MYPY) src/

lint: install
	@echo "Проверка стиля кода (ruff check)..."
	$(RUFF) check src/

format: install
	@echo "Форматирование кода (ruff format)..."
	$(RUFF) format src/

check-requirements: install
	@echo "Проверка соответствия импортов и зависимостей..."
	$(PYTHON) scripts/check_deps.py

# Цепочки (Композиция действий)
check: typecheck lint check-requirements
	@echo "Все проверки успешно пройдены!"

# Очистка
clean:
	@echo "Очистка кэшей и временных файлов..."
	rm -rf $(VENV)
	find . -type d -name "__pycache__" -exec rm -r {} +
	find . -type d -name ".mypy_cache" -exec rm -r {} +
	find . -type d -name ".ruff_cache" -exec rm -r {} +