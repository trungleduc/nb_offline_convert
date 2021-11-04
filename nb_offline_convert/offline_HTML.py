#############################################################
# Created on Thu Nov 04 2021                                #
# Copyright (c) 2021 Duc Trung Le (leductrungxf@gmail.com)  #
# Distributed under the terms of the MIT License            #
#############################################################


from nbconvert import HTMLExporter
from .tools import OfflineMixing


class OfflineHTMLExporter(OfflineMixing, HTMLExporter):

    template_name = "lab_offline"

    def from_notebook_node(self, nb, resources=None, **kw):
        resources["offline_module_path"] = self.offline_module_path
        return super().from_notebook_node(nb, resources, **kw)
