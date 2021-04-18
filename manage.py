import argparse, os, subprocess, sys

# set root path
root_path = os.path.dirname(os.path.abspath(__file__))

# set up argparser
parser = argparse.ArgumentParser(
    description="Utilities file for running all scripts related to the Volley project"
)
parser.add_argument(
    "--test",
    default=(False),
    action="store_true",
    help="run tests for the project",
)
parser.add_argument(
    "--commit",
    default=(False),
    help="safely commit the project to the correct environment",
)
parser.add_argument(
    "--run",
    default=(False),
    help="run the flask project in a specific environment",
)

# parse the input arguments
args = parser.parse_args()
argdict = vars(args)

# ensure that only one utility is being used at a time
used_args = [arg for arg in argdict.values() if arg]
if len(used_args) > 1:
    print("Please only use one utility argument at a time.")
    sys.exit()

# run pep8 fixes and linter, force correct linting. project will not start until linting errors are fixed
success_colour = "\033[90m"
warning_colour = "\033[93m"
fail_colour = "\033[91m"
standard_colour = "\033[0m"

print(f"{warning_colour}RUNNING AUTOMATIC LINTING.{standard_colour}")
subprocess.run(["black", ".", "-l", "79", "-q"])

# check if there are any linting errors
lint_outcome = subprocess.run(
    [
        "flake8",
        "--ignore=E401,E501",
        "--exclude=.git,.gitignore,*.pot,*.py[co],__pychache__,venv,.env",
    ],
    stdout=subprocess.PIPE,
)

# if there are linting errors, fail and run the linter
if len(str(lint_outcome.stdout)) > 3:
    print(
        f"{fail_colour}LINTING ERRORS FOUND. PLEASE FIX LINTING ERRORS BEFORE CONTINUING.{standard_colour}"
    )
    # run the linter to output the actual problems
    subprocess.run(
        [
            "flake8",
            "--ignore=E401,E501",
            "--exclude=.git,.gitignore,*.pot,*.py[co],__pychache__,venv,.env",
        ],
    )
    sys.exit()
else:
    print(f"{success_colour}NO LINTING ERRORS FOUND.{standard_colour}")

# run tests for the volley flask app
# e.g "python manage.py --test"
if argdict["test"]:
    os.environ["ROOT_PATH"] = root_path
    os.environ["FLASK_APP"] = "api"
    os.environ["FLASK_ENV"] = "development"
    os.environ["APP_CONFIG_FILE"] = os.path.join(
        root_path, "config", "test.py"
    )
    subprocess.run(["python", "-m", "pytest", "--disable-warnings"])

# commit changes to git
# e.g "python manage.py --commit My commit message"
if argdict["commit"]:
    subprocess.run(["git", "add", "."])
    subprocess.run(["git", "commit", "-m", argdict["commit"]])
    subprocess.run(["git", "push"])

# run the volley flask app in the specified environment
# e.g "python manage.py --run dev"
if argdict["run"]:
    if argdict["run"] == "dev":
        os.environ["ROOT_PATH"] = root_path
        os.environ["FLASK_APP"] = "api"
        os.environ["FLASK_ENV"] = "development"
        os.environ["APP_CONFIG_FILE"] = os.path.join(
            root_path, "config", "dev.py"
        )
        subprocess.run(["flask", "run"])
