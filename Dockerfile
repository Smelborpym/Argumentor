FROM python:3.9

WORKDIR /app

RUN pip install poetry

RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock* ./

RUN poetry install --no-interaction --no-ansi

COPY . .

RUN useradd -m appuser && chown -R appuser /app
USER appuser

CMD ["poetry", "run", "streamlit", "run", "app/app.py"]