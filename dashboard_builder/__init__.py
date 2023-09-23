import importlib.resources as pkg_resources

def get_template(template_name):
    try:
        content = pkg_resources.read_text('dashboard_builder.templates', template_name)
        return content
    except FileNotFoundError:
        return f"Template {template_name} not found!"
