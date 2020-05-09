FROM python:3.6.5

WORKDIR .\scraper

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "-u", "./Scraper.py" ]