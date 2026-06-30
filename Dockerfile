FROM python:3.13-slim

WORKDIR /src

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["uvicorn", "src.api:router", "--host", "0.0.0.0", "--port", "8000", "--reload"]