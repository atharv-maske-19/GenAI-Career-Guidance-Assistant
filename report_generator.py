from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet


def generate_report(
    ats_score,
    career,
    skills,
    strengths,
    weaknesses
):

    pdf_file = "career_report.pdf"

    doc = SimpleDocTemplate(
        pdf_file
    )

    styles = getSampleStyleSheet()

    content = []

    content.append(
        Paragraph(
            "Career Guidance Report",
            styles["Title"]
        )
    )

    content.append(
        Spacer(1, 12)
    )

    content.append(
        Paragraph(
            f"ATS Score: {ats_score}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Recommended Career: {career}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Skills: {', '.join(skills)}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Strengths: {', '.join(strengths)}",
            styles["Normal"]
        )
    )

    content.append(
        Paragraph(
            f"Weaknesses: {', '.join(weaknesses)}",
            styles["Normal"]
        )
    )

    doc.build(content)

    return pdf_file