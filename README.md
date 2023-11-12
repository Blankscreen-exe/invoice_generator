# Invoice Generator

This is an invoice generator built with `Jinja2` and `WeasyPrint`. 

You can use this to make a pdf and an html invoice. Before you can use this script, you will need to customize some settings beforehand.

## Installation

I recommend that you create a virtual environment first, before installing the dependencies.

```shell
pip3 install -r requirements.txt
```

> **NOTE**: WeasyPrint is known to have problems in Windows OS which can easily be fixed [like this](https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#missing-library).

## Usage

The templates(HTML/CSS) are completely upto you to customize. These templates are found in the project root directory by default. The starter template can be found as `invoice_template_001.html`.Similarly, the associated style file can be found as `invoice_template_001.css`.

To apply bootstrap styling and loading other CDNs you can append to the `TEMPLATE_CSS` variable which can be found inside `settings.py`. This is an array of all the `css` which is required to render the template. You should load your custom `css` file in this array as well.

`data.json` contains the context data which will be renderd into the template. In case you want to perform calculations, you can wither engineer those formulas directly into the `html` template or in the `get_context_data()` function which can be found inside `settings.py`.

To run the script, make sure all of the above is present inside the project root directory and run this command:

```shell
python3 invoice_gen.py
```

If all goes as planned, you will see a message in the terminal like this:

```shell
PDF generated: output-12-Nov-2023.pdf
```

## Preview

![preview](./docs/preview.png)