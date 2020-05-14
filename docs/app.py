"""
app.py

Main Dash/Flask application code.
"""
import flask
from flask import Flask

app = Flask(
    __name__,
    static_url_path = '/', 
    static_folder='_build/html',
)

@app.route('/')
@app.route('/<path:path>')
def serve_documentation(path = 'index.html'):
    """
    Serve the Sphinx generated html documentation
    located in the doc/_build/html directory.

    :param path:    html filepath to serve

    :returns:       send_static_file Flask method called with path
    """
    return app.send_static_file(path)


if __name__ == "__main__":
    app.run(debug=True)
else:
    server = app.run()
