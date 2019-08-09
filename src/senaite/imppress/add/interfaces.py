# -*- coding: utf-8 -*-
"""Module where all interfaces, events and exceptions live."""

from zope.publisher.interfaces.browser import IDefaultBrowserLayer
from bika.lims.interfaces import IBikaLIMS
from senaite.impress.interfaces import ILayer as ISenaiteIMPRESS
from senaite.lims.interfaces import ISenaiteLIMS

class ISenaiteImppressAddLayer(IDefaultBrowserLayer):
    """Marker interface that defines a browser layer."""

class IMyLIMSLayer(IBikaLIMS, ISenaiteLIMS, ISenaiteIMPRESS):
    """Marker interface that defines a Zope 3 browser layer.
    """
