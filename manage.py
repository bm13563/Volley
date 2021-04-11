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

lint_outcome = subprocess.run(["flake8"], stdout=subprocess.PIPE)
if len(str(lint_outcome.stdout)) > 3:
    print(
        f"{fail_colour}LINTING ERRORS FOUND. PROJECT CANNOT BE RUN UNTIL THESE ARE FIXED.{standard_colour}"
    )
    sys.exit()
else:
    print(f"{success_colour}NO LINTING ERRORS FOUND.{standard_colour}")

# run tests for the volley flask app
# e.g "python manage.py --test"
if argdict["test"]:
    os.environ["FLASK_APP"] = "api"
    os.environ["FLASK_ENV"] = "development"
    subprocess.run(["python", "-m", "pytest"])

# run the volley flask app in the specified environment
# e.g "python manage.py --run dev"
if argdict["run"]:
    if argdict["run"] == "dev":
        os.environ["FLASK_APP"] = "api"
        os.environ["FLASK_ENV"] = "development"
        os.environ["APP_CONFIG_FILE"] = os.path.join(
            root_path, "config", "dev.py"
        )
        subprocess.run(["flask", "run"])
