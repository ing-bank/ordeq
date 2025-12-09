FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

ADD . /app

ENV PATH="/app/.venv/bin:$PATH"

WORKDIR app
RUN uv sync

ENTRYPOINT ["uv", "run", "-m", "air_quality", "run", "air_quality"]
