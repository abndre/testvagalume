FROM python
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt

CMD export LC_ALL=C.UTF-8
CMD export LANG=C.UTF-8

ENTRYPOINT ["python"]
CMD ["app.py"]
