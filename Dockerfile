FROM tiangolo/uwsgi-nginx-flask:python3.6-alpine3.7
RUN apk --update add bash nano git
ENV STATIC_URL /static
ENV STATIC_PATH $HOME/gitpro/Kambuche/src/static
COPY ./requirements.txt /var/www/requirements.txt
RUN pip install --upgrade pip
RUN pip install -r /var/www/requirements.txt
