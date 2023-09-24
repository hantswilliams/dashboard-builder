from flask import Flask, render_template_string, request
from matplotlib.figure import Figure

#### For local dev testing....//otherwise turn off - comment out below ###
import os 
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
##########################################################################

from dashboard_builder import get_dashboard_template  # noqa: E402
from dashboard_builder.config import Config # noqa: E402
from dashboard_builder.components.outputs import OutputChart_Matplotlib # noqa: E501, E402
from dashboard_builder.components.managers import ComponentManager # noqa: E402, E501

app = Flask(__name__)

dashboard_settings = Config(
    footer_text="Built by Hants Williams, PhD, RN - Clinical Assistant Professor - Stony Brook University, School of Health Professions - Applied Health Informatics" # noqa: E501
    )

@app.route('/', methods=['GET', 'POST'])
def index():

    manager = ComponentManager(request)

    # Generate the figure **without using pyplot**.
    fig = Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot()
    ax.plot([1, 2, 3])

    output12 = OutputChart_Matplotlib(fig)
    manager.register_outputs(output12)

    return render_template_string(
        get_dashboard_template('base'),
        output_components=manager.render_outputs(),
        settings=dashboard_settings
    )

if __name__ == '__main__':
    app.run(debug=True)