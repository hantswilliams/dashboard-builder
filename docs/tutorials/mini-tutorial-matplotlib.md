# Flask Dashboard Mini-Tutorial: with **Matplotlib**

In this tutorial, we will walk you through the steps to build a dashboard application using Flask and our custom `dashboard_builder`. You'll start by creating a simple Flask application and then level it up by integrating the powerful dashboard builder for a more interactive and informative web interface.

!!! note "Some Flask knowledge is recommended!"
    Dashboard Builder is dependent on Flask. If you have not worked with Flask before, we recommend that you briefly familiarize yourself with the Flask web development framework by reading the [official documentation](https://flask.palletsprojects.com/). A great tutorial or introduction to Flask is also the [The Flask Mega Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) by Miguel Bringber

!!! note "Some Matplotlib knowledge is recommended!"
    The visualization components in this example use Matplotlib. If you are unfamiliar with Matplotlib, it's advisable to delve into the [official documentation](https://matplotlib.org/stable/contents.html). For a comprehensive introduction, consider checking out the tutorials available on the [Matplotlib website](https://matplotlib.org/stable/tutorials/index.html).


## **Part A: Setting up a Simple Flask App**

Before diving into the dashboard, let's set up a basic Flask application.

### Prerequisites
1. Make sure you have Flask installed. If not, you can install it via pip:
```bash
pip install Flask
```

### Creating the Flask App:

1. Create a new Python script and name it, say, `app.py`.
2. Copy and paste the following code into `app.py`:

``` py title="app.py"
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True)
```

3. Run your script:
```bash
python app.py
```

4. Visit `http://localhost:5000/` in your browser, and you should see the message "Hello, World!".

Great! You've just set up a simple Flask application. Now, let's take it up a notch and integrate the dashboard.

## **Part B: Integrating the Dashboard Builder**

The `dashboard_builder` will allow us to create dynamic dashboards with ease. It abstracts the process of setting up input and output components.

### 1. Prerequisites
For this tutorial, we are going to create and use a `create_plot` function that lives in a `example_matplot.py` python module, and a pandas `df` that is generated from a `example_data.py` module. These pieces of code are not dashboard builder specific, they are just generic code that we would otherwise write or use to create data in pandas, or create a plot in matplotlib. For the `example_matplot.py` module, in the same working directory you are in, create a new python file called `example_matplot.py` and copy and paste the following code:

!!! note "Matploblib writing in web servers!!"
    When using matplotlib in a server environment we need to set a specific argument after loading in matplotlib: `matplotlib.use('Agg')`. This step is required for rendering any matplotlib visualizations in a flask-based web application. The `Agg` argument is used for file writing in our Flask app. For more information, please visit the matplotlib [documentation on backends](https://matplotlib.org/stable/users/explain/figure/backends.html) to see all that is possible. 

``` py title="example_matplot.py"

import matplotlib
matplotlib.use('Agg') # required for Flask to serve matplotlib images
import matplotlib.pyplot as plt # noqa 

def create_plot(df, user_selected_1):

    ########################################################################
    # Create filter DF based on user value
    if user_selected_1 and user_selected_1 != 'Select All':
        output_df = df[df['condition'] == user_selected_1]
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

    return fig

```

Similarly, for the `example_data.py` module, create a new python file called `example_data.py` and copy and paste the following code:

``` py title="example_data.py"

import pandas as pd 

df = pd.DataFrame({
    'condition': ['Flu', 'Cold', 'Chickenpox', 'Measles', 'Malaria', 
                'Ebola', 'Dengue', 'Cholera', 'Typhoid', 'Hepatitis', 
                'AIDS', 'Tuberculosis', 'COVID-19', 'Zika', 'Meningitis'],
    'condition_count': [10000, 12000, 3000, 4000, 5000, 200, 
                        2300, 400, 2200, 3000, 5000, 11000, 
                        14000, 800, 2500]
})

```


### 2. Modifying the Flask App for the Dashboard

#### 2a. Modules
In `app.py`, import the necessary modules and functions:

```python
from flask import Flask, request
from matplot import create_plot
from data import df
from dashboard_builder import ComponentManager, DashboardOutput
```

#### 2b. Index Update
Update the `index()` function to integrate the dashboard components:

```python
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

    fig = create_plot(df, input_group.get_input('condition_selection').value)

    ComponentManager.create_output_group(
        manager_instance=index_manager,
        outputs=[
            {
                'type': 'chart_matplotlib',
                'content': fig
            }
        ]
    )

    return DashboardOutput(manager=index_manager).render()
```

#### 2c. Final Code 
Save your changes. 

Your `app.py` should now look like this:

``` py title="app.py"
from flask import Flask, request
from example_matplot import create_plot
from example_data import df
from dashboard_builder import ComponentManager, DashboardOutput # noqa

app = Flask(__name__)

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

    fig = create_plot(df, input_group.get_input('condition_selection').value)

    ComponentManager.create_output_group(
        manager_instance=index_manager,
        outputs=[
            {
                'type': 'chart_matplotlib',
                'content': fig
            }
        ]
    )

    return DashboardOutput(manager=index_manager).render()

if __name__ == "__main__":
    app.run(debug=True)
```

And run the script again:
```bash
python app.py
```

Visit `http://localhost:5000/` again. Now, instead of a simple message, you should see a dynamic dashboard allowing you to select a condition and view a corresponding plot.

## Conclusion

With Flask's flexibility combined with the ease-of-use provided by the `dashboard_builder`, you can quickly set up dashboards with interactive components. This approach allows for a modular design where you can easily enhance, modify, or scale your dashboard applications as needed. Happy coding!