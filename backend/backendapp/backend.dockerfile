###############################################
# Base Image
###############################################
FROM python:3.9-alpine as python-base

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1
#    PIP_NO_CACHE_DIR=off \
#    PIP_DISABLE_PIP_VERSION_CHECK=on \
#    PIP_DEFAULT_TIMEOUT=100 \
#    POETRY_VERSION=1.1.0 \
#    POETRY_HOME="/opt/poetry" \
#    POETRY_VIRTUALENVS_IN_PROJECT=true \
#    POETRY_NO_INTERACTION=1 \
#    PYSETUP_PATH="/opt/pysetup" \
#    VENV_PATH="/opt/pysetup/.venv"

# prepend poetry and venv to path
#ENV PATH="$POETRY_HOME/bin:$VENV_PATH/bin:$PATH"

###############################################
# Builder Image
###############################################
FROM python-base as builder-base
#适用alpine版本镜像
RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.ustc.edu.cn/g' /etc/apk/repositories \
    && apk update \
    && apk add --no-cache curl \
    && apk add postgresql-dev gcc python3-dev musl-dev
#适用slim版本
#RUN sed -i "s@http://deb.debian.org@http://mirrors.aliyun.com@g" /etc/apt/sources.list
#RUN apt-get update \
#    && apt-get install --no-install-recommends -y \
#    curl \
#    build-essential

# install poetry - respects $POETRY_VERSION & $POETRY_HOME
RUN curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false
#raw国内源,速度不理想
#RUN curl -sSL https://raw.staticdn.net/python-poetry/poetry/master/get-poetry.py | python -
#https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py

# copy project requirement files here to ensure they will be cached.
#WORKDIR $PYSETUP_PATH
COPY poetry.lock pyproject.toml /

# install runtime deps - uses $POETRY_VIRTUALENVS_IN_PROJECT internally
RUN poetry install --no-root

###############################################
# Production Image
###############################################
FROM builder-base as production
#COPY --from=builder-base $PYSETUP_PATH $PYSETUP_PATH
WORKDIR /app
COPY ./app .
#ENV PYTHONPATH=/app