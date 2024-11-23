from fpdf import FPDF

data = [
  {
    "title": "Test",
    "category_id": 5,
    "amount": 100,
    "date": "2024-11-23T20:10:20.379000"
  },
  {
    "title": "Test",
    "category_id": 7,
    "amount": 150,
    "date": "2024-11-23T20:10:20.379000"
  }
]

head = ("Название", "Категория", "Сумма", "Дата")

pdf = FPDF()
pdf.add_page()

pdf.add_font("DejaVu", '', 'DejaVuSans.ttf')
pdf.add_font("DejaVu", "B", "DejaVuSans-Bold.ttf")

pdf.set_font("DejaVu", size=16)



pdf.output('table.pdf')