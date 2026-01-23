from core.interfaces import FinancialReportRequester, FinancialReportRequest

class FinancialReportController:
    def __init__(self, requester: FinancialReportRequester):
        self._requester = requester

    def create_report(self, report_id: str):
        print(f"Controller: Received request for {report_id}")
        request = FinancialReportRequest(report_id=report_id)
        self._requester.generate_report(request)