# FROM scratch AS data_stage
FROM python:3.8.3-buster

# COPY --from=data_stage /pref_ds /pref_ds
# RUN chmod -R 777 /pref_ds/

COPY ../requirements.txt /api/requirements.txt
# COPY --from=data_stage /api/requirements.txt /api/requirements.txt

RUN apt-get update -y
# RUN apt-get install ca-certificates
# RUN apt-get install -y software-properties-common gnupg
# RUN add-apt-repository ppa:deadsnakes/ppa -y
# RUN apt install python3 python3-pip -y
# RUN python3 -m pip install -U --upgrade pip
# COPY --from=build-stage /app/public/ /api/
WORKDIR /api
RUN pip3 install -r requirements.txt
RUN pip3 install gunicorn

COPY ./ /api/

# COPY ./nginx.py.conf /etc/nginx/conf.d/default.conf

CMD flask run --host=0.0.0.0 --port=$PORT
# gunicorn --bind 0.0.0.0:8000 wsgi:app  --daemon