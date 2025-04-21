from fpdf import FPDF
from datetime import datetime
from generate_qrcode import generate_qr_code
import os

class PurchaseOrderPDF(FPDF):

    def header(self):
        # Logo
        try:
            self.image("logo.jpg", x=10, y=10, w=40)
        except:
            # Fallback if logo is missing
            self.set_font("Arial", "B", 12)
            self.set_xy(10, 10)
            self.cell(40, 10, "[Logo Placeholder]", align="C")
        
        # Company Info
        self.set_font("SF-Pro-Rounded", "B", 14)
        self.set_xy(60, 10)
        self.cell(0, 10, "Ắc quy Nguyễn Đức", ln=2)
        # self.image(generate_qr_code("https://www.acmecorp.com", 10), x=150, y=10, w=30)
        self.set_font("Arial", "", 10)
        self.cell(0, 6, "123 Business St, City, Country", ln=2)
        self.cell(0, 6, "Email: contact@acme.com | Phone: (123) 456-7890", ln=1)
        
        # Title
        self.set_font("Arial", "B", 16)
        self.set_xy(10, 40)
        self.cell(0, 10, "Purchase Order Confirmation", ln=1, align="C")
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()} - Generated with Python", 0, 0, "C")

def create_po_confirmation(filename):
    pdf = PurchaseOrderPDF()

    pdf.add_font("SF-Pro-Rounded", "B", "font/SF-Pro-Rounded-Regular.ttf", uni=True)
    # pdf.add_font("SF-Pro-Rounded", "", "SF-Pro-Rounded-Heavy.ttf", uni=True)
    # pdf.add_font("SF-Pro-Rounded", "", "SF-Pro-Rounded-Back.ttf", uni=True)
    # pdf.add_font("SF-Pro-Rounded", "", "SF-Pro-Rounded-Back.ttf", uni=True)
    # pdf.add_font("SF-Pro-Rounded", "", "SF-Pro-Rounded-Back.ttf", uni=True)
    # pdf.add_font("SF-Pro-Rounded", "", "SF-Pro-Rounded-Back.ttf", uni=True)
    # pdf.add_font("SF-Pro-Rounded", "", "SF-Pro-Rounded-Back.ttf", uni=True)
    # pdf.add_font("SF-Pro-Rounded", "", "SF-Pro-Rounded-Back.ttf", uni=True)
    pdf.add_page()
    
    # PO Details
    pdf.set_font("Arial", "", 10)
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
    pdf.set_font("Arial", "B", 10)
    headers = ["Item", "Description", "Quantity", "Unit Price", "Total"]
    col_widths = [20, 80, 30, 30, 30]
    
    # Header
    pdf.set_fill_color(200, 200, 200)
    for i, header in enumerate(headers):
        pdf.cell(col_widths[i], 10, header, border=1, fill=True)
    pdf.ln()
    
    # Table Data
    pdf.set_font("Arial", "", 10)
    items = [
        ["001", "Widget A", "10", "$50.00", "$500.00"],
        ["002", "Gadget B", "5", "$100.00", "$500.00"],
        ["003", "Tool C", "20", "$25.00", "$500.00"],
        ["001", "Widget A", "10", "$50.00", "$500.00"],
        ["002", "Gadget B", "5", "$100.00", "$500.00"],
        ["003", "Tool C", "20", "$25.00", "$500.00"],
        ["001", "Widget A", "10", "$50.00", "$500.00"],
        ["002", "Gadget B", "5", "$100.00", "$500.00"],
        ["003", "Tool C", "20", "$25.00", "$500.00"],
        ["001", "Widget A", "10", "$50.00", "$500.00"],
        ["002", "Gadget B", "5", "$100.00", "$500.00"],
        ["003", "Tool C", "20", "$25.00", "$500.00"],
        ["001", "Widget A", "10", "$50.00", "$500.00"],
        ["002", "Gadget B", "5", "$100.00", "$500.00"],
        ["003", "Tool C", "20", "$25.00", "$500.00"],
        ["001", "Widget A", "10", "$50.00", "$500.00"],
        ["002", "Gadget B", "5", "$100.00", "$500.00"],
        ["003", "Tool C", "20", "$25.00", "$500.00"]
    ]
    
    for row in items:
        for i, item in enumerate(row):
            pdf.cell(col_widths[i], 10, item, border=1)
        pdf.ln()
    
    # Total
    pdf.ln(5)
    pdf.set_font("Arial", "B", 12)
    pdf.cell(160, 10, "Total:", align="R")
    pdf.cell(30, 10, "$1500.00", align="R")
    
    # Save PDF
    pdf.output(filename)

create_po_confirmation("po_confirmation_fpdf.pdf")

font_path = "font/SF-Pro-Rounded-Regular.ttf"
# Clean up stale .pkl files
for pkl_file in ["SF-Pro-Rounded-Regular.pkl", "SF-Pro-Rounded-Regular.cw127.pkl"]:
    pkl_path = os.path.join(os.path.dirname(font_path), pkl_file)
    if os.path.exists(pkl_path):
        try:
            os.remove(pkl_path)
            print(f"Removed stale cache: {pkl_path}")
        except Exception as e:
            print(f"Failed to remove {pkl_path}: {e}")
