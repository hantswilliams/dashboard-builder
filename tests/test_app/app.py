import os 
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..'))) ## noqa: E501, added for local dev testing / 2 levels up from tests/test_app/app.py

from flask import Flask, render_template_string, request # noqa: E402, F401
import pandas as pd # noqa: E402, F401
from dashboard_builder import get_template # noqa: E402, F401

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello World!'

if __name__ == '__main__':
    app.run(debug=True)