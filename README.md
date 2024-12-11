# recipe-sharing-app

## Project deployed at https://crispy-e7ajd8bmgkg3ghgk.italynorth-01.azurewebsites.net/

## How to run project

### 1. Download project

Copy repository address
In terminal navigate to the directory where you want the project to be cloned

```commandline
git clone <repository_address>
```

### 2. Create virtual enviroment

In terminal navigate to the directory, containing manage.py
```commandline
python -m venv .venv
```
Open PyCharm and set your project virtual enviroment to the one created


### 3. Activate virtual enviroment
#### On Windows
```commandline
.venv\Scripts\activate
```
#### On Linux and MacOS
```commandline
source .venv/bin/activate
```

### 4. Install dependencies
```commandline
pip install -r requirements.txt
```

### 5. Database
#### Easy way
In settings.py replace the database settings with the following code:
```
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": <database_name>,
        "USER": <your_database_user>,
        "PASSWORD": <your_database_password>,
        "HOST": <your_database_host>,
        "PORT": <your_database_port>,
    }
}
```
Open PostgreSQL console and run:
```commandline
CREATE DATABASE <database_name>;
```

#### Harder way
Use the credentials in the .env file. Open PostgreSQL console and run the following commands:
```commandline
CREATE USER <username_from_env> WITH PASSWORD '<password_from_env>';
```
```commandline
CREATE DATABASE <db_name_from_env> OWNER <username_from_env>;
```
```commandline
GRANT ALL PRIVILEGES ON DATABASE <db_name_from_env> TO <username_from_env>;
```

### 6. Migrations
In terminal run:
```commandline
python manage.py migrate
```

### 7. Run project
The project should be ready to go. Either click the "run" button in PyCharm, or enter the following command in terminal:
```commandline
python manage.py runserver
```
