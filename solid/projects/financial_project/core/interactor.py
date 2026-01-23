from core.interfaces import (
    FinancialReportRequester,
    FinancialDataGateway,
    FinancialReportPresenter,
    FinancialReportRequest,
    FinancialReportResponse
)


class FinancialReportGenerator(FinancialReportRequester):
    def __init__(self, gateway: FinancialDataGateway,
                 presenter: FinancialReportPresenter):
        self._gateway = gateway
        self._presenter = presenter

    def generate_report(self, request: FinancialReportRequest) -> None:
        print(f"--- Interactor: Generating Report {request.report_id} ---")

        # 1. Get Data
        entities = self._gateway.get_entities()

        # 2. Business Logic
        total = sum(e.amount for e in entities)
        status = "PROFITABLE" if total >= 0 else "LOSS"

        # 3. Create Response
        response = FinancialReportResponse(
            report_id=request.report_id,
            total_balance=total,
            status=status
        )

        # 4. Present
        self._presenter.present(response)