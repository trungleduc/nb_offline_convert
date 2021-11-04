from nbconvert import HTMLExporter
from .tools import OfflineMixing


class OfflineHTMLExpoter(OfflineMixing, HTMLExporter):

    template_name = "lab_offline"

    def from_notebook_node(self, nb, resources=None, **kw):
        resources["offline_module_path"] = self.offline_module_path
        return super().from_notebook_node(nb, resources, **kw)
