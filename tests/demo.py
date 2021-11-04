from nb_offline_convert import OfflineHTMLExpoter
import sys

def convert_notebook(nb_path: str) -> None:

    write_format = 'w'
    outfile = nb_path.split('.')[0] + '.html'

    converter = OfflineHTMLExpoter()

    out, _ = converter.from_filename(nb_path)
    with open(outfile, write_format) as f:
        f.write(out)
    print(sys.prefix)

if __name__ == '__main__':
    convert_notebook('bqplot.ipynb')
