# Dashboard Builder (Version: Alpha)

The `dashboard-builder` is a Python package designed to help you create interactive web dashboards with minimal effort, while still giving you *full access* to the underlining web framework supporting it - which is [Flask](https://flask.palletsprojects.com/). So whether you're looking to visualize datasets, create dynamic reports, or provide interactive analytics, this library streamlines the process, letting you focus on the data and logic, while it takes care of the presentation.

Our intended audience for this tool are python developers or data scientists that needs direct access to the web framework (e.g., [Flask](https://flask.palletsprojects.com/)) because of large amounts of custom code or required functionality, but still want a simple way of creating dashboards, similar to [Streamlit](https://streamlit.io/), [Dash](https://plotly.com/dash/) or [Shiny](https://shiny.posit.co/py/) - which make it harder to configure or customize the web framework. Flask is one of the most un-oppinionated web frameworks for python, which makes it a great choice. 

## Features
- **Easy Integration**: Designed with simplicity in mind, integrate `dashboard-builder` into your existing Python projects in minutes.
- **Interactive Widgets**: From drop-downs to sliders, offer dynamic input options to users.
- **Customizable Layouts**: Control the layout and presentation of your dashboards.
- **Extendable with Custom Templates**: Need a unique look? Integrate your own templates easily.

!!! note "Alpha Release"
    Dashboard Builder is currently in Alpha and is not yet ready for production purposes. We are working hard to finalize unit and E2E testing. We expect to have a production ready release by November 1, 2023. Stay tuned.  

## Installation

To install `dashboard-builder`, you can use pip:

```bash 
pip install dashboard-builder
```

## Quick Start

After installation, you can quickly set up a basic dashboard:

```python title="app.py"
from dashboard_builder import ...

# Your code to create a dashboard
```

For more detailed guides, usage examples, and API reference, navigate to the respective sections in the documentation.

---

## Next Steps:

1. [**Getting Started**:](../docs/tutorials/getting-started.md) Learn the basics of setting up your first dashboard.
2. **Components**: Dive deep into the various components and widgets available.
3. **Layouts & Templates**: Understand how to customize and layout your dashboards.
4. **Advanced Topics**: Dive deeper into more advanced functionalities and custom integrations.

---

Feel free to reach out for support or suggest features on our [GitHub repository](https://github.com/your_github/dashboard-builder).

---


