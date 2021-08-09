from openpyxl import load_workbook

def get_empreendimento_id(filename):
    wb = load_workbook(filename=filename)
    sheet = wb.active
    x1 = sheet['A2']
    return int(x1.value)
