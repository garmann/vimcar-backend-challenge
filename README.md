register new user:
http --form POST http://0.0.0.0:5000/register username="1@2.de" password="XXX"

activate new account:
http http://0.0.0.0:5000/activationlink/gregas_dasd.dxe_7822035

login and get data:
http -a 1@13.de:XXX http://0.0.0.0:5000/data


# TODO
# testing: http & unittests
# docker setup
# readme