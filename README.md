# vimcar-backend-challenge

this is a first shoot for the backend challenge from vimcar. for the last months i have worked with js - so i had some fun with python now. its a simple implementation but it works and hopefully shows, i'm albe to create something working with python too.

currently you have to run your own flask and myqsl process. there is no docker container or else. for my development i always use my vagrant images. this would be to overkill to upload them.

## commands
- register new user:
```http --form POST http://0.0.0.0:5000/register username="1@1.de" password="XXX"```

- activate new account:
```http http://0.0.0.0:5000/activationlink/gregas_dasd.dxe_7822035```

- login and get data:
```http -a 1@1.de:XXX http://0.0.0.0:5000/data```

## todo
- testing: http & unittests
- docker setup

## setup
- import mysql data from vimcar.sql or create own database with commands from sql-struct.sql
- change config.json
- pip install -r requirements.txt
- start flask with python3 app.py

## notes
- i'm using flask with basic auth
- mysql is used for persistence
- all inputs are checked
- bcrypt is used for pw/db salting