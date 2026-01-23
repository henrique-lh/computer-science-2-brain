import abc
from dataclasses import dataclass
from typing import List
from core.entities import FinancialEntity

# --- Data Structures (DTOs) ---
@dataclass
class FinancialReportRequest:
    report_id: str

@dataclass
class FinancialReportResponse:
    report_id: str
    total_balance: float
    status: str

# --- View Models (Data for the UI) ---
@dataclass
class ScreenViewModel:
    formatted_balance: str
    color_code: str

@dataclass
class PrintViewModel:
    pdf_formatted_text: str

# --- Interfaces (Ports) ---

# Input Boundary
class FinancialReportRequester(abc.ABC):
    @abc.abstractmethod
    def generate_report(self, request: FinancialReportRequest) -> None:
        pass

# Output Boundary
class FinancialReportPresenter(abc.ABC):
    @abc.abstractmethod
    def present(self, response: FinancialReportResponse) -> None:
        pass

# Gateway Interface
class FinancialDataGateway(abc.ABC):
    @abc.abstractmethod
    def get_entities(self) -> List[FinancialEntity]:
        pass

# View Interfaces (Technically needed by Presenters)
class ScreenView(abc.ABC):
    @abc.abstractmethod
    def display(self, view_model: ScreenViewModel) -> None:
        pass

class PrintView(abc.ABC):
    @abc.abstractmethod
    def print_document(self, view_model: PrintViewModel) -> None:
        pass