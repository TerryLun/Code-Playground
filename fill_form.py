import inspect
import pdfforms
import pdfrw
from reportlab.pdfgen import canvas


def create_overlay():
    """
    Create the data that will be overlayed on top
    of the form that we want to fill
    """
    c = canvas.Canvas('simple_form_overlay.pdf')

    c.drawString(115, 650, 'Mike')
    c.drawString(115, 600, 'Driscoll')
    c.drawString(115, 550, '123 Greenway Road')
    c.drawString(115, 500, 'Everytown')
    c.drawString(355, 500, 'IA')
    c.drawString(115, 450, '55555')

    c.save()