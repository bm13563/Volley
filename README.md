# Volley
Connecting great people

# Installing the project
Config files are not kept in the project!!
1. Clone the repository
2. Create a virtual environment -> python -m venv venv
3. Install requirements from requirements.txt -> pip install

# Working on the project
1. Run the project through the manage.py file, using the --run flag + the environment. This is recommended, rather than using flask run or python app.py, since environment variables, flask config, linting etc is handled explicitly.

```bash
python manage.py --run dev
```

2. Run tests through the manage.py file, using the --test flag. This will handle environments and flask config automatically.

```bash
python manage.py --test
```

3. Commit to the repo through the manage.py file, using the --commit flag. This will run the linters and push to the correct location. This must have a commit message.

```bash
python manage.py --commit "The commit message for the change"
```
