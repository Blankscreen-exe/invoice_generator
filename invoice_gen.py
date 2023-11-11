from jinja2 import Template
from weasyprint import HTML, CSS
import json
from datetime import datetime

def render_template(template_str, context, styles, output_filename):
    template = Template(template_str)
    rendered_html = template.render(context)

    html_file = f"{output_filename}.html"
    pdf_file = f"{output_filename}.pdf"

    # Save the rendered HTML to a file
    with open(html_file, 'w') as file:
        file.write(rendered_html)

    # Convert HTML to PDF using WeasyPrint
    HTML(html_file).write_pdf(pdf_file
        ,     
        stylesheets=styles,
    )

    return pdf_file

# Example context data
context_data = {}
with open("./data.json") as data:
    data = json.load(data)
    data['issueDate'] = datetime.strptime(data['issueDate'], '%d-%m-%Y').strftime('%d-%m-%Y')
    data['dueDate'] = datetime.strptime(data['dueDate'], '%d-%m-%Y').strftime('%d-%m-%Y')
    data['invoiceDate'] = datetime.strptime(data['issueDate'], '%d-%m-%Y').strftime('%B')
    
    context_data = data

# Example Jinja template
template_html = ""
with open("./invoice_template_002.html") as template:
    template_html = template.read()
template_css = ""
with open("./invoice_template_002.css") as styles:
    template_css = styles.read()
    
template_css = [
    CSS("./invoice_template_002.css"),
    CSS("https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css" ),
    CSS("https://maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css" )
]

# Replace the above example with your own HTML template and context data
output_filename = "generated_pdf"

# Render the template and generate the PDF
pdf_filename = render_template(template_html, context_data, template_css, output_filename)
print(f"PDF generated: {pdf_filename}")
