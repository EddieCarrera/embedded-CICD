# Useful commands:
# docker container ls:              lists created containers
# docker start -i my-container      starts a created container
# docker container rm my-container  removes a created container
# docker rmi my-image               removes "my-image" image
##############################################################################
# docker create -it --entrypoint="/bin/bash" --name my-container my-image
# -i creates an interactive container (allows for cmd line interactivity).
# -t short for "tty", which creates command line interaction
# --entrypoint overrides default entrypoint given from Dockerfile
# --name names the container with given name
##############################################################################
# docker cp another-test.py my-container:/tests/another-test.py
# Allows for file transfer into an existing container
##############################################################################
# docker run --rm my-image
# This is the create + start command into one command
# --rm makes is such that the container is deleted after it runs and exists

# Fetch ubuntu image
FROM ubuntu

# Install Python
# RUN command runs a command as a layer in Docker so that
# filesystem is permenently changed
# build-essential includes gcc into image
RUN \ 
  apt-get update && \ 
  apt-get install -y python3 && \
  apt-get install -y build-essential 

# Create a directory for our tests
RUN mkdir /tests

# Copy in python script
COPY test.py /tests/test.py

# Copy in program under tests
COPY main.cpp /tests/main.cpp

# Command that will be invoked when container starts
ENTRYPOINT [ "python3", "tests/test.py" ]

# CMD can also be used, which implements the following:
# CMD[something else] = $ /bin/sh -c "something else"