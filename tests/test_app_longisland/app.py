from flask import Flask, request
import plotly.express as px
import pandas as pd
from helper_functions import process_data # noqa

##########################################################################
#### For local dev testing....//otherwise turn off - comment out below ###
import os # noqa
import sys # noqa
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
##########################################################################

from dashboard_builder import ComponentManager, DashboardOutput # noqa

app = Flask(__name__)

df = pd.read_csv('https://raw.githubusercontent.com/hantswilliams/dashboard-builder/main/tests/test_app_3/ny_suffolk_nassau.csv')

@app.route('/', methods=['GET', 'POST'])
def index():

    # Step 1: Initialize the component manager for this request/endpoint
    index_manager = ComponentManager(request)

    input_group_one = ComponentManager.create_input_group(
        manager_instance=index_manager,
        markdown_top='## From Group 1',
        inputs=[
            {
                'type': 'dropdown',
                'name': 'hospital_selection',
                'label': 'Select a condition:',
                'values': (df, 'Hospital Name')
            }
        ]
    )

    input_group_two = ComponentManager.create_input_group(
        manager_instance=index_manager,
        markdown_top='## From Group 2',
        inputs=[
            {
                'type': 'slider_categorical',
                'name': 'bed_selection',
                'label': 'Select a number of beds:',
                'categories' : ['Select All', 'hospitals < 100 beds', '100 beds >= hospitals < 300 beds', 'hospitals >= 300 beds'] # noqa
            }
        ]
    )

    intput_group_three = ComponentManager.create_input_group(
        manager_instance=index_manager,
        markdown_top='## From Group 3',
        inputs=[
            {
                'type': 'radio',
                'name': 'net_income_selection',
                'label': 'Select a net income:',
                'options': ['Positive', 'Negative']
            }
        ]
    )

    # Step 2: Process the data
    user_selected_1 = input_group_one.get_input('hospital_selection').value      
    user_selected_2 = input_group_two.get_input('bed_selection').value
    user_selected_3 = intput_group_three.get_input('net_income_selection').value

    table, fig = process_data(df, [user_selected_1, user_selected_2, user_selected_3]) # noqa


    # Step 3: Create the output group
    ComponentManager.create_output_group(
        manager_instance=index_manager,
        outputs=[
            {
                'type': 'markdown',
                'content': f"**Form 1**: {user_selected_1}; **Form 2**: {user_selected_2}; **Form 3**: {user_selected_3}" # noqa 
            },
            {
                'type': 'chart_matplotlib',
                'content': fig
            },
            {
                'type': 'table_html',
                'content': table
            }
        ]
    )


    return DashboardOutput(manager=index_manager).render()

if __name__ == '__main__':
    app.run(debug=True)