from flask import Flask, render_template_string, request
import pandas as pd 

import matplotlib
matplotlib.use('Agg') # required for Flask to serve matplotlib images
import matplotlib.pyplot as plt # noqa 

#### For local dev testing....//otherwise turn off - comment out below ###
import os # noqa
import sys # noqa
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
##########################################################################

from dashboard_builder import get_dashboard_template #noqa 
from dashboard_builder.config import Config # noqa: E402
from dashboard_builder.components.managers import ComponentManager, FormGroup # noqa
from dashboard_builder.config import Config # noqa 
from dashboard_builder.components.inputs import InputDropdown # noqa 
from dashboard_builder.components.outputs import OutputChart_Matplotlib # noqa 

app = Flask(__name__)

########################################################################
# Create a simple DataFrame
df = pd.DataFrame({
    'condition': ['Flu', 'Cold', 'Chickenpox', 'Measles', 'Malaria', 
                'Ebola', 'Dengue', 'Cholera', 'Typhoid', 'Hepatitis', 
                'AIDS', 'Tuberculosis', 'COVID-19', 'Zika', 'Meningitis'],
    'condition_count': [10000, 12000, 3000, 4000, 5000, 200, 
                        2300, 400, 2200, 3000, 5000, 11000, 
                        14000, 800, 2500]
})
########################################################################

dashboard_settings = Config(
    footer_text="Condition Frequency Count Dashboard - Powered by Dashboard Builder"
    )

@app.route('/', methods=['GET', 'POST'])
def index():

    manager = ComponentManager(request)

    # # Creating our form group
    # form_group_one = FormGroup(
    #     action_url='/',
    #     markdown_top="""### Select a Specific Condition""", 
    #     markdown_bottom="""*Use this section to filter by a specific condition.*""") 
    
    # # Creating our first input component, and then regstering it othe form group 
    # input_dropdown = InputDropdown(
    #     name='condition_selection', 
    #     label='Select a condition:', 
    #     values=(df, 'condition')) 

    # form_group_one.add_inputs(input_dropdown)
    
    # ########################################################################
    # # Registering our input and form group to the manager 
    # manager.register_inputs(input_dropdown)
    # manager.register_form_groups(form_group_one)

    # # User selected value
    # user_selected = input_dropdown.value


    # Use the new create_form_group method
    form_group_one = ComponentManager.create_form_group(
        manager_instance=manager,
        action_url='/',
        markdown_top="""### Form Group 1""", 
        markdown_bottom="""*Use this section to filter by a specific condition.*""",
        inputs=[
            {
                'type': 'dropdown',
                'name': 'condition_selection',
                'label': 'Select a condition:',
                'values': (df, 'condition')
            },
            {
                'type': 'dropdown',
                'name': 'condition_selection_2',
                'label': 'Select a condition:',
                'values': (df, 'condition')
            }
        ]
    )

    # User selected value
    user_selected = form_group_one.get_input('condition_selection').value  

    ########################################################################
    # Create filter DF based on user value
    if user_selected and user_selected != 'Select All':
        output_df = df[df['condition'] == user_selected]
    else:
        output_df = df


    ########################################################################
    # Create matplotlib chart
    fig, ax = plt.subplots(figsize=(10, 7))

    main_color = '#1f75fe'  
    highlight_color = '#ee204d' 

    ax.bar(df['condition'], df['condition_count'], color=main_color, alpha=0.7, label='All Conditions')  # noqa 
    ax.bar(output_df['condition'], output_df['condition_count'], color=highlight_color, alpha=0.9, label='Selected Condition')  # noqa
    ax.axhline(y=df['condition_count'].mean(), color='red', linestyle='--', label=f'Mean: ${(df["condition_count"].mean()).round(2):,}')  # noqa

    # Fonts and rotations for labels
    ax.set_xticklabels(df['condition'], rotation=70, ha='right', fontsize=10)
    ax.set_title('Condition Counts', fontsize=16, fontweight='bold', pad=20) 
    ax.set_xlabel('Condition Name', fontsize=14, labelpad=15)
    ax.set_ylabel('Condition Count', fontsize=14, labelpad=15)

    fig.tight_layout()


    # Register the outputs 
    output_1 = OutputChart_Matplotlib(fig)
    manager.register_outputs(output_1)


    ########################################################################
    return render_template_string(
        get_dashboard_template('base'),
        settings=dashboard_settings,
        form_groups=manager.render_form_groups(), 
        output_components=manager.render_outputs()
    )

if __name__ == "__main__":
    app.run(debug=True)
