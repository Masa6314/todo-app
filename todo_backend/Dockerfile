FROM python:3.9-buster
ENV PYTHONUNBUFFERED=1

# 作業ディレクトリ
WORKDIR /src

RUN pip install --upgrade pip && pip install poetry

ENV POETRY_VIRTUALENVS_IN_PROJECT=true

# ✅ ファイルを /src にコピー（pyproject.toml, poetry.lock を含める）
COPY pyproject.toml poetry.lock ./

RUN poetry install --no-root --no-interaction --no-ansi

# ✅ アプリケーション全体を /src にコピー
COPY . .

# 起動
ENTRYPOINT ["poetry", "run", "uvicorn", "api.main:app", "--host", "0.0.0.0", "--reload"]
