FROM mysql:5.7

COPY vimcar.sql /docker-entrypoint-initdb.d/

EXPOSE 3306
