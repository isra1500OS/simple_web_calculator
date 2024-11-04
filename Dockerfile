# syntax=docker/dockerfile:1

FROM python:3.13
ENV VIRTUAL_ENV=/usr/src/app
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

#WORKDIR /usr/src/app
COPY requirements.txt .
#RUN pip3 install Flask
RUN pip install -r requirements.txt
COPY . .
RUN chmod +x app.py


CMD [ "python3", "app.py"]