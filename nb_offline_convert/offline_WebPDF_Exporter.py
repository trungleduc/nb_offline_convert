
from nbconvert import HTMLExporter, WebPDFExporter
from traitlets.traitlets import Dict

from .tools import get_extention_path


class OfflineWebPDFExpoter(WebPDFExporter):

    template_name = 'lab-offline'

    offline_module_path = Dict(
        get_extention_path(), help='Path to offline js module')

    def from_notebook_node(self, nb, resources=None, **kw):

        resources['offline_module_path'] = self.offline_module_path
        return super().from_notebook_node(nb, resources, **kw)
