FROM python:3.13.1

RUN apt-get update 
RUN apt-get install -y python3-opencv pipx
RUN pipx install poetry

ENV PATH="/root/.local/bin:$PATH"

COPY . /services/receipt_service
WORKDIR /services/receipt_service

RUN poetry install

RUN chmod +x ./init.sh

CMD [ "./init.sh" ]