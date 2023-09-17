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
    PYTHON_REQUIREMENTS_FILE=local
    DJANGO_SETTINGS_MODULE=budgetapp.settings.dev
    SECRET_KEY={secret}
    DJANGO_DEBUG=True
    LITESTREAM_AZURE_ACCOUNT_KEY="op://Development/budgetapp-storage-key/credential"
    REPLICA_URL="abs://budgetapp@databases/prod/prod.db"
    DEV_DB_PATH="./data/dev.db"
    PROD_DB_PATH="./data/prod.db"
    """
    env_path = PROJECT_ROOT / ".env"
    with open(env_path, "w") as env:
        env.write(environments)


def init_node_environment():
    """
    Run yarn install
    """
    subprocess.run(["yarn", "install"], shell=True)


def install_pre_commit():
    """
    Run pre-commit install
    """
    subprocess.run(["pre-commit", "install"], shell=True)


def main():
    logger.info("Create .env file")
    create_environment_variables()
    logger.info("Install node packages")
    init_node_environment()
    logger.info("Install pre-commit")
    install_pre_commit()


if __name__ == "__main__":
    main()
