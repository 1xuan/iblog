

## what is Dockerfile?

- Dockerfile

~~~bash
FROM ubuntu
ENV APP nginx
RUN apt-get update && apt-get install -y APP
WORKDIR /var/www/html/
ADD index.html ./
EXPOSE 80
ENTRYPOINT ['some stuff']
CMD ["nginx", "-g", "daemon off;"]
~~~

- FROM

    which is our base image for building our own image

- ENV
    
    Be used to set environment
    
- RUN
    
    Be used to execute shell command in the new layer and commit the result in the new image (Only executes at image build time, not container run time)

- WORKDIR
    
    Change current working directory

- ADD

    ADD files from local host to the Docker image

- EXPOSE

    Expose port on which a containers listens for connections

- ENTRYPOINT
    Which is prepending part of CMD

- CMD
    Sepcify a *default* command that executes when the container is starting
    
*referece [Dockerfile](https://www.educba.com/dockerfile/)*

*referece [Difference Between run, cmd and entrypoint in a Dockerfile](https://www.baeldung.com/ops/dockerfile-run-cmd-entrypoint)*

