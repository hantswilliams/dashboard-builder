You start with the basic setup (initializing and configuring), then move on to defining and registering your components. Once everything is registered, you proceed with the rendering. Finally, there are some additional utility functions and customizations for added flexibility. This structure offers a linear flow for someone setting up their dashboard or view from scratch.

### 1. **Initialization and Configuration**
Create an instance of `ComponentManager` with the current Flask request object. Set any default values or configurations for the manager, especially if you want to customize some aspects of rendering.
```python
index_manager = ComponentManager(request)
```
### 2. **Form Group Creation**
Utilize the `create_input_group` class method from `ComponentManager` to create a form group which can contain multiple input components. Register the form group with an instance of the `ComponentManager` using `register_form_groups`.
```python
    input_group = ComponentManager.create_input_group(
        ...
    )
```
### 3. **Component Registration** 
Register input components with the manager. This means linking specific string identifiers (like 'dropdown' or 'text') with their corresponding Python classes (`InputDropdown`, `TextInput`, etc.). Similarly, register output components (like 'text' for `OutputText` or 'chart_matplotlib' for `OutputChart_Matplotlib`).
```python
    input_group = ComponentManager.create_input_group(
        ...
        inputs=[
            {
                'type': 'dropdown',
                'name': 'condition_selection',
                'label': 'Select a condition:',
                'values': (df, 'condition')
            }
        ]
    )
```
### 4. **Output Group Creation**
Utilize the `create_output_group` class method from `ComponentManager` to create an output group which can contain multiple output components. Each output component should be registered within the created output group.
```python
    ComponentManager.create_output_group(
        manager_instance=manager,
        outputs=[
            {
                'type': 'text',
                'content': f"Selected conditions From Form 1: {user_selected_1}" 
            },
            {
                'type': 'chart_matplotlib',
                'content': fig
            }
        ]
    )
```
### 5. **Template Management and Final Rendering**
Decide whether to use a custom template or a default one: If custom: Make sure both `template_name` and `template_path` are provided. Fetch the custom template content using `TemplateManager.dashboard_template_custom`. If default: Fetch the default template content using `TemplateManager.dashboard_template`. Create an instance of `DashboardOutput` with the `ComponentManager` instance, template details, and any other custom parameters.  For example, rendering the dashboard using the manager instance can be done with:
       ```python
       return DashboardOutput(manager=index_manager).render()
       ```
Use the `render` method from `DashboardOutput` to merge the components' rendering with the chosen template and generate the final dashboard view.

### 6. **Customization and Utilities**
For custom template configurations, the `template_defaults` method can be used to update the manager's configuration with any keyword arguments. Retrieve these values using `template_defaults_values`. Utilities like `get_input` in the `FormGroup` can be used to fetch specific input components by name.
```python
    # For custom templates
    return DashboardOutput(
        manager=manager,
        template_path="./", 
        template_name="custom_temp.j2", 
        inputs=manager.render_form_groups(), 
        outputs=manager.render_outputs(),
        custom_value_1="This field can be called via custom_value_1 in your jinja template: custom_temp.j2", # if you want to pass custom values to template  # noqa
        custom_value_2="This field can be called via custom_value_2 in your jinja template: custom_temp.j2" # if you want to pass custom values to template # noqa
    ).render()
```

