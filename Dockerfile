FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
run chmod 777 /usr/src/app/*

CMD [ "python", "./stac_merge.py" ]
ENTRYPOINT [ "python","/usr/src/app/stac_merge.py"]
