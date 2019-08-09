from senaite.impress.analysisrequest.reportview import MultiReportView

class MyMultiReportView(MultiReportView):
    """My specific controller view for multi-reports
    """

    def __init__(self, collection, request):
        logger.info("MyMultiReportView::__init__:collection={}"
                    .format(collection))
        super(MultiReportView, self).__init__(collection, request)
        self.collection = collection
        self.request = request
