import os
from flask import render_template, abort, request
from jinja2 import TemplateNotFound
from fnmatch import fnmatch
from .config.rules import RULES, BLOCKED_PREFIXES

def auto_route_handler(path):
    for pattern, rule_config in RULES.items():
        if fnmatch(path, pattern):
            if 'middleware' in rule_config:
                for middleware_func in rule_config['middleware']:
                    response = middleware_func(path)
                    if response is not None:
                        return response

            handler = rule_config.get(request.method)
            if handler:
                result = handler(path)
                
                if request.method == 'GET' and isinstance(result, dict):
                    template = result.get('template')
                    if template:
                        return render_template(template, **result.get('context', {}))
                
                return result

    for blocked in BLOCKED_PREFIXES:
        if path.startswith(blocked):
            abort(404)

    if request.method == 'GET':
        template_name = f"{path}.html"
        if path.endswith('/') or not path:
            template_name = f"{path or 'index'}.html"

        try:
            return render_template(template_name)
        except TemplateNotFound:
            try:
                return render_template(f"{path}/index.html")
            except TemplateNotFound:
                abort(404)
    
    abort(405)