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

## Setup and Installation

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

4.  **Initialize the Database**
    Run the following Flask CLI commands to set up the database and apply the initial migration.

    ```bash
    # (First time only) Create the migrations folder
    flask db init

    # Create an initial migration script
    flask db migrate -m "Initial migration"

    # Apply the migration to create the database and tables
    flask db upgrade
    ```

5.  **Run the Application**
    The application can be started using the Flask CLI.
    ```bash
    flask run
    ```
    The application will be available at `http://127.0.0.1:5000`.

## How It Works

The core of the application is the `auto_route_handler` in `app/auto_loader.py`. When you navigate to a URL, it first checks for a matching rule in `app/config/rules.py`.

-   If a rule is found, it executes the associated handler or middleware.
-   If no rule is found for a `GET` request, it attempts to render a corresponding HTML template from the `app/templates/` directory (e.g., a request to `/users` will try to render `app/templates/users.html`).