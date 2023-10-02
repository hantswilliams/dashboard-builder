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
### 3. **Component Registration and Input Group Creation** 
To simplify and streamline the process, we use predefined factory methods for each input component. This not only aids in creating component instances but also reduces the need for separate component registration steps. Use the factory methods inside the `ComponentManager.Inputs` class to directly add your input components. Example of adding in a dropdown component for taking in user input: 
```python
input_group = ComponentManager.create_input_group(
    manager_instance=manager,
    inputs=[
        ComponentManager.Inputs.dropdown('condition_selection', 'Select a condition:', (df, 'condition'))
    ]
)
```

### 4. **Output Group Creation**
To create an output group containing multiple output components, utilize the `create_output_group` class method from `ComponentManager`. With the new architecture, you can leverage factory methods for output components available under `ComponentManager.Outputs`. Here is an example then of creating two output components, one for text and one for a matplotlib figure: 
```python
ComponentManager.create_output_group(
    manager_instance=manager,
    outputs=[
        ComponentManager.Outputs.text_output(f"Selected conditions From Form 1: {user_selected_1}"),
        ComponentManager.Outputs.chart_matplotlib(fig)
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

