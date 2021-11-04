from nbconvert import HTMLExporter
from traitlets.traitlets import Dict
import sys
from .tools import get_extention_path, get_template_path


class OfflineHTMLExpoter(HTMLExporter):

    template_name = "lab_offline"
    mathjax_url = (
        get_template_path("static", "MathJax", "MathJax.js")
        + "?config=TeX-AMS_CHTML-full,Safe"
    )

    widget_renderer_url = get_template_path(
        "static",
        "@jupyter-widgets",
        "html-manager@0.20.0",
        "dist",
        "embed-amd.js",
    )
    offline_module_path = Dict(
        get_extention_path(), help="Path to offline js module"
    )

    def from_notebook_node(self, nb, resources=None, **kw):

        resources["offline_module_path"] = self.offline_module_path
        return super().from_notebook_node(nb, resources, **kw)
