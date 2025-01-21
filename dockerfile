FROM python

WORKDIR /app


COPY . .

EXPOSE 3000
RUN pip install -r requirements.txt

CMD [ "python", "app.py" ]

