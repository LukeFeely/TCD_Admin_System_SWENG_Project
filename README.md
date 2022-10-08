# SoftwareEngineeringProject

#### Running the Project

The project makes use of a MySQL database hosted on Digital Ocean. This will remain running for the coming months for the sake of testing the application.

1. Clone the repo

2. If you're using virtualenv (recommended) then run  `virtualenv venv` in the root directory. If not using virtualenv, skip to step 4

3. Activate the virtual env by running this in a bash shell: `source /venv/bin/activate`

4. Install dependencies by running: `pip install -r requirements.txt` in the root directory.

5. Navigate into SoftwareEngineeringProject/ and run: `python manage.py runserver`

6. Go to localhost:8000 in your browser to see the site


#### Customising the settings

To deploy the project with your own configuration, you will need to make the following changes to SoftwareEngineeringProject/SoftwareEngineeringProject/settings.py:

1. Configure the database backend under DATABASES['default']. The project is configured to work with a MySQL database. If you are using a different engine, you will need to install the appropriate Python connector for it and configure it in the same location (e.g. pyscopg2 for PostgreSQL).

2. Configure your email backend at the bottom of the settings. We created an email account for the project which is the current configuration.

3. For proper security, you may want to generate a new secret key. This is a 50 character string of random characters that can be generated yourself or using a cryptographically strong generator online. Enter your new key under SECRET_KEY in the settings file.
