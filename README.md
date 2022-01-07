# nb_offline_convert - An offline exporter for `nbconvert`

The normal `HTML` exporter of `nbconvert` creates the `HTML` files that will fetch resources (javascript and css files) from CDN, and the `WebPDF` exporter also depends on `HTML` exporter, so it's not possible to generate `HTML` of `PDF` files with widgets using `nbconvert` in an environement without internet connection.

This exporter allows `nbconvert` to export notebooks into `HTML` and `PDF` files that use all resources from the local machine by doing three steps:
- The `RequireJS` file content is injected directly into the generated `HTML`files.
- The `ipywidgets` javascript file (`embed-amd.js`), icons and fonts are bundled with `nb_offline_convert`. `embed-amd.js` is patched to fetch icons and fonts from local paths instead of CDN 
- The javascript files of widgets are configured to be fetched from the local notebook extension paths.

## Installation

`nb_offline_convert` can be installed from PyPI

```
pip install nb-offline-convert
```

## Usage

- Usage in CLI

```bash
# convert to html
jupyter nbconvert --to html-offline notebook-you-want-to-convert.ipynb
```
```bash
# convert to pdf
jupyter nbconvert --to webpdf-offline notebook-you-want-to-convert.ipynb
```

The default `Mathjax` option is `TeX-AMS_CHTML-full,Safe`, to change this option, pass `--OfflineHTMLExporter.mathjax_option` to the command line: 

```bash
# Use 'TeX-MML-AM_CHTML,Safe' option
jupyter nbconvert --to html-offline --OfflineHTMLExporter.mathjax_option=TeX-MML-AM_CHTML,Safe  notebook-you-want-to-convert.ipynb
```

- Usage in a script

```python
from nb_offline_convert import OfflineHTMLExporter, OfflineWebPDFExporter

# convert to html
html_converter = OfflineHTMLExporter()
content, _ = html_converter.from_filename("notebook-you-want-to-convert.ipynb")
with open("converted_file.html", "w") as f:
    f.write(content)
    
# convert to pdf
pdf_converter = OfflineWebPDFExporter()
content, _ = pdf_converter.from_filename("notebook-you-want-to-convert.ipynb")
with open("converted_file.pdf", "wb") as f:
    f.write(content)
```
Add `mathjax_option` parameter to the constructor of `OfflineHTMLExporter` or `OfflineWebPDFExporter` to modify the `Mathjax` option:

```python
html_converter = OfflineHTMLExporter(mathjax_option="TeX-AMS_CHTML-full,Safe")
```

## Development

install `nb_offline_convert` for development using:

```
git clone https://github.com/trungleduc/nb_offline_convert.git
cd nb_offline_convert
python -m pip install -e .
```
