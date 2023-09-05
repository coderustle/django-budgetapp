#!/usr/bin/env python

import logging
import random
import string
import subprocess
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger()


PROJECT_ROOT = Path(__file__).parent.parent


def create_environment_variables():
    """
    This function create the .env file with the needed
    environment variables.
    """
    secret = "".join(
        random.choice(string.ascii_letters + string.digits) for _ in range(50)
    )
    environments = f"""
    BUILD_ENV=local
    SECRET_KEY={secret}
    DJANGO_SETTINGS_MODULE=budgetapp.settings.dev
    DJANGO_DEBUG=True
    DB_NAME=budgetapp_dev
    DB_HOST=localhost
    DB_PASS=abc123
    DB_USER=budget
    """
    env_path = PROJECT_ROOT / ".env"
    with open(env_path, "w") as env:
        env.write(environments)


def init_node_environment():
    """
    Run yarn install
    """
    subprocess.run(["yarn", "install"], shell=True)


def main():
    logger.info("Create .env file")
    create_environment_variables()
    logger.info("Install node packages")
    init_node_environment()


if __name__ == "__main__":
    main()
