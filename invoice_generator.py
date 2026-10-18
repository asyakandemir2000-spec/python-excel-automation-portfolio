import os

try:
    from reportlab.lib.pagesizes import letter
    from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
except ImportError:
    print("Required dependency missing! Please run 'pip install reportlab' in your terminal.")
    input("\nPress Enter to close...")
    exit()

OUTPUT_PDF = "./invoice_summary.pdf"

def generate_invoice_pdf():
    print("Initializing PDF Invoice Automation Engine...")
    
    doc = SimpleDocTemplate(OUTPUT_PDF, pagesize=letter,
                            rightMargin=40, leftMargin=40, topMargin=40, bottomMargin=40)
    story = []
    
    styles = getSampleStyleSheet()
    
    title_style = ParagraphStyle(
        'InvoiceTitle',
        parent=styles['Heading1'],
        fontSize=24,
        leading=28,
        alignment=1,
        spaceAfter=20
    )
    
    normal_style = ParagraphStyle(
        'InvoiceText',
        parent=styles['Normal'],
        fontSize=10,
        leading=14,
        fontName="Helvetica"
    )
    
    bold_style = ParagraphStyle(
        'InvoiceBold',
        parent=normal_style,
        fontName="Helvetica-Bold"
    )

    story.append(Paragraph("INVOICE SUMMARY", title_style))
    story.append(Paragraph("==================================================", normal_style))
    story.append(Spacer(1, 10))
    
    story.append(Paragraph("<b>Invoice Number:</b> INV-2026-001", normal_style))
    story.append(Paragraph("<b>Date:</b> September 29, 2026", normal_style))
    story.append(Paragraph("<b>Due Date:</b> October 15, 2026", normal_style))
    story.append(Spacer(1, 15))
    
    story.append(Paragraph("--------------------------------------------------", normal_style))
    story.append(Paragraph("CLIENT INFORMATION:", bold_style))
    story.append(Paragraph("--------------------------------------------------", normal_style))
    story.append(Paragraph("Name: Acme Global Corp", normal_style))
    story.append(Paragraph("Email: billing@acmeglobal.com", normal_style))
    story.append(Paragraph("Address: 123 Tech Avenue, New York, NY", normal_style))
    story.append(Spacer(1, 15))
    
    story.append(Paragraph("--------------------------------------------------", normal_style))
    story.append(Paragraph("BILLING DETAILS:", bold_style))
    story.append(Paragraph("--------------------------------------------------", normal_style))
    story.append(Paragraph("<b>Description:</b> Backend Automation Services | <b>Qty:</b> 1 | <b>Price:</b> $1250.00", normal_style))
    story.append(Spacer(1, 10))
    
    story.append(Paragraph("--------------------------------------------------", normal_style))
    story.append(Paragraph("<b>GRAND TOTAL: $1250.00</b>", ParagraphStyle('Total', parent=normal_style, fontSize=12, fontName="Helvetica-Bold")))
    story.append(Paragraph("==================================================", normal_style))
    story.append(Spacer(1, 20))
    
    story.append(Paragraph("Thank you for your business!", ParagraphStyle('ThankYou', parent=normal_style, alignment=1, fontName="Helvetica-Oblique")))
    
    doc.build(story)
    print(f"\nSuccess! Professional corporate PDF generated at: '{OUTPUT_PDF}'")

if __name__ == "__main__":
    try:
        generate_invoice_pdf()
    except Exception as error:
        print(f"An error occurred during PDF generation workflow: {error}")

    input("\nProcess finished! Press Enter to close this window...")