# Offical Python runtime
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt ./
COPY parakeet_it.py ./
COPY fibonacci.py ./

RUN pip install --no-cache-dir -r requirements.txt

# the command
CMD ["python3", "parakeet_it.py", "convert-java", "fibonacci.py"]

