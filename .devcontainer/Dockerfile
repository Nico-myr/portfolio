FROM mcr.microsoft.com/devcontainers/python:1-3.12

RUN apt-get update && apt-get install -y git-lfs

RUN git lfs install

WORKDIR /workspaces/${localWorkspaceFolderBasename}

COPY requirements.txt /tmp/requirements.txt
RUN pip install --upgrade pip && pip install -r /tmp/requirements.txt