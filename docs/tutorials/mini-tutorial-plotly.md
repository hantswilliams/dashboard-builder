# Flask Dashboard Mini-Tutorial: with **Plotly**

In this tutorial, we will guide you through crafting a dashboard application using **Flask** integrated with **Plotly** for enhanced visualizations. By using our custom `dashboard_builder`, you will be able to seamlessly combine Flask's flexibility with the visualization prowess of Plotly.

!!! note "Some Flask knowledge is recommended!"
    Dashboard Builder is dependent on Flask. If you have not worked with Flask before, we recommend that you briefly familiarize yourself with the Flask web development framework by reading the [official documentation](https://flask.palletsprojects.com/). A great tutorial or introduction to Flask is also the [The Flask Mega Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) by Miguel Bringber

!!! note "Some Plotly knowledge is recommended!"
    The visualization components in this example use Plotly. If you are unfamiliar with Plotly, it's advisable to delve into the [official documentation](https://plotly.com/python/). For a comprehensive introduction, consider checking out the tutorials available on the Plotly website.


## **Part A: Setting up a Simple Flask App**

Starting with a basic Flask foundation, we'll then integrate our dashboard for more advanced features.

### Prerequisites
1. Ensure Flask and Plotly are installed. If not, do so using pip:
```bash
pip install Flask plotly
```

### Creating the Flask App:

1. Create a Python script, for instance, `app.py`.
2. Paste the following into `app.py`:

``` py title="app.py"
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True)
```

3. Launch the script:
```bash
python app.py
```

4. Access `http://localhost:5000/` in a browser. The message "Hello, World!" should greet you.

You have now established a fundamental Flask application. Let's elevate it with the dashboard.

## **Part B: Introducing Plotly for Enhanced Visualizations**

The `dashboard_builder` facilitates the creation of dynamic dashboards. For this part, we'll lean on Plotly for chart visualizations.

#### 1. Modules
Add the necessary modules and functions at the start of `app.py`:

``` py title="app.py"
from flask import Flask, request
import plotly.express as px
import pandas as pd
from dashboard_builder import ComponentManager, DashboardOutput
```

#### 2. Data
Let's define some example data for our dashboard:

```python
df = pd.DataFrame({
    'condition': ['Rheumatoid arthritis', 'Osteoarthritis', 'Osteoporosis', 'Fibromyalgia'], # noqa
    'frequency': [10, 15, 8, 7]
})
```

Certainly! Let's segment the `index()` function's code into the three distinct sections as per your request.

---

#### 3. Index Update

To achieve the desired dashboard, you'll need to revisit and update the `index()` function. It can be logically divided into three sections:

##### 3.1. Initializing Index Manager and Input Group

The first segment involves setting up the Index Manager, which aids in component management. You'll also craft an input group for users to make selections.

```python
@app.route('/', methods=['GET', 'POST'])
def index():
    # Initialize the Index Manager with the current request.
    index_manager = ComponentManager(request)

    # Define the Input Group, allowing users to choose a medical condition.
    input_group = ComponentManager.create_input_group(
        manager_instance=index_manager,
        inputs=[
            ComponentManager.Inputs.dropdown('condition_selection', 'Select a condition: ', (df, 'condition'))
        ]
    )
```

##### 3.2. Crafting the Plotly Visualization

With the input data procured, you'll now configure the Plotly visualization. This segment deciphers the user's selection, determines coloring conditions, and structures the chart.

```python
    # Extract the user's choice from the input group.
    user_selected_1 = input_group.get_input('condition_selection').value

    # Depending on the user's choice, designate rows as 'Selected' or 'Not Selected'.
    selected_condition = df['condition'] == user_selected_1 if user_selected_1 != 'Select All' else None 

    if selected_condition is not None:
        colors = ['Selected' if cond else 'Not Selected' for cond in selected_condition]
    else:
        colors = ['Not Selected'] * len(df)

    # Construct a Plotly bar chart visualization.
    fig = px.bar(
        df,
        x='condition',
        y='frequency',
        color=colors,
        color_discrete_map={"Not Selected": "#A0AEC0", "Selected": "#48BB78"}
    )
```

##### 3.3. Creating the Output Group

In this final segment, you'll assemble and render the Output Group. This group will exhibit both text and the chart visualization, presenting users with the completed dashboard.

```python
    # Define the Output Group containing text and the Plotly chart.
    ComponentManager.create_output_group(
        manager_instance=index_manager,
        outputs=[
            ComponentManager.Outputs.text(f"Value selected: {user_selected_1}"),
            ComponentManager.Outputs.plotly(fig)
        ]
    )

    # Render and return the assembled dashboard.
    return DashboardOutput(manager=index_manager).render()
```


#### 4. Concluding Code
Save all changes.

The final `app.py` should resemble:

``` py title="app.py"

from flask import Flask, request
import plotly.express as px
import pandas as pd
from dashboard_builder import ComponentManager, DashboardOutput

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
            ComponentManager.Inputs.dropdown('condition_selection', 'Select a condition: ', (df, 'condition'))
        ]
    )

    user_selected_1 = input_group.get_input('condition_selection').value

    selected_condition = df['condition'] == user_selected_1 if user_selected_1 != 'Select All' else None # noqa

    if selected_condition is not None:
        colors = ['Selected' if cond else 'Not Selected' for cond in selected_condition]
    else:
        colors = ['Not Selected'] * len(df)

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
            ComponentManager.Outputs.text(f"Value selected: {user_selected_1}"),
            ComponentManager.Outputs.plotly(fig)
        ]
    )

    return DashboardOutput(manager=index_manager).render()

if __name__ == "__main__":
    app.run(debug=True)


```

Execute the script once more:
```bash
python app.py
```

Visiting `http://localhost:5000/` will now present a dynamic dashboard. This dashboard provides the ability to choose a condition and view a relevant Plotly graph.

## **Conclusion**

By combining Flask with Plotly and the `dashboard_builder`, the creation of interactive dashboards becomes intuitive. This modular approach is scalable, permitting enhancements or modifications as per requirement. Dive in and experiment further to craft your desired dashboards!