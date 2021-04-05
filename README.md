# Volley
Connecting great people

# Installing the project
Config files are not kept in the project!!
1. Clone the repository
2. Create a virtual environment -> python -m venv venv
3. Install requirements from requirements.txt -> pip install

# Running the project
Run the project through the manage.py file, using the --run flag + the environment. This will handle environments and flask config automatically. This is recommended, rather than using flask run or python app.py, since environment variables and flask config is handled explicitly.
1. Run the project in development mode -> python manage.py --run dev

# Running tests
Run tests through the manage.py file, using the -test flag. This will handle environments and flask config automatically.
1. Run all tests -> python manage.py --test
