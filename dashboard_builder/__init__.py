# import importlib.resources as pkg_resources

# def get_template(template_name):
#     with pkg_resources.path('dashboard_builder.templates', template_name) as template_path:
#         with open(template_path, 'r') as file:
#             return file.read()

import importlib.resources as pkg_resources

def list_all_resources_in_package():
    return pkg_resources.contents('dashboard_builder.templates')

print(list_all_resources_in_package())

content = pkg_resources.read_text('dashboard_builder.templates', 'base.html')
print(content)

def get_template(template_name):
    return pkg_resources.read_text('dashboard_builder.templates', template_name)
