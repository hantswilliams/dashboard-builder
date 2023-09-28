from flask import Flask, request
from matplot import create_plot
from data import df

#### For local dev testing....//otherwise turn off - comment out below ###
import os # noqa
import sys # noqa
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
##########################################################################

from dashboard_builder import ComponentManager, DashboardOutput # noqa

app = Flask(__name__)


########################################################################

@app.route('/', methods=['GET', 'POST'])
def index():

    manager = ComponentManager(request)

    # manager.config(
    #     footer_text="Condition Frequency Count Dashboard - Powered by Dashboard Builder"
    # )

    # Use the new create_input_group method
    input_group = ComponentManager.create_input_group(
        manager_instance=manager,
        inputs=[
            {
                'type': 'dropdown',
                'name': 'condition_selection',
                'label': 'Select a condition:',
                'values': (df, 'condition')
            }
        ]
    )

    # User selected value
    user_selected_1 = input_group.get_input('condition_selection').value  

    fig = create_plot(df, user_selected_1)

    ########################################################################
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

    ########################################################################

    # For custom templates
    return DashboardOutput(
        manager=manager,
        template_name="custom_temp.j2", use_custom_template=True, template_config={"custom_template_dir": "./"}, # noqa
        dashboard_settings=manager.config_values, 
        inputs=manager.render_form_groups(), 
        outputs=manager.render_outputs(),
        custom_value_1="Yolo Man", # if you want to pass custom values to template  # noqa
        custom_value_2="Its all Good" # if you want to pass custom values to template # noqa
    ).render()

if __name__ == "__main__":
    app.run(debug=True)
