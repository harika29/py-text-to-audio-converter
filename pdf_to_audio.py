import pyttsx3
import PyPDF2


def text_to_speech(text=""):
    speaker = pyttsx3.init()
    speaker.say(text)
    speaker.runAndWait()


def read_from_pdf(pdf):
    book = open(pdf, "rb")
    pdf_reader = PyPDF2.PdfFileReader(book)
    page_count = pdf_reader.numPages
    print("Number of pages in selected book: ", page_count)
    text = ""
    # extract context from every page and append it to text
    for i in range(page_count):
        page = pdf_reader.getPage(i)
        text += page.extractText()
    return text


if __name__ == '__main__':
    pdf_text = read_from_pdf("sampleFile.pdf")
    text_to_speech(pdf_text)