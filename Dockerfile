# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.7-slim

# Add build arguments
# Copy local code to the container image.
ENV APP_HOME /pycm

WORKDIR $APP_HOME

# Install production dependencies.
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    python3-dev \
    libssl-dev \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy the application source
COPY . ./

# Install Python dependencies
RUN pip install -r requirements.txt --no-cache-dir
# TODO
# ENV PYTHONPATH /workspace/${_PYTHONPATH}
# prior to running our web service, get berglas
COPY --from=gcr.io/berglas/berglas:latest /bin/berglas /bin/berglas

# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
ENTRYPOINT exec /bin/berglas exec -- gunicorn --bind :$PORT --workers 1 --threads 8 app:app 
