from fpdf import FPDF
from datetime import datetime

class PurchaseOrderPDF(FPDF):
    def header(self):
        # Logo
        try:
            self.image("logo.jpg", x=10, y=10, w=25)
        except:
            # Fallback if logo is missing
            self.set_font("SF-Pro-Rounded", "B", 12)
            self.set_xy(10, 10)
            self.cell(40, 10, "[Logo Placeholder]", align="C")
        
        # Company Info
        self.set_font("SF-Pro-Rounded", "B", 14)
        self.set_xy(60, 10)
        self.cell(0, 10, "Ắc quy Nguyễn Đức", ln=2)
        self.set_font("SF-Pro-Rounded", "B", 10)
        self.cell(0, 6, "123 Business St, City, Country", ln=2)
        self.cell(0, 6, "Email: contact@acme.com | Phone: (123) 456-7890", ln=1)
        
        # Title
        self.set_font("SF-Pro-Rounded", "B", 16)
        self.set_xy(10, 40)
        self.cell(0, 10, "Purchase Order Confirmation", ln=1, align="C")
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("SF-Pro-Rounded", "B", 8)
        self.cell(0, 10, f"Page {self.page_no()} - Generated with Python", 0, 0, "C")

def create_po_confirmation(filename, items):
    pdf = PurchaseOrderPDF()
    pdf.add_font("SF-Pro-Rounded", "B", "font/SF-Pro-Rounded-Regular.ttf", uni=True)
    pdf.add_page()
    
    # PO Details
    pdf.set_font("SF-Pro-Rounded", "B", 10)
    po_details = [
        f"PO Number: PO-2025-001",
        f"Issue Date: {datetime.now().strftime('%Y-%m-%d')}",
        f"Supplier: Global Supplies Inc.",
        f"  456 Industrial Rd, City, Country",
        f"  Email: sales@globalsupplies.com",
        f"Delivery Date: {datetime.now().strftime('%Y-%m')}-15",
    ]
    for detail in po_details:
        pdf.cell(0, 8, detail, ln=1)
    
    pdf.ln(10)
    
    # Item Table
    pdf.set_font("SF-Pro-Rounded", "B", 10)
    headers = ["Item", "Description", "Quantity", "Unit Price", "Tổng tiền"]
    col_widths = [20, 80, 30, 30, 30]
    
    # Header
    pdf.set_fill_color(200, 200, 200)
    for i, header in enumerate(headers):
        pdf.cell(col_widths[i], 10, header, border=1, fill=True)
    pdf.ln()
    
    # Table Data

    for row in items:
        for i, item in enumerate(row):
            pdf.cell(col_widths[i], 10, item, border=1)
        pdf.ln()
    
    # Total
    pdf.ln(5)
    pdf.set_font("SF-Pro-Rounded", "B", 12)
    pdf.cell(160, 10, "Total:", align="R")
    pdf.cell(30, 10, "$1500.00", align="R")
    
    # Save PDF
    pdf.output(filename)

items = [
    ["001", "Widget A", "10", "$50.00", "$500.00"],
    ["002", "Gadget B", "5", "$100.00", "$500.00"],
    ["003", "Tool C", "20", "$25.00", "$500.00"],
]

create_po_confirmation("po_confirmation_fpdf.pdf", items)

