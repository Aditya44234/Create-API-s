from flask import Response
from fpdf import FPDF
from app.routes.users import user_bp, entries

# Export as CSV
@user_bp.route("/export_csv")
def export_csv():
    def generate():
        yield 'id,name,role,email,message,timestamp\n'
        for entry in entries:
            line = f"{entry['id']},{entry['name']},{entry['role']},{entry['email']},{entry['message']},{entry['timestamp']}\n"
            yield line
    return Response(generate(), mimetype='text/csv',
                    headers={"Content-Disposition": "attachment;filename=entries.csv"})

# Export as PDF
@user_bp.route("/export_pdf")
def export_pdf():
    class PDF(FPDF):
        def header(self):
            self.set_font('Arial', 'B', 12)
            self.cell(0, 10, 'User Entries', 0, 1, 'C')
            self.ln(5)

    pdf = PDF()
    pdf.add_page()
    pdf.set_font("Arial", size=10)

    # Table header
    col_widths = [10, 30, 25, 45, 40, 40]
    headers = ['ID', 'Name', 'Role', 'Email', 'Message', 'Timestamp']
    for i, header in enumerate(headers):
        pdf.cell(col_widths[i], 8, header, 1, 0, 'C')
    pdf.ln()

    # Table rows
    for entry in entries:
        row = [
            str(entry['id']),
            entry['name'],
            entry['role'],
            entry['email'],
            entry['message'],
            entry['timestamp']
        ]
        for i, item in enumerate(row):
            display = item
            if len(display) > 30 and i == 4:  # message column
                display = display[:27] + "..."
            pdf.cell(col_widths[i], 8, display, 1, 0, 'C')
        pdf.ln()

    pdf_bytes = pdf.output(dest='S').encode('latin1')
    return Response(
        pdf_bytes,
        mimetype='application/pdf',
        headers={"Content-Disposition": "attachment;filename=entries.pdf"}
    )
