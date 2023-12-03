#!/bin/bash

# käynnistetään Flask-palvelin taustalle
FLASK_ENV=test poetry run flask run &

# odetetaan, että palvelin on valmiina ottamaan vastaan pyyntöjä
while [[ "$(curl -s -o /dev/null -w ''%{http_code}'' localhost:5000)" != "302" ]];
  do sleep 1;
done

# suoritetaan testit
poetry run robot src/tests/robot
status=$?

# pysäytetään Flask-palvelin portissa 5000
kill $(lsof -t -i:5000)

exit $status