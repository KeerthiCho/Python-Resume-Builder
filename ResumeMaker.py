from fpdf import FPDF

class ResumeBuilder(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, "Resume", ln=True, align="C")
        self.ln(10)

    def add_section(self, title):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, title, ln=True)
        self.set_font("Arial", "", 12)

    def add_item(self, text):
        self.multi_cell(0, 10, f"- {text}")
        self.ln(1)

# Create a resume instance
pdf = ResumeBuilder()
pdf.add_page()

# Personal Details
pdf.add_section("Personal Details")
pdf.add_item("Name: John Doe")
pdf.add_item("Email: johndoe@example.com")
pdf.add_item("Phone: +123456789")

# Education
pdf.add_section("Education")
pdf.add_item("B.Sc. in Computer Science, XYZ University (2018-2022)")
pdf.add_item("High School, ABC School (2016-2018)")

# Skills
pdf.add_section("Skills")
pdf.add_item("Python, Java, C++")
pdf.add_item("Web Development: HTML, CSS, JavaScript")
pdf.add_item("Data Analysis: Pandas, NumPy, Matplotlib")

# Experience
pdf.add_section("Experience")
pdf.add_item("Intern at Tech Company (2021): Worked on web scraping and data analysis.")

# Save the resume
pdf.output("resume.pdf")
print("Resume generated successfully as resume.pdf")
