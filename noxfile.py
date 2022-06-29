"""
Automation tasks.
"""
import nox
from nox.sessions import Session

SOURCE_CODE = "./budgetapp"

# nox options
nox.options.sessions = ["format", "lint"]
nox.options.reuse_existing_virtualenvs = False
nox.options.default_venv_backend = "none"


#
# FORMAT AND LINTING CODE TASKS
# ----------------------------------------------------
@nox.session(name="format")
def format_code(session: Session):
    """Task to format all files"""
    session.run("isort", ".")
    session.run("black", ".")


@nox.session(name="lint")
def lint_code(session: Session):
    """This taks is used to run linting on code"""
    session.run(
        "pylint",
        "-j",
        "4",
        "-f",
        "colorized",
        SOURCE_CODE,
    )


#
# RUN UNIT TESTS IN DOCKER
# ----------------------------------------------------
@nox.session(name="test-unit")
def test_unit(session: Session):
    """Run all the unit tests in docker container"""
    session.run(
        "docker",
        "compose",
        "run",
        "webapp-budgetapp",
        "python",
        "manage.py",
        "test",
        "tests.unit",
        external=True,
    )


#
# RUN FUNCTIONAL TESTS
# ----------------------------------------------------
@nox.session(name="test-functional")
def test_functional(session: Session):
    """Run all functional tests locally"""
    session.run(
        "python",
        "manage.py",
        "test",
        "tests.functional",
    )
