FROM python

WORKDIR /app
COPY . /app

# Expose ports
EXPOSE 8080

# set environment variables
ENV TZ="America/Bogota"
ENV SECRET_KEY="yaAZgHd7SkmLaHZudFZDRgTOnVoFWU2u"
ENV EMAIL_SALT_KEY="dcdg5RW3YCKpJIkgdD4RUigjGfpyXHCB"
ENV JWT_SECRET_KEY="bjKtLdGDbb0eB9GW9ITJh6kETPOThVVj"
ENV JWT_REFRESH_SECRET_KEY="h2KjPlBTqxyz8soqu7m5YWVIyr5aUHbn"
ENV POSTGRES_URI="postgresql+psycopg2://postgres:1234@postgres_store:5432/store"
ENV POSTGRES_URI_TEST="postgresql+psycopg2://postgres:1234@postgres_store:5432/store_test"
ENV REDIS_HOST=redis_store


RUN pip install --upgrade pip
RUN pip install -U autopep8 --user
RUN pip --no-cache-dir install autoflake8
RUN pip --no-cache-dir install -r /app/requirements.txt
