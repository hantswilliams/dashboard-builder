from flask import Flask, render_template_string, request

import matplotlib
matplotlib.use('Agg') # required for Flask to serve matplotlib images
import matplotlib.pyplot as plt # noqa: E402 need to import after matplotlib.use('Agg')
from matplotlib.figure import Figure # noqa: E402



#### For local dev testing....//otherwise turn off - comment out below ###
import os # noqa
import sys # noqa 
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
##########################################################################

from dashboard_builder import get_dashboard_template, get_dashboard_template_custom  # noqa: E402, E501, F401
from dashboard_builder.config import Config # noqa: E402
from dashboard_builder.components.outputs import OutputChart_Matplotlib # noqa: E501, E402
from dashboard_builder.managers import ComponentManager # noqa: E402, E501

app = Flask(__name__)

dashboard_settings = Config(
    custom_template_dir="custom_templates_app4",
    footer_text="Built by Hants Williams, PhD, RN - Clinical Assistant Professor - Stony Brook University, School of Health Professions - Applied Health Informatics" # noqa: E501
    )

@app.route('/', methods=['GET', 'POST'])
def index():

    manager = ComponentManager(request)

    # Generate the figure **without using pyplot**.
    fig = Figure(figsize=(5, 4), dpi=100)
    ax = fig.add_subplot()
    ax.plot([1, 2, 3])

    manager.register_outputs(OutputChart_Matplotlib(fig))

    print('Page Manager Contents from /: ', fig)

    return render_template_string(
        # get_dashboard_template('base'),
        get_dashboard_template_custom('my_custom_template.j2', dashboard_settings),
        output_components=manager.render_outputs(),
        settings=dashboard_settings
    )

@app.route('/page', methods=['GET', 'POST'])
def index2():

    manager = ComponentManager(request)

    # Generate the figure **without using pyplot**.
    fig, ax = plt.subplots()

    fruits = ['apple', 'blueberry', 'cherry', 'orange']
    counts = [40, 100, 30, 55]
    bar_labels = ['red', 'blue', '_red', 'orange']
    bar_colors = ['tab:red', 'tab:blue', 'tab:red', 'tab:orange']

    ax.bar(fruits, counts, label=bar_labels, color=bar_colors)

    ax.set_ylabel('fruit supply')
    ax.set_title('Fruit supply by kind and color')
    ax.legend(title='Fruit color')

    manager.register_outputs(OutputChart_Matplotlib(fig))

    ## print the contents of the manager in the terminal
    print('Page Manager Contents from /page: ', fig)

    return render_template_string(
        # get_dashboard_template('base'),
        get_dashboard_template_custom('my_custom_template.j2', dashboard_settings),
        output_components=manager.render_outputs(),
        settings=dashboard_settings
    )

if __name__ == '__main__':
    app.run(debug=True)