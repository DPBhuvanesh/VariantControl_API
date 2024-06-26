# VariantControl_API

This project utilizes FastAPI and PostgreSQL to manage variants of dresses. It implements CRUD operations (Create, Read, Update) for dress variants. The primary focus of this project is to learn FastAPI, SQLAlchemy, and Pydantic for schema creation.

## Prerequisites

- Install PostgreSQL: Download and install the PostgreSQL database management system from the official website.
- Install pgAdmin4: Download and install pgAdmin4, a PostgreSQL administration tool, for managing your PostgreSQL server and databases.

## Getting Started

1. Clone this repository to your local machine.
2. Navigate to the project directory in your terminal.
3. Use any code editor and run python environment
4. Must Activate the environment in powershell or any terminal you have
5. This help to run in virual environment, freeze the version of software and runs the smoothly program.
If you want to frezze use freeze command to freeze the version
   

## This is for powershell
``` environment
 python -m venv env
```
``` activate
.\\env\Scripts\activate.ps1
```


   
## 1.Install the project dependencies by running:
 ``` bash
 pip install -r requirements.txt
```

## 2.Create a PostgreSQL database and update the database details in the project configuration. 
   
   Download PGAdmin 4 and PostregresSQL for your system. Open PGadmin4 create and server and database.
   Set the password in Installation. 

``` python
EXAMPLE : DATABASE_URL = "postgresql://username:password@localhost/databasename"
```
## 3. Run the FastAPI application using Uvicorn
```python
uvicorn main:app --host 0.0.0.0 --port 80

```
## 4. Run this as locahost to access the API

``` site
http://localhost/docs
```

This code have been pytested and Tested many times so If you have any trouble please post it.

## This Project helps me to learn more things in FastAPI and Sqlalchemy, I have learnt PostregreSQL and it's Function.
## Contributing
If you'd like to contribute to this project, feel free to fork it and submit a pull request with your changes. Contributions are welcome!


