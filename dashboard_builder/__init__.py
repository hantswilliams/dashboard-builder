def get_template(template_name):
    with open(f'dashboard_builder/templates/{template_name}', 'r') as file:
        return file.read()
