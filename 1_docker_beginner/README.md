# Docker Beginner

Based on the tutorial:

[https://www.youtube.com/watch?v=bi0cKgmRuiA](https://www.youtube.com/watch?v=bi0cKgmRuiA)

### Definitions

- A `Dockerfile` is a blueprint that contains the instructions to build a Docker image
- An `Image` is a template for instantiating and running containers
- Then the `Container` is the actual running process (the instance)
- Each line in the Dockerfile is also called a build step of a `Docker Layer`
    - What is the Docker build cache?
        - Every time you build a Docker image, *each build step is cached*. To improve build time, if a particular build step has not been changed, Docker has a mechanism to reuse it from cache - this way those steps need not be rebuild.
- Always aim to:
    - Reduce build time
    - Keep image size to minimum (e.g. `COPY` only the absolutely necessary files, rather than full folder)

### Docker Commands

1. `RUN` vs `CMD` inside the Dockerfile
    - The `RUN` command is typically used to install applications and software packages. For example,
        
        `RUN ["apt-get", "install", "firefox"]`  (executable form)
        
        `RUN apt-get -y install firefox` (shell form)
        
    - `RUN` executes the command on top of the current image, and by creating a new image layer. Dockerfile often contains multiple RUN instructions.
    - The `CMD` directive allows user to specify the default command executed by the container once it is started.
        
        Example: `CMD ["python3", "app.py"]`
        
    - If there are multiple `CMD` instructions in the Dockerfile, only the last `CMD` is valid.
    - In case you provide a command with the `docker run` command, the `CMD`
    in the D*ockerfile* gets ignored*.* For instance,
        
        `docker run -it ubuntu bash` —> here `bash` overrides the `CMD` line in the Dockerfile (which gets ignored)
        
    - (Advanced) `ENTRYPOINT` can be used instead of `CMD`, if this ignoring behaviour is not desirable: [https://www.geeksforgeeks.org/difference-between-run-vs-cmd-vs-entrypoint-docker-commands/](https://www.geeksforgeeks.org/difference-between-run-vs-cmd-vs-entrypoint-docker-commands/)

1. `build` vs `run` commands
    1. `docker build .` converts your `Dockerfile` into an image.
    2. `docker create <your-image>` creates a container from your image from step 1.
    3. `docker start container_id` starts the container from step 2.
    4. `docker run image` - creates and starts a container from an image - i.e., it is a shortcut for 2. and 3. (`docker create image` and `docker start container_id`).

### Docker Compose

[https://www.youtube.com/watch?v=Z44UJUXsOGA](https://www.youtube.com/watch?v=Z44UJUXsOGA)

- If you have multiple services each requiring their own container, then you can use `docker-compose` to specify the definitions of each of the containers in a single YAML file
- Basically, Docker Compose is a tool to help define and share multi-container applications (e.g. when you have different micro-services)
- The configuration for a docker compose file is done in `docker-compose.yml`.
You don’t need to place this at the root of your project like a Dockerfile. In fact, it can go anywhere, as it doesn’t depend on any other code

### Links

Some ways to optimize your Dockerfile:

[Intro Guide to Dockerfile Best Practices | Docker](https://www.docker.com/blog/intro-guide-to-dockerfile-best-practices/)