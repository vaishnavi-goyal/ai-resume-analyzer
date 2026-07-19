import PyPDF2


def extract_resume_text(uploaded_file):

    reader = PyPDF2.PdfReader(uploaded_file)

    text = ""

    for page in reader.pages:

        page_text = page.extract_text()

        if page_text:

            text += page_text + "\n"

    return text


def get_resume_statistics(text):

    words = len(text.split())

    characters = len(text)

    lines = len(text.split("\n"))

    return {

        "words": words,

        "characters": characters,

        "lines": lines

    }
