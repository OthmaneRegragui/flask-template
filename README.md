# Simple Flask Auto-Routing Application

This is a basic Flask application that demonstrates a simple auto-routing mechanism, database integration with Flask-SQLAlchemy, and migrations with Flask-Migrate.

## Features

-   **Auto-Routing**: Automatically renders templates or executes handlers based on the URL path.
-   **Database**: Uses SQLite with Flask-SQLAlchemy for ORM.
-   **Migrations**: Includes Flask-Migrate for handling database schema changes.
-   **CRUD Operations**: A `CRUDMixin` provides common database operations for models.

## Prerequisites

-   Python 3.8+
-   `pip` and `venv`

## Project Setup for a New User (Cloned Repository)

Follow these steps if you have just cloned this repository.

1.  **Clone the Repository**
    ```bash
    git clone <your-repository-url>
    cd <your-repository-name>
    ```

2.  **Create and Activate a Virtual Environment**
    -   On macOS and Linux:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
    -   On Windows:
        ```bash
        python -m venv venv
        .\\venv\\Scripts\\activate
        ```

3.  **Install Dependencies**
    Install all the required packages using the `requirements.txt` file.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Apply Database Migrations**
    This command will create your local `app.db` file and set up all the necessary tables based on the existing migration scripts.
    ```bash
    flask db upgrade
    ```

5.  **Run the Application**
    The application can be started using the Flask CLI.
    ```bash
    flask run
    ```
    The application will be available at `http://127.0.0.1:5000`.

## Developer Guide: Managing the Database

These commands are for developers who are modifying the database schema.

-   **Initializing (First time ever)**: If you are starting this project from scratch and the `migrations` directory does not exist, run this command **once**:
    ```bash
    flask db init
    ```

-   **Creating New Migrations**: After you change your models in `app/models/`, run this command to automatically generate a new migration script:
    ```bash
    flask db migrate -m "A short description of the model changes"
    ```

-   **Applying Migrations**: To apply new migrations to the database, run:
    ```bash
    flask db upgrade
    ```