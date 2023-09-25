# components/outputs.py

from flask import render_template_string
import io
import base64
import json
from markdown import markdown
from ..utils import get_jinja_subtemplate

class OutputText:
    """
    Represents a text output component for a dashboard or view.
    This class facilitates rendering plain text content using a specified template.
    """
    def __init__(self, content):
        """
        Initialize a new instance of the OutputText class.

        Args:
            content (str): The text content to be rendered.
        """
        self.content = content

    def render(self):
        """
        Render the text content as an HTML string using the specified template.

        Returns:
            str: HTML representation of the text content.
        """
        return render_template_string(
            get_jinja_subtemplate("outputs/outputtext.j2"),
            content=self.content)

class OutputChart_Matplotlib:
    """
    Represents a chart output component for a dashboard or view.
    This class facilitates rendering Matplotlib plots in an HTML view.
    """
    def __init__(self, matplob_object):
        """
        Initialize a new instance of the OutputChart_Matplotlib class.

        Args:
            matplob_object: A Matplotlib figure or similar object that has 
                a 'savefig' method.
        """
        self.matplob_object = matplob_object

    def render(self):
        """
        Render the Matplotlib plot as an embedded image in an HTML string using the 
        specified template.

        The method performs the following steps:
        1. Converts the Matplotlib object to a figure.
        2. Saves the figure as an image to an in-memory bytes buffer.
        3. Encodes the bytes buffer to Base64.
        4. Renders the encoded image using a specified template.

        Returns:
            str: HTML representation of the embedded image chart.
        """
        # Create a bytes buffer for the image to save to
        buf = io.BytesIO()

        # Convert the plt object to a Figure, then save the figure to the buffer
        self.matplob_object.savefig(buf, format="png", bbox_inches='tight')
        buf.seek(0)

        # Convert bytes to a data URL (base64 encoding)
        encoded_bytes = base64.b64encode(buf.getvalue())
        data_url = "data:image/png;base64," + encoded_bytes.decode('utf8')

        buf.close()

        return render_template_string(
            get_jinja_subtemplate("outputs/outputchart_matplotlib.j2"),
            image=data_url)


class OutputChart_Altair:
    """
    Represents a chart output component for a dashboard or view using Altair.
    This class facilitates rendering Altair charts in an HTML view.
    """
    def __init__(self, altair_chart, chart_title, chart_id):
        """
        Initialize a new instance of the OutputChart_Altair class.

        Args:
            altair_chart: An Altair chart object.
            chart_title (str): The title for the Altair chart.
            chart_id (str): A unique identifier for the chart.
        """
        self.altair_chart = altair_chart
        self.chart_title = chart_title
        self.chart_id = chart_id

    def render(self):
        """
        Render the Altair chart as an embedded JSON in an HTML string using the 
        specified template.

        The method performs the following steps:
        1. Converts the Altair chart to a dictionary and then to a JSON string.
        2. Renders the JSON string using a specified template.

        Returns:
            str: HTML representation of the embedded Altair chart.
        """
        chart_json = json.dumps(self.altair_chart.to_dict())
        
        return render_template_string(
            get_jinja_subtemplate("outputs/outputchart_altair.j2"),
            chart_json=chart_json, chart_title = self.chart_title,
            chart_id=self.chart_id)


class OutputTable_HTML:
    """
    Represents a table output component for a dashboard or view using HTML.
    This class facilitates rendering tabular data in an HTML view.
    """
    def __init__(self, data):
        """
        Initialize a new instance of the OutputTable_HTML class.

        Args:
            data (list): A list of dictionaries representing the rows of the table. 
                         Each dictionary should have the same keys representing 
                         the columns.
        """
        self.data = data  # Assuming data is a list of dictionaries

    def render(self):
        """
        Render the tabular data as an HTML table using the specified template.

        Returns:
            str: HTML representation of the data in table format.
        """
        return render_template_string(
            get_jinja_subtemplate("outputs/outputtable_html.j2"),
            data=self.data)


class OutputImage:
    """
    Represents an image output component for a dashboard or view.
    This class facilitates rendering an image in an HTML view.
    """
    def __init__(self, src, alt=""):
        """
        Initialize a new instance of the OutputImage class.

        Args:
            src (str): The source URL or path of the image.
            alt (str, optional): The alternative text for the image (used for 
                                 accessibility purposes). Defaults to an 
                                 empty string.
        """
        self.src = src
        self.alt = alt

    def render(self):
        """
        Render the image as an HTML <img> element using the specified template.

        Returns:
            str: HTML representation of the image.
        """
        return render_template_string(
            get_jinja_subtemplate("outputs/outputimage.j2"),
            src=self.src, alt=self.alt)


class OutputMarkdown:
    """
    Represents a markdown output component for a dashboard or view.
    This class facilitates rendering markdown content in an HTML view.
    """
    def __init__(self, markdown_content):
        """
        Initialize a new instance of the OutputMarkdown class.

        Args:
            markdown_content (str): The markdown content to be rendered.
        """
        self.markdown_content = markdown_content

    def render(self):
        """
        Convert the markdown content to HTML and then render it 
        using the specified template.

        Returns:
            str: HTML representation of the markdown content.
        """
        html_content = markdown(self.markdown_content)    
        return render_template_string(
            get_jinja_subtemplate("outputs/outputmarkdown.j2"),
            content=html_content)