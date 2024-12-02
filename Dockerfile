FROM python:3.12.3


COPY . .

RUN pip install -r requirements.txt

CMD [ "python3", "src/slack.py" ]