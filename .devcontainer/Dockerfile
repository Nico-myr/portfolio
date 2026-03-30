FROM mcr.microsoft.com/devcontainers/python:1-3.12

WORKDIR /workspaces/${localWorkspaceFolderBasename}

COPY requirements.txt /tmp/requirements.txt
RUN pip install --upgrade pip && pip install -r /tmp/requirements.txt