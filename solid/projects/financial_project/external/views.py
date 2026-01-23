from core.interfaces import ScreenView, PrintView, ScreenViewModel, PrintViewModel

class WebView(ScreenView):
    def display(self, view_model: ScreenViewModel) -> None:
        print("\n[WEB VIEW RENDER]")
        print(f"<html><h1 style='color:{view_model.color_code}'>")
        print(f"Balance: {view_model.formatted_balance}")
        print("</h1></html>\n")

class PDFView(PrintView):
    def print_document(self, view_model: PrintViewModel) -> None:
        print("\n[PDF VIEW RENDER]")
        print("%PDF-1.4")
        print(view_model.pdf_formatted_text)
        print("%%EOF\n")