from io import BytesIO

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.platypus import (
    Paragraph,
    SimpleDocTemplate,
    Spacer,
)


def create_pdf(result: dict) -> bytes:
    """
    Convert the Newsroom result dictionary into a PDF.
    Returns the PDF as bytes.
    """

    buffer = BytesIO()

    document = SimpleDocTemplate(
        buffer,
        pagesize=A4
    )

    styles = getSampleStyleSheet()

    content = []

    # -------------------------
    # Title
    # -------------------------
    content.append(
        Paragraph(
            "AI Newsroom Report",
            styles["Title"]
        )
    )

    content.append(Spacer(1, 20))

    # -------------------------
    # Add each section
    # -------------------------
    for section_name, section_data in result.items():

        heading = section_name.replace("_", " ").title()

        content.append(
            Paragraph(
                heading,
                styles["Heading2"]
            )
        )

        content.append(Spacer(1, 8))

        # If the section is a dictionary
        if isinstance(section_data, dict):

            for key, value in section_data.items():

                content.append(
                    Paragraph(
                        f"<b>{key.replace('_', ' ').title()}</b>",
                        styles["BodyText"]
                    )
                )

                content.append(
                    Paragraph(
                        str(value),
                        styles["BodyText"]
                    )
                )

                content.append(Spacer(1, 6))

        # If the section is a list
        elif isinstance(section_data, list):

            for item in section_data:

                content.append(
                    Paragraph(
                        f"• {item}",
                        styles["BodyText"]
                    )
                )

            content.append(Spacer(1, 10))

        # Otherwise it's plain text
        else:

            content.append(
                Paragraph(
                    str(section_data),
                    styles["BodyText"]
                )
            )

            content.append(Spacer(1, 10))

    document.build(content)

    pdf_bytes = buffer.getvalue()

    buffer.close()

    return pdf_bytes