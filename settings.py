from weasyprint import HTML, CSS
from datetime import datetime

OUTPUT_FILENAME = f"output-{datetime.now().strftime('%d-%b-%Y')}"
TEMPLATE_HTML_PATH = "./invoice_template_002.html"

TEMPLATE_CSS = [
    CSS("./invoice_template_002.css"),
    CSS("https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css" ),
    CSS("https://maxcdn.bootstrapcdn.com/font-awesome/4.3.0/css/font-awesome.min.css" )
]

def get_context_data(context_json:dict)->dict:
    """This function manipulates the context you import from data.json"""
    context_json['issueDate'] = datetime.strptime(context_json['issueDate'], '%d-%m-%Y').strftime('%d-%m-%Y')
    context_json['dueDate'] = datetime.strptime(context_json['dueDate'], '%d-%m-%Y').strftime('%d-%m-%Y')
    context_json['invoiceDate'] = datetime.strptime(context_json['issueDate'], '%d-%m-%Y').strftime('%B')
    return context_json