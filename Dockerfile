FROM python:3.14.7-slim

# Prevent Python from writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1

# Make Python output appear immediately
ENV PYTHONUNBUFFERED=1

# Install uv
COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

# Install dependencies first.
# This layer will be cached until pyproject.toml or uv.lock changes.
COPY pyproject.toml uv.lock ./
COPY dataset dataset
COPY scripts scripts

RUN uv sync --locked --no-install-project

# Copy application source
COPY src ./src

RUN uv sync --locked

EXPOSE 8000
