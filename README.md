# Dashboard Builder

[![Ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
![Ruff Linting](https://github.com/hantswilliams/dashboard-builder/actions/workflows/ruff.yml/badge.svg)
![Google Doc Strings](https://img.shields.io/badge/Doc_Strings-Google-blue)
![Truffle Hog](https://github.com/hantswilliams/dashboard-builder/actions/workflows/trufflehog.yml/badge.svg)
[![Lisence: apache-2](https://img.shields.io/badge/Lisence:-Apache%202-red)](https://github.com/apache/.github/blob/main/LICENSE)

**[Documentation](https://dashboardbuilder.appliedhealthinformatics.com/)**

The `dashboard-builder` is a Python package designed to help you create interactive web dashboards with minimal effort, while still giving you *full access* to the underlining web framework supporting it - which is [Flask](https://flask.palletsprojects.com/). So whether you're looking to visualize datasets, create dynamic reports, or provide interactive analytics, this library streamlines the process, letting you focus on the data and logic, while it takes care of the presentation.

Our intended audience for this tool are python developers or data scientists that needs direct access to the web framework (e.g., [Flask](https://flask.palletsprojects.com/)) because of large amounts of custom code or required functionality, but still want a simple way of creating dashboards, similar to [Streamlit](https://streamlit.io/), [Dash](https://plotly.com/dash/) or [Shiny](https://shiny.posit.co/py/) - which make it harder to configure or customize the web framework. Flask is one of the most un-oppinionated web frameworks for python, which makes it a great choice.

##  **Positioning of Dashboard Builder in the Data Visualization Ecosystem**

In the vast landscape of data visualization tools, Dashboard Builder has carved out a unique and essential space for developers and data professionals. Dashboard Builder is for those who seek the balance between flexibility and ease-of-use, offering a middle-ground solution that doesn't compromise on power or versatility. Here's how it fits in:

1. **Starting From Scratch: Web Frameworks**  
   At one end of the spectrum, there are the barebone web frameworks like Flask, Django, or FastAPI. These frameworks provide enormous flexibility, allowing developers to build almost anything they envision. However, this often comes at the cost of starting from scratch. For many, the complexity of setting up, designing, and integrating multiple components is a hurdle, especially when the primary goal is to visualize and interact with data efficiently.

2. **High-level Visualization Tools: Tableau and Power BI**  
   On the opposite end, there are high-level visualization platforms like Tableau or Power BI. These tools empower users to create dashboards by simply dragging and dropping. But this ease of use can come with limitations. Custom visualizations or interactions might not be feasible, and these platforms can come with hefty price tags.

3. **Middle-Ground Tools: Shiny, Streamlit, Dash, and others**  
   Somewhere in between, tools like Shiny, Streamlit, Dash, and Gradio have emerged. They offer Python or R developers the ability to quickly create interactive web applications with minimal web development. However, they often abstract away too much of the underlying structure. This abstraction can limit developers from customizing or extending their apps in ways not natively supported by these platforms.

4. **Dashboard Builder: The Goldilocks Zone**  
   This is where Dashboard Builder shines. It occupies what we like to call the "Goldilocks Zone." It's not as raw and challenging as starting with pure web frameworks, yet it doesn't confine you within rigid structures like high-level tools. At the same time, it offers more control and flexibility than middle-ground tools. With Dashboard Builder, developers retain the ability to modify and customize components to their needs, integrating various visualization libraries and web components. Yet, they don't have to grapple with the foundational setup, making it easier and faster to get started.

## **Key Features**: 

### Native Visualizations with Familiar Tools:
Dashboard Builder empowers users to craft visuals using the full functionality of industry-standard libraries like *Matplotlib*, *Plotly*, and *Altair*. This means no compromises, no curbed features—just pure, unadulterated visual storytelling as these libraries intended.

### *No coding for HTML, CSS, or JS* 
Once you've created your visualization, there's typically the daunting task of embedding it within a web interface, which requires wrangling with HTML, CSS, or even JavaScript. The dashboard builder removes this step, letting you focus solely on Python. With just your Python skills, you can craft a web-responsive, interactive, and visually appealing dashboard. But if you need to, you can still access the HTML, CSS, and JS to customize the dashboard to your needs.

### Modern *Styling* with Tailwind: 
Leveraging the power of Tailwind CSS, Dashboard Builder offers dynamic and mobile-responsive layouts that ensure your visuals look vibrant and engaging across all devices. From widescreen monitors to compact mobile views, your dashboards will always adapt gracefully and retain their modern aesthetic appeal.

### Growing Component Library: 
- *Input Elements*: 
    - Single select 
    - Radio button 
    - Slider
    - Free text
    
- *Output Elements*: 
    - Visualizations
        - Altair 
        - Matplotlib 
        - Plotly
    - Markdown 
    - Free text 
    - Images
    - Text
    - Markdown

- *Container Related Elements*:
    - Column 
    - Expander 

- *Style Themes*: 
    - Default (light)
    - Dark 
    - Pink
    - Blue
    - Red
    - Yellow
    - Green

- Default and custom templates 
    - Currently have two default templates to choose between for a dashboard page: 
        - `base`: contains a side-bar (on left hand side for placing interactive widgets) and a main output view
        - `base_nosidebar`: contains a main output view only, no side bar; helpful for view-only dashboards with no need to interactivity
    - Custom Templates 
        - You can create your own custom template and load it in. Generally speaking, you can make the template look however you want. 
        - The default base template that we use, that you can modify however you want is [found here](https://github.com/hantswilliams/dashboard-builder/blob/main/dashboard_builder/dashboard_templates/base.j2)
        - You can then then set the custom folder where the template exists with the `dashboard_builder.config` parameter, and then call the `get_dashboard_template_custom` function to use your own template!  


--- 

## **Example Dashboards**

1. Complex example of Hospital and Centers for Medicare and Medicaid (CMS) Data for Long Island, New York. It is deployed via GCP Cloud Run, [please click here](https://dashboard-builder-cms-longisland-ua432tkhwq-uc.a.run.app/). The associated github source code for this repo can found here [https://github.com/hantswilliams/dashboard-builder-cms-longisland](https://github.com/hantswilliams/dashboard-builder-cms-longisland). 

## To do: 
- [ ] Add more output visualization components that include:
    - Folium
    - GGPlot
    - Bokeh
    - Seaborn
- [ ] Add more input components that might include: 
    - Date picker
    - File upload
    - Checkbox
    - Multi-select
    - Color picker
    - Number input
- [x] Address matplotlib issue for rendering on web framework
- [x] Add initial input components
- [x] Add initial output components
- [x] Create test files 
- [x] Add github actions for linting and secret checks
- [x] Create build script 
- [x] Create at least one basic 'base' template for the dashboard view 
- [x] Incorporate some form of state management system 
- [x] Create a simple app examples
- [x] Update below markdown/readme, double check it to make sure aligns with API 
- [x] Create docusuraus documentation site 
- [ ] Create video tutorials 
---

---
