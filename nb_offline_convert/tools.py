import os
import re
from typing import Dict as TypeDict
import sys
from genericpath import isdir
from jupyter_core.paths import jupyter_path


def get_template_path(*kw) -> str:
    return os.path.join(
        sys.prefix,
        "share",
        "jupyter",
        "nbconvert",
        "templates",
        "lab_offline",
        *kw,
    )


def patch_html_config(cdn: str, static_path: str) -> None:

    embed_path = os.path.join(static_path, "embed-amd.js")

    with open(embed_path, "r") as f:
        content: str = f.read()
    with open(embed_path, "w") as f:
        pattern = fr"{cdn}\/@jupyter-widgets\/html-manager@(.*?)\/dist\/"
        new_content = re.sub(pattern, static_path, content)
        f.write(new_content)


def get_extention_path() -> TypeDict[str, str]:
    ret = {}
    for base in jupyter_path():
        extensions_path = os.path.join(base, "nbextensions")
        if not isdir(extensions_path):
            continue
        subdir = [d for d in os.scandir(extensions_path) if d.is_dir()]
        for ex_path in subdir:
            files = [f for f in os.scandir(ex_path) if f.is_file()]
            for file in files:
                if file.name == "index.js":
                    module = ex_path.name
                else:
                    module = os.path.splitext(file.name)[0]

                ret[module] = file.path

    return ret



