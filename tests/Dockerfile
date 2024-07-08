FROM continuumio/miniconda3:latest

RUN apt-get update

RUN conda install -y -c conda-forge numpy=1.26.4 pydap

ARG UNAME=test_opendap
ARG UID=1000
ARG GID=1000
RUN groupadd -g $GID -o $UNAME
RUN useradd -m -u $UID -g $GID -o -s /bin/bash $UNAME
USER $UNAME

WORKDIR /app
ENTRYPOINT [ "python", "opendap_pydap.py" ]
