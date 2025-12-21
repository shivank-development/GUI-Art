from fpdf import FPDF

class ResumePDF(FPDF):
    def header(self):
        self.set_font("Arial", "B", 16)
        self.cell(0, 10, self.name, ln=True, align="C")
        self.set_font("Arial", "", 12)
        self.cell(0, 10, self.contact_info, ln=True, align="C")
        self.ln(10)

    def add_section(self, title, content):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, title, ln=True)
        self.set_font("Arial", "", 12)
        for line in content:
            self.multi_cell(0, 10, f"- {line}")
        self.ln(5)

    def set_info(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info

def collect_input():
    print("Enter your basic information:")
    name = input("Full Name: ")
    email = input("Email: ")
    phone = input("Phone: ")
    linkedin = input("LinkedIn URL: ")
    contact_info = f"{email} | {phone} | {linkedin}"

    summary = input("Professional Summary: ")

    skills = input("List your skills (comma-separated): ").split(",")
    skills = [s.strip() for s in skills]

    print("\nEnter your Work Experience (type 'done' when finished):")
    work_experience = []
    while True:
        title = input("Job Title: ")
        if title.lower() == "done":
            break
        company = input("Company: ")
        date = input("Dates (e.g. Jan 2020 - Present): ")
        desc = input("Description: ")
        work_experience.append(f"{title} at {company} ({date})\n{desc}")

    print("\nEnter your Education:")
    edu = input("Degree and School (e.g. B.Sc. in Computer Science, XYZ University): ")
    education = [edu]

    return name, contact_info, summary, skills, work_experience, education

def generate_resume():
    name, contact_info, summary, skills, work_experience, education = collect_input()

    pdf = ResumePDF()
    pdf.set_info(name, contact_info)
    pdf.add_page()

    pdf.add_section("Professional Summary", [summary])
    pdf.add_section("Skills", skills)
    pdf.add_section("Work Experience", work_experience)
    pdf.add_section("Education", education)

    filename = name.replace(" ", "_") + "_Resume.pdf"
    pdf.output(filename)
    print(f"\nResume saved as: {filename}")

if __name__ == "__main__":
    generate_resume()


