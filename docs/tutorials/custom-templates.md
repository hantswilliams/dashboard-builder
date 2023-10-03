# Templates: Base and Custom Templates

## Default Templates

Be default, you are provided with templates that you can choose between. The first template (base) contains a side bar and a main viewing area, while the second included template (base_nosidebar) contains only the main viewing area. 

You can choose between base and base_nosideby by setting the template_name parameter in the DashboardOutput class to either "base" or "base_nosidebar". If you want the standard base template, you do not need to do anything, as it is the default template.

```python
DashboardOutput(
    manager=manager, # the name of your ComponentManager instance
    ).render()
```

Here is an example of how you would move from the default value of `base` to `base_nosidebar`:

```python
DashboardOutput(
    manager=manager, # the name of your ComponentManager instance
    template_name="base_nosidebar",  # the name of your template with its extension 
    ).render()

```

## Custom Templates

Now, if you would like to create your own template, you can do so by creating a new .j2 file in the templates folder. You can then use the following code to render the template:

```python

DashboardOutput(
    manager=manager, # the name of your ComponentManager instance

    template_path="./",  # the path to your template
    template_name="custom_temp.j2",  # the name of your template with its extension 

    ## and then you can add in as many custom variables as 
    ## you want or need that can be passed to your template....
    custom_value_1 = "This field can be called via custom_value_1 in your jinja template: custom_temp.j2", # if you want to pass custom values to template  # noqa
    custom_value_2 = "This field can be called via custom_value_2 in your jinja template: custom_temp.j2" # if you want to pass custom values to template # noqa
    ).render()

```

**For your custom template to work (e.g., if you want to have inputs and outputs), you need to make sure that you include two sections:**

1. The first section is for displaying the input (forms) components:
```j2

{% for form_group in form_groups %}
    <div class="mb-4 border-b pb-4">
        {{ form_group|safe }}
    </div>
{% endfor %}
```
2. The second section is for displaying the output components: 
```j2

{% for output_component in output_components %}
    <div class="mb-4">{{ output_component|safe }}</div>
{% endfor %}
```