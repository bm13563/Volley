import argparse, os

# set root path
root_path = os.path.dirname(os.path.abspath(__file__))

# set up argparser
parser = argparse.ArgumentParser(description='Utilities file for running all scripts related to the Volley project')
parser.add_argument("--run", help="run the flask project in a specific environment")

# parse the input arguments
args = parser.parse_args()
argdict = vars(args)

# run the volley flask app in the specified environment
# e.g "python utils.py --run dev"
if "run" in argdict:
    if argdict["run"] == "dev":
        os.environ["FLASK_APP"] = "api"
        os.environ["FLASK_ENV"] = "development"
        os.environ["APP_CONFIG_FILE"] = os.path.join(root_path, "config", "dev.py")
        os.system("flask run")


