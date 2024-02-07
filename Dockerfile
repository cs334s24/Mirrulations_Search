FROM python:3.12.1-bookworm

WORKDIR /app

RUN python3 -m venv .venv
RUN .venv/bin/pip install flask gunicorn flask_cors

COPY templates /app/templates
COPY kickoff_app.py .

CMD [".venv/bin/gunicorn", "-w3", "--bind", "0.0.0.0:8000", "kickoff_app:launch()"]
