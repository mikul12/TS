FROM python:3.6.5

WORKDIR .\Consumer

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "-W ignore", "-u", "./consume.py" ]