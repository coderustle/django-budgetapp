"""
Automation tasks.
"""
import nox

SOURCE_CODE = "./budgetapp"

# nox options
nox.options.sessions = ["format", "lint"]
nox.options.reuse_existing_virtualenvs = False
nox.options.default_venv_backend = "none"


#
# FORMAT AND LINTING CODE TASKS
# ----------------------------------------------------
@nox.session(name="format")
def format_code(session):
    """Task to format all files"""
    session.run("isort", ".")
    session.run("black", ".")


@nox.session(name="lint")
def lint_code(session):
    """This taks is used to run linting on code"""
    session.run(
        "pylint",
        "-j",
        "4",
        "-f",
        "colorized",
        SOURCE_CODE,
    )
