# Создание виртуального окружения
python -m venv venv

# Активация виртуального окружения
 venv/Scripts/activate

# Активация виртуального окружения
pip install requirements.txt

# Запуск celery
celery -A src.apps.celery_app:celery worker --loglevel=INFO --pool=solo

# Запуск flower
celery -A src.apps.celery_app:celery flower
