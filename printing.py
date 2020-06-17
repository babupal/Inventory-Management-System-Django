from reportlab.lib.pagesizes import letter, A4

from reportlab.platypus import SimpleDocTemplate, Paragraph, Table
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_RIGHT
from django.contrib.auth.models import User
from Inventory.models import Item, Category

class MyPrint:
    def __init__(self, buffer, pagesize):
        self.buffer = buffer
        if pagesize == 'A4':
            self.pagesize = A4
        elif pagesize == 'Letter':
            self.pagesize = letter
        self.width, self.height = self.pagesize

    def print_users(self):
        buffer = self.buffer
        doc = SimpleDocTemplate(buffer,
                                rightMargin=72,
                                leftMargin=72,
                                topMargin=72,
                                bottomMargin=72,
                                pagesize=self.pagesize)

        elements = []
        styles = getSampleStyleSheet()
        styles.add(ParagraphStyle(name='centered', alignment=TA_CENTER))

        users = User.objects.all()
        print("Users: "+ str(users))
        elements.append(Paragraph('My User Names', styles['Heading1']))
        for i, user in enumerate(users):
            print(str(i) + user.username)
            elements.append(Paragraph(user.username, styles['Normal']))
        doc.build(elements)
        pdf = buffer.getvalue()
        buffer.close()
        return pdf
    
    def print_items(self):
        buffer = self.buffer
        doc = SimpleDocTemplate(buffer,
                                rightMargin=72,
                                leftMargin=72,
                                topMargin=72,
                                bottomMargin=72,
                                pagesize=self.pagesize)

        elements = []
        styles = getSampleStyleSheet()
        style_right = ParagraphStyle(name='right', parent=styles['Normal'], alignment=TA_RIGHT)
        # styles.add(ParagraphStyle(name='centered', alignment=TA_CENTER))

        items = Item.objects.all()  
        elements.append(Paragraph('Inventory Item Report', styles['Heading1']))
        for i, item in enumerate(items):
            iqstr=str(item.quantity)
            ipstr=str(item.price)
            iistr=str(item.item_id)
            tbl_data = [
                        [
                        Paragraph(iistr, styles["Normal"]),
                        Paragraph(item.name, styles["Normal"]),
                        Paragraph(item.category.category, styles["Normal"]),
                        Paragraph(iqstr, style_right),
                        Paragraph(ipstr, style_right),
                        ]
            ]
            tbl = Table(tbl_data)
            elements.append(tbl)
        doc.build(elements)
        pdf = buffer.getvalue()
        buffer.close()
        return pdf

 