FROM python:3.12.3
COPY . .

RUN pip install -r requirements.txt

CMD [ "python", "src/slack_connection.py" ]
