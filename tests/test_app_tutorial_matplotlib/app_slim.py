from flask import Flask, request
from example_matplot import create_plot
from example_data import df

##########################################################################
#### For local dev testing....//otherwise turn off - comment out below ###
import os # noqa
import sys # noqa
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
##########################################################################

from dashboard_builder import ComponentManager, DashboardOutput # noqa

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():

    index_manager = ComponentManager(request)

    index_manager.template_defaults(
        page_title="CMS 2019 Data",
        footer_text="Built by Hants Williams - Condition Frequency Count Dashboard - Powered by Dashboard Builder" # noqa
    )

    input_group = ComponentManager.create_input_group(
        manager_instance=index_manager,
        inputs=[
            ComponentManager.Inputs.dropdown('condition_selection', 'Select a condition: ', (df, 'condition')) # noqa
        ]
    )

    fig = create_plot(df, input_group.get_input('condition_selection').value)

    ComponentManager.create_output_group(
        manager_instance=index_manager,
        outputs=[
            ComponentManager.Outputs.matplotlib(fig)
        ]
    )

    return DashboardOutput(manager=index_manager).render()

if __name__ == "__main__":
    app.run(debug=True)




