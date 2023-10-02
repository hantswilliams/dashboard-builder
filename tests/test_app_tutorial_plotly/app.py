from flask import Flask, request
import plotly.express as px
import pandas as pd

##########################################################################
#### For local dev testing....//otherwise turn off - comment out below ###
import os # noqa
import sys # noqa
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
##########################################################################

from dashboard_builder import ComponentManager, DashboardOutput # noqa

app = Flask(__name__)

df = pd.DataFrame({
    'condition': ['Rheumatoid arthritis', 'Osteoarthritis', 'Osteoporosis', 'Fibromyalgia'], # noqa
    'frequency': [10, 15, 8, 7]
})

@app.route('/', methods=['GET', 'POST'])
def index():

    index_manager = ComponentManager(request)

    input_group = ComponentManager.create_input_group(
        manager_instance=index_manager,
        inputs=[
            {
                'type': 'dropdown',
                'name': 'condition_selection',
                'label': 'Select a condition:',
                'values': (df, 'condition')
            }
        ]
    )

    user_selected_1 = input_group.get_input('condition_selection').value

    selected_condition = df['condition'] == user_selected_1 if user_selected_1 != 'Select All' else None # noqa
    colors = ['Selected' if cond else 'Not Selected' for cond in selected_condition] or ['Not Selected'] * len(df) # noqa

    fig = px.bar(
        df,
        x='condition',
        y='frequency',
        color=colors,
        color_discrete_map={"Not Selected": "#A0AEC0", "Selected": "#48BB78"}  
    )

    ComponentManager.create_output_group(
        manager_instance=index_manager,
        outputs=[
            {
                'type': 'text',
                'content': f"Selected conditions From Form 1: {user_selected_1}"
            },
            {
                'type': 'chart_plotly',
                'content': fig
            }
        ]
    )

    return DashboardOutput(manager=index_manager).render()

if __name__ == "__main__":
    app.run(debug=True)
