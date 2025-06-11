FROM python:3.13

WORKDIR /clinic

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt
RUN chmod +x /clinic/wait-for-it.sh

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]