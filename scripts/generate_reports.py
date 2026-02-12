from fpdf import FPDF

def generate_csv(df, path):
    df.to_csv(path, index=False)


class PDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, self.title, 0, 1, "C")

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", 0, 0, "C")


def generate_pdf(df, path, title):
    pdf = PDF()
    pdf.title = title
    pdf.add_page()
    pdf.set_font("Arial", "", 10)

    col_width = pdf.w / (len(df.columns) + 1)

    # Header
    for col in df.columns:
        pdf.cell(col_width, 10, str(col), 1)
    pdf.ln()

    # Rows
    for _, row in df.iterrows():
        for item in row:
            pdf.cell(col_width, 10, str(item), 1)
        pdf.ln()

    pdf.output(path)