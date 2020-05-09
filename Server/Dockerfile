FROM python:3.6.5

WORKDIR .\server

COPY requirements.txt ./
COPY templates ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./serwer.py" ]