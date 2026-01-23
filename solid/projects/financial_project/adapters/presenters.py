from core.interfaces import (
    FinancialReportPresenter,
    FinancialReportResponse,
    ScreenView,
    PrintView,
    ScreenViewModel,
    PrintViewModel
)


class ScreenPresenter(FinancialReportPresenter):
    def __init__(self, view: ScreenView):
        self._view = view

    def present(self, response: FinancialReportResponse) -> None:
        color = "green" if response.total_balance >= 0 else "red"
        formatted_money = f"${response.total_balance:,.2f}"

        view_model = ScreenViewModel(
            formatted_balance=f"{formatted_money} ({response.status})",
            color_code=color
        )
        self._view.display(view_model)


class PrintPresenter(FinancialReportPresenter):
    def __init__(self, view: PrintView):
        self._view = view

    def present(self, response: FinancialReportResponse) -> None:
        formatted_text = (
            f"OFFICIAL REPORT: {response.report_id}\n"
            f"BALANCE: {response.total_balance}\n"
            f"STATUS: {response.status}"
        )
        view_model = PrintViewModel(pdf_formatted_text=formatted_text)
        self._view.print_document(view_model)