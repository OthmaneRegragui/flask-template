# ./app/config/rules.py
from flask import session, redirect, abort, request, render_template
from app.models.user import User

def login_required(path):
    if 'user' not in session:
        return redirect('/login')
    return None

def admin_required(path):
    response = login_required(path)
    if response:
        return response
    if session.get('role') != 'admin':
        abort(403)
    return None

def list_users_handler(path):
    users = User.get_all()
    return {
        'template': 'users.html',
        'context': {'users': users}
    }

def add_user_post_handler(path):
    username = request.form.get('username')
    if username:
        existing_user = User.find_by(username=username)
        if not existing_user:
            User.create(username=username, role='user')
    return redirect('/users')

def login_post_handler(path):
    username = request.form.get('username')
    user = User.find_by(username=username)
    if user:
        session['user'] = user.username
        session['role'] = user.role
        return redirect('/dashboard')
    return redirect('/login')

def logout_handler(path):
    session.clear()
    return redirect('/')

RULES = {
    'users': {
        'GET': list_users_handler,
    },
    'user/add': {
        'POST': add_user_post_handler
    },
    'login': {
        'POST': login_post_handler
    },
    'logout': {
        'GET': logout_handler
    },
    'dashboard': {
        'middleware': [login_required]
    },
    'admin/*': {
        'middleware': [admin_required]
    }
}

BLOCKED_PREFIXES = [
    'partials',
]