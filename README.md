# Flask Auto-Routing Template

A feature-rich Flask project template designed for rapid development. It comes with a powerful rule-based auto-routing system, a reusable CRUD mixin for models, and a clean, scalable project structure.

This template is an ideal starting point for building web applications, providing a solid foundation with essential components already configured.

## Features

-   **Application Factory Pattern**: The app is created using a factory (`create_app`), making it modular and easy to configure for different environments (e.g., development, testing, production).
-   **Rule-Based Auto-Routing**: A custom routing system in `auto_loader.py` that minimizes boilerplate. It can automatically render templates based on the URL or execute complex logic defined in a central `rules.py` file.
-   **Middleware Support**: The routing system supports middleware for tasks like authentication (`login_required`) and authorization (`admin_required`).
-   **SQLAlchemy with CRUD Mixin**: Includes a `CRUDMixin` that provides generic Create, Read, Update, and Delete methods, which can be easily added to any SQLAlchemy model to reduce repetitive code.
-   **Database Migrations**: Integrated with `Flask-Migrate` to handle database schema migrations seamlessly.
-   **Centralized Configuration**: Environment-specific settings are managed in `app/config/settings.py`, keeping configuration clean and separate from the application logic.
-   **Clear & Scalable Project Structure**: The project is organized logically, separating models, configuration, extensions, and utilities for easy maintenance and scalability.

## Project Structure

The project is organized to promote separation of concerns and scalability.

```
.
├── app.py                  # Application entry point (runner)
├── instance/               # Instance-specific config and database file
│   └── app.db
├── app/
│   ├── __init__.py           # Application factory (create_app)
│   ├── auto_loader.py        # Core auto-routing logic
│   ├── extensions.py         # Flask extension initializations (db, migrate)
│   │
│   ├── config/
│   │   ├── __init__.py
│   │   ├── rules.py          # Central routing rules, middleware, and handlers
│   │   └── settings.py       # Configuration classes (Development, Production)
│   │
│   ├── models/
│   │   ├── __init__.py
│   │   └── user.py           # Example database model using the CRUDMixin
│   │
│   ├── static/               # Static assets (CSS, JavaScript)
│   │   ├── css/style.css
│   │   └── js/script.js
│   │
│   ├── templates/            # Jinja2 templates
│   │   ├── base.html         # Base layout template
│   │   └── ...
│   │
│   └── utils/
│       ├── __init__.py
│       └── crud_mixin.py     # Reusable CRUD mixin for SQLAlchemy models
│
└── requirements.txt          # Project dependencies
```

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

### Prerequisites

-   Python 3.8+
-   `pip` and `venv`

### Installation

1.  **Clone the repository:**
    ```bash
    git clone <your-repository-url>
    cd <repository-name>
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    # On Windows
    # venv\Scripts\activate
    # On MacOS/Linux
    source venv/bin/activate
    ```

3.  **Install the dependencies:**
    *(You will need to create a `requirements.txt` file first)*
    ```bash
    pip freeze > requirements.txt
    ```
    Then install them:
    ```bash
    pip install -r requirements.txt
    ```
    *Likely dependencies are: `Flask`, `Flask-SQLAlchemy`, `Flask-Migrate`.*

4.  **Run the application:**
    ```bash
    flask run
    # Or
    python app.py
    ```

The application will start, automatically create the `app.db` SQLite database, and apply any migrations. You can access it at `http://127.0.0.1:5000`.

## How to Use This Template

### 1. Configuration

-   Modify `app/config/settings.py` to change the `SECRET_KEY`, database URI, and other settings.
-   Create different configuration classes for `TestingConfig` or `ProductionConfig` as needed.

### 2. Adding New Routes

The routing is handled by `app/auto_loader.py` based on rules in `app/config/rules.py`.

-   **Simple Template Route**: If a URL path matches a template name (e.g., `/about` matches `about.html`), it will be rendered automatically. No code needed.
-   **Routes with Logic**: For routes that require logic (e.g., form handling, database queries), add a rule to the `RULES` dictionary in `app/config/rules.py`.

    **Example: Adding a new `/profile` page that requires login.**
    ```python
    # app/config/rules.py

    def profile_handler(path):
        # Your logic here, e.g., fetch user from database
        user = User.find_by(username=session.get('user'))
        return {
            'template': 'profile.html',
            'context': {'user': user}
        }

    RULES = {
        # ... other rules
        'profile': {
            'GET': profile_handler,
            'middleware': [login_required]
        },
    }
    ```

### 3. Creating New Models

1.  Create a new file in the `app/models/` directory (e.g., `app/models/post.py`).
2.  Define your model class, inheriting from `db.Model` and the `CRUDMixin`.

    ```python
    # app/models/post.py
    from app.extensions import db
    from app.utils.crud_mixin import CRUDMixin

    class Post(CRUDMixin, db.Model):
        id = db.Column(db.Integer, primary_key=True)
        title = db.Column(db.String(120), nullable=False)
        content = db.Column(db.Text, nullable=False)
        # Add user relationship
        user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

        def __repr__(self):
            return f'<Post {self.title}>'
    ```
3.  After creating or modifying a model, generate a new database migration:
    ```bash
    flask db migrate -m "Add Post model"
    ```
4.  The migration is applied automatically when you next run the app.

## License

This project is open-source and available under the [MIT License](LICENSE.md).