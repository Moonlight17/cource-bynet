FROM python:3.8.9 as back-stage

WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apt update \
    && apt install gcc musl-dev
# RUN apk add --no-cache --update postgresql-dev musl-dev linux-headers curl gcc g++ \
#     postgresql-dev wget\
#     gfortran musl-dev 

# RUN apk add --no-cache --update \


# install dependencies
COPY ./requirements.txt /app/requirements.txt
RUN pip install --upgrade cython
RUN pip install --upgrade pip

# RUN wget https://pypi.python.org/packages/da/c6/0936bc5814b429fddb5d6252566fe73a3e40372e6ceaf87de3dec1326f28/pandas-1.4.4-cp36-cp36m-manylinux1_x86_64.whl
# RUN pip install pandas-1.4.4-cp36-cp36m-manylinux1_x86_64.whl



RUN pip install --no-cache-dir -r requirements.txt
# RUN echo test


# copy project
COPY . .
EXPOSE 8000


# production stage
# COPY --from=build-stage /vue/dist /app

# CMD ["python", "manage.py", "makemigrations", "epam"]
# CMD ["python", "manage.py", "migrate", "epam"]


CMD /bin/sh /app/docker-entrypoint.sh
