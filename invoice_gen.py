"""
This script consumes jinja based templates with CSS styling.
To change how it works, go to the settings.py file and make your changes there.

made by : https://github.com/Blankscreen-exe 
"""

from jinja2 import Template
import json
from settings import *

def render_template(template_file:str, context:dict, styles:list, output_filename:str)->str:
    """
    Render a Jinja template to PDF using WeasyPrint.

    Parameters:
    - template_file (str): The content of the Jinja HTML template.
    - context (dict): Context data to render in the template.
    - styles (list): List of stylesheets to apply to the generated PDF.
    - output_filename (str): Name for the output PDF file.

    Returns:
    - str: The filename of the generated PDF.

    This function takes a Jinja template, renders it with the provided context data, and generates a PDF.
    It uses WeasyPrint to convert the HTML content into a PDF, applying any provided stylesheets.
    The rendered HTML content can optionally be saved to a file by uncommenting lines inside the function.
    The output PDF filename is returned.
    """
    template = Template(template_file)
    rendered_html = template.render(context)

    html_file = f"{output_filename}.html"
    pdf_file = f"{output_filename}.pdf"

    # REVIEW: Enable this to Save the rendered HTML to a file
    with open(html_file, 'w') as file:
        file.write(rendered_html)

    # Convert HTML to PDF using WeasyPrint
    HTML(html_file).write_pdf(pdf_file, stylesheets=styles)

    return pdf_file

# Load context data
context_data = {}
with open("./data.json") as data:
    context_data = get_context_data(json.load(data))
    
# load Jinja template
template_html = ""
with open(TEMPLATE_HTML_PATH) as template:
    template_html = template.read()

# Render the template and generate the PDF
pdf_filename = render_template(template_html, context_data, TEMPLATE_CSS, OUTPUT_FILENAME)
print(f"PDF generated: {pdf_filename}")
