FROM python:3.12.1-bookworm

WORKDIR /app

RUN python3 -m venv .venv
COPY . .
RUN .venv/bin/pip install -e .

CMD [".venv/bin/gunicorn", "-w3", "--bind", "0.0.0.0:8000", "mirrsearch.api.app:launch()"]
