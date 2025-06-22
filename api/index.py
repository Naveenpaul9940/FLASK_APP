from app import app  # This imports your existing app object

def handler(environ, start_response):
    return app(environ, start_response)