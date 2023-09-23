import os

def get_template(template_name):
    current_dir = os.path.dirname(__file__)  # This gets the directory where __init__.py resides
    template_path = os.path.join(current_dir, 'templates', template_name)
    
    with open(template_path, 'r') as file:
        return file.read()
