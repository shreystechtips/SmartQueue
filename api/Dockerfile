# FROM scratch AS data_stage
FROM nginx

# COPY --from=data_stage /pref_ds /pref_ds
# RUN chmod -R 777 /pref_ds/

COPY ./api/requirements.txt /api/requirements.txt
# COPY --from=data_stage /api/requirements.txt /api/requirements.txt

RUN apt-get update -y
# RUN apt-get install ca-certificates
# RUN apt-get install -y software-properties-common gnupg
# RUN add-apt-repository ppa:deadsnakes/ppa -y
RUN apt install python3 python3-pip -y
RUN python3 -m pip install -U --upgrade pip
# COPY --from=build-stage /app/public/ /api/
WORKDIR /api
RUN pip3 install -r requirements.txt
RUN pip3 install gunicorn

COPY ./api/ /api/

# COPY ./nginx.py.conf /etc/nginx/conf.d/default.conf


CMD gunicorn --bind 0.0.0.0:5000 wsgi:app  --daemon