from nb_offline_convert import OfflineHTMLExporter, OfflineWebPDFExporter


def convert_notebook(nb_path: str) -> None:

    outfile = nb_path.split(".")[0]

    converter = OfflineHTMLExporter()

    out, _ = converter.from_filename(nb_path)
    with open(outfile + ".html", "w") as f:
        f.write(out)

    pdf_converter = OfflineWebPDFExporter()
    out, _ = pdf_converter.from_filename(nb_path)
    with open(outfile + ".pdf", "wb") as f:
        f.write(out)


if __name__ == "__main__":
    convert_notebook("bqplot.ipynb")
