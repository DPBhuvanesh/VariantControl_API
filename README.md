# VariantControl_API

This project utilizes FastAPI and PostgreSQL to manage variants of dresses. It implements CRUD operations (Create, Read, Update) for dress variants. The primary focus of this project is to learn FastAPI, SQLAlchemy, and Pydantic for schema creation.

## Prerequisites

- Install PostgreSQL: Download and install the PostgreSQL database management system from the official website.
- Install pgAdmin4: Download and install pgAdmin4, a PostgreSQL administration tool, for managing your PostgreSQL server and databases.

## Getting Started

1. Clone this repository to your local machine.
2. Navigate to the project directory in your terminal.

## 1.Install the project dependencies by running:

## pip install -r requirements.txt

## 2.Create a PostgreSQL database and update the database details in the project configuration. 

EXAMPLE : DATABASE_URL = "postgresql://username:password@localhost/databasename"

## 3. Run the FastAPI application using Uvicorn:

uvicorn main:app --reload

## 4.Example for acessing API

Access the API at http://localhost:8000/doc#/ to explore the Swagger UI documentation and interact with the API endpoints.

## Contributing
If you'd like to contribute to this project, feel free to fork it and submit a pull request with your changes. Contributions are welcome!


