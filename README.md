# Dockerise FastAPI Mini-project

This repo is a guide to dockerise a FastAPI project. 


## How to build this repo?
1. set-up the enviroment, install whatever needed <br>
`python3 -m venv env` <br>
`source env/bin/activate`
2. build the project using FastAPI: main.py and test_main.py
3. save the dependencies:
   `pip freeze > requirements.txt ` 
4. dockerise it:<br>
    4.1. Dockerfile: instruction to build images <br>
    4.2. .dockerignore: like .gitignore <br>
    4.3. docker-compose.yaml: docker compose allows you to define and manage multi-container applications in a single YAML file <br>
    4.4. .env: define environment varialbes, take it as hyp.yaml <br>
5. check the project by `docker compose up --build`, version control via Git.

## Docker cheatsheet
`docker ps` - List containers<br>
`docker compose up --build` - Create and start containers, Build images before starting containers <br>
`docker run` - Create and run a new container from an image <br>
`docker compose down` -  Stop and remove containers, networks<br>
`docker compose watch` - Watch build context for service and rebuild/refresh containers when files are updated<br>
