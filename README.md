# Challenge @ Invera

Django application for the Invera's challenge.

[![Built with Django](https://img.shields.io/badge/built%20with%20Django-ff69b4.svg?logo=django&color=black)](/)

## Postman Documentation

[![Run in Postman](https://run.pstmn.io/button.svg)](https://god.gw.postman.com/run-collection/17728852-fe2f566e-8677-4f48-8f0d-2252fb381c27?action=collection%2Ffork&source=rip_markdown&collection-url=entityId%3D17728852-fe2f566e-8677-4f48-8f0d-2252fb381c27%26entityType%3Dcollection%26workspaceId%3De2dd2eb0-609c-4662-aee5-e51c7cbdb4ee)

## Getting Up and Running Locally with Docker

The steps below will get you up and running with a local development environment. All of these commands assume you are in the root of your generated project.

### Prerequisites

- Docker
- Docker-Compose

### Steps

- Clone the repo `git clone https://github.com/francosbenitez/invera-challenge`.
- Navigate to repo directory `cd invera-challenge`.

#### Server

- Build and run the docker-compose file `docker-compose up --build`.
- Go to [http://0.0.0.0:8000/](http://0.0.0.0:8000/). On this route, you can also find the Swagger Documentation.
- Enjoy!

#### Tests

- Run `docker-compose run --rm web pytest`.

## Preview

I also deployed a production version of this app. To try it out:

- Go to [https://invera-challenge.up.railway.app/](https://invera-challenge.up.railway.app/)
- Enjoy!
