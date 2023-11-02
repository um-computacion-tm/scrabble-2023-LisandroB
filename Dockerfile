FROM python:3-alpine

RUN apk update
RUN apk add git
RUN git clone https://github.com/um-computacion-tm/scrabble-2023-LisandroB.git
WORKDIR /scrabble-2023-LisandroB
RUN pip install -r requirements.txt

CMD [ "sh", "-c", "coverage run -m unittest -b && coverage report -m && python play.py"]
