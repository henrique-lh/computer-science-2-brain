from core.interactor import FinancialReportGenerator
from adapters.gateways import FinancialDataMapper
from adapters.controllers import FinancialReportController
from adapters.presenters import ScreenPresenter, PrintPresenter
from external.views import WebView, PDFView


def run():
    # Common Database Adapter
    database_mapper = FinancialDataMapper()

    # --- Scenario 1: Web Request ---
    print("=== SCENARIO 1: Web Report ===")
    web_view = WebView()
    screen_presenter = ScreenPresenter(web_view)

    # Inject dependencies
    web_interactor = FinancialReportGenerator(database_mapper, screen_presenter)
    web_controller = FinancialReportController(web_interactor)

    web_controller.create_report("REP-WEB-001")

    print("-" * 30)

    # --- Scenario 2: PDF Request ---
    # Notice: We reuse the exact same Database and Interactor logic class,
    # we just swap the Presenter and View.
    print("=== SCENARIO 2: PDF Report ===")
    pdf_view = PDFView()
    print_presenter = PrintPresenter(pdf_view)

    pdf_interactor = FinancialReportGenerator(database_mapper, print_presenter)
    pdf_controller = FinancialReportController(pdf_interactor)

    pdf_controller.create_report("REP-PDF-002")


if __name__ == "__main__":
    run()