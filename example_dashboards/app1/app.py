from flask import Flask, render_template_string, request
import pandas as pd

#### For local dev testing....//otherwise turn off - comment out below ###
import os 
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
##########################################################################

from dashboard_builder import get_dashboard_template # noqa: E402
from dashboard_builder.config import Config # noqa: E402
from dashboard_builder.components.inputs import InputDropdown  # noqa: E402
from dashboard_builder.components.outputs import OutputText, OutputTable_HTML, OutputImage, OutputMarkdown # noqa: E501, E402
from dashboard_builder.components.managers import ComponentManager, FormGroup # noqa: E501, E402

app = Flask(__name__)

dashboard_settings = Config(
    footer_text="My Custom Footer for the Dashboard - Powered by Dashboard Builder"
    )

## load in json to dataframe, some fake data from dummyjson.com
df = pd.read_json('https://dummyjson.com/products')
df = pd.concat([df.drop(['products'], axis=1), df['products'].apply(pd.Series)], axis=1)

@app.route('/', methods=['GET', 'POST'])
def index():

    # Step 1: Initialize the component manager for this request/endpoint
    manager = ComponentManager(request)

    # Step 2: Registering and capturing inputs for this request
    form_group_a = FormGroup(action_url='/', markdown_top="""### Group A""", markdown_bottom="""*Use this section to filter by a specific brand.*""") # noqa: E501 we are first creating a form group 
    input1_dropdown = InputDropdown(name='brand_selection', label='Select a brand:', values=(df, 'brand')) # noqa: E501 // then we are creating an input component, in this case a dropdown //  
    form_group_a.add_inputs(input1_dropdown) # noqa: E501 // then we are adding the input component to the form group
    manager.register_inputs(input1_dropdown) # noqa: E501 // then we are registering the input component to the manager
    manager.register_form_groups(form_group_a) # noqa: E501 // then we are registering the form group to the manager

    # Step 3: manipulating the data based on the input components
    modeded_df = df.copy()
    if input1_dropdown.value != 'Select All':
        modeded_df = modeded_df[modeded_df['brand'] == input1_dropdown.value]

    image_value = modeded_df.iloc[0, 12]
    print(image_value)

    # Step 4: Create the outputs for this request
    output_markdown = OutputMarkdown("""### Example Header with Markdown""")
    output_image = OutputImage(image_value)
    output_text = OutputText(f"Number of rows returned: {modeded_df.shape[0]}")
    output_table = OutputTable_HTML(modeded_df.to_dict(orient='records'))

    # Step 5: Register the outputs to the manager
    manager.register_outputs(output_markdown, output_image, output_text, output_table)

    # Step 6: Render the template with the inputs and outputs
    return render_template_string(
        get_dashboard_template('base'),
        form_groups=manager.render_form_groups(), 
        output_components=manager.render_outputs(),
        settings=dashboard_settings
    )

if __name__ == '__main__':
    app.run(debug=True, port=5000)


