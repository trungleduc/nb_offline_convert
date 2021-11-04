from nbconvert import WebPDFExporter
from .tools import OfflineMixing


class OfflineWebPDFExporter(OfflineMixing, WebPDFExporter):

    template_name = "webpdf_offline"

    def from_notebook_node(self, nb, resources=None, **kw):

        resources["offline_module_path"] = self.offline_module_path
        return super().from_notebook_node(nb, resources, **kw)
