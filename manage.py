import argparse, os, sys

# set root path
root_path = os.path.dirname(os.path.abspath(__file__))

# set up argparser
parser = argparse.ArgumentParser(description='Utilities file for running all scripts related to the Volley project')
parser.add_argument("--test", default=(False), action="store_true", help="run tests for the project")
parser.add_argument("--run", default=(False), help="run the flask project in a specific environment")

# parse the input arguments
args = parser.parse_args()
argdict = vars(args)

# ensure that only one utility is being used at a time
used_args = [arg for arg in argdict.values() if arg]
if len(used_args) > 1:
    print("Please only use one utility argument at a time.")
    sys.exit()

# run tests for the volley flask app
# e.g "python manage.py --test"
if argdict["test"]:
    os.environ["FLASK_APP"] = "api"
    os.environ["FLASK_ENV"] = "development"
    os.system("python -m pytest")

# run the volley flask app in the specified environment
# e.g "python manage.py --run dev"
if argdict["run"]:
    if argdict["run"] == "dev":
        os.environ["FLASK_APP"] = "api"
        os.environ["FLASK_ENV"] = "development"
        os.environ["APP_CONFIG_FILE"] = os.path.join(root_path, "config", "dev.py")
        os.system("flask run")

