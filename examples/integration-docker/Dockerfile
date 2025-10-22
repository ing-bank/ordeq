# Use a Python image with uv pre-installed
FROM ghcr.io/astral-sh/uv:python3.12-bookworm-slim

# Copy the source code into the image
ADD . /app

# Place executables in the environment at the front of the path
ENV PATH="/app/.venv/bin:$PATH"

# Sync the project into a new environment
WORKDIR app
RUN uv sync

# Set the entrypoint to run the Ordeq application
ENTRYPOINT ["uv", "run", "src/app/__main__.py", "run"]
