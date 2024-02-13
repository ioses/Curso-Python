import openpyxl

# Ruta al archivo Excel en la carpeta de Descargas de Windows
archivo_excel = "C:\\Users\\ioses\\Downloads\\prueba.xlsx"

# Abre el archivo Excel
try:
    workbook = openpyxl.load_workbook(archivo_excel)
except FileNotFoundError:
    print(f"El archivo {archivo_excel} no se encuentra en la carpeta de Descargas.")
    exit()

# Selecciona la primera hoja del archivo (puedes cambiar el nombre si es necesario)
sheet = workbook.active

# Lee el valor de la primera celda (A1)
valor_celda = sheet.cell(row=1, column=1).value

# Imprime el valor de la primera celda
print(f"El valor de la primera celda es: {valor_celda}")

# Cierra el archivo Excel
workbook.close()
