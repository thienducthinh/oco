from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from datetime import datetime
# Assuming generate_qr_code is defined elsewhere
from generate_qrcode import generate_qr_code

def create_po_confirmation(filename):
    # Initialize document
    doc = SimpleDocTemplate(filename, pagesize=letter, leftMargin=10*mm, rightMargin=10*mm, topMargin=10*mm, bottomMargin=10*mm)
    elements = []
    styles = getSampleStyleSheet()

    # Register custom font (replace SF-Pro.ttf with your .otf or .ttf file)
    try:
        pdfmetrics.registerFont(TTFont("SF-Pro-Rounded", "font/SF-Pro-Rounded-Regular.ttf"))
    except Exception as e:
        print(f"Font registration failed: {e}")

    # Define custom style for company name
    company_style = ParagraphStyle(
        name="CompanyName",
        fontName="SF-Pro-Rounded",
        fontSize=14,
        leading=16,
        textColor=colors.black
    )

    # Header content (to be drawn on each page via onPage)
    def header_footer(canvas, doc):
        canvas.saveState()

        # Logo
        try:
            canvas.drawImage("logo.jpg", 10*mm, doc.pagesize[1] - 30*mm, width=40*mm, height=20*mm)
        except:
            canvas.setFont("Helvetica-Bold", 12)
            canvas.drawCentredString(30*mm, doc.pagesize[1] - 20*mm, "[Logo Placeholder]")

        # Company Info
        canvas.setFont("SF-Pro-Rounded" if "SF-Pro-Rounded" in pdfmetrics.getRegisteredFontNames() else "Helvetica-Bold", 14)
        canvas.drawString(60*mm, doc.pagesize[1] - 20*mm, "Ắc quy Nguyễn Đức")
        canvas.setFont("Helvetica", 10)
        canvas.drawString(60*mm, doc.pagesize[1] - 25*mm, "123 Business St, City, Country")
        canvas.drawString(60*mm, doc.pagesize[1] - 30*mm, "Email: contact@acme.com | Phone: (123) 456-7890")

        # QR Code (uncomment if needed)
        # try:
        #     qr_path = generate_qr_code("https://www.acmecorp.com", 10)
        #     canvas.drawImage(qr_path, 150*mm, doc.pagesize[1] - 30*mm, width=30*mm, height=30*mm)
        # except:
        #     pass

        # Title
        canvas.setFont("Helvetica-Bold", 16)
        canvas.drawCentredString(doc.pagesize[0]/2, doc.pagesize[1] - 50*mm, "Purchase Order Confirmation")

        # Footer
        canvas.setFont("Helvetica-Oblique", 8)
        canvas.drawCentredString(doc.pagesize[0]/2, 10*mm, f"Page {canvas.getPageNumber()} - Generated with Python")
        canvas.restoreState()

    # PO Details
    po_details = [
        f"PO Number: PO-2025-001",
        f"Issue Date: {datetime.now().strftime('%Y-%m-%d')}",
        f"Supplier: Global Supplies Inc.",
        f"  456 Industrial Rd, City, Country",
        f"  Email: sales@globalsupplies.com",
        f"Delivery Date: {datetime.now().strftime('%Y-%m')}-15",
    ]
    for detail in po_details:
        elements.append(Paragraph(detail, styles["Normal"]))
        elements.append(Spacer(1, 2*mm))

    elements.append(Spacer(1, 10*mm))

    # Item Table
    headers = ["Item", "Description", "Quantity", "Unit Price", "Total"]
    col_widths = [20*mm, 80*mm, 30*mm, 30*mm, 30*mm]
    data = [headers] + [
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

    table = Table(data, colWidths=col_widths)
    table.setStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.Color(0.78, 0.78, 0.78)),  # Header background
        ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
        ("FONTSIZE", (0, 0), (-1, -1), 10),
        ("ALIGN", (2, 0), (-1, -1), "CENTER"),  # Center Quantity, Unit Price, Total
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ])
    elements.append(table)

    # Total
    elements.append(Spacer(1, 5*mm))
    total_table = Table([["Total:", "$1500.00"]], colWidths=[160*mm, 30*mm])
    total_table.setStyle([
        ("FONTNAME", (0, 0), (-1, -1), "Helvetica-Bold"),
        ("FONTSIZE", (0, 0), (-1, -1), 12),
        ("ALIGN", (0, 0), (-1, -1), "RIGHT"),
    ])
    elements.append(total_table)

    # Build PDF with header and footer
    doc.build(elements, onFirstPage=header_footer, onLaterPages=header_footer)

create_po_confirmation("po_confirmation_reportlab.pdf")