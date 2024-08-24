import re

# Extraer correos electrónicos
def extraer_emails(text):
    return re.findall(r'\S+@\S+\.\S+', text)

# Extraer comentarios de un código fuente
def extraer_comentarios(code):
    return re.findall(r'//.*|/\*.*?\*/', code, re.DOTALL)

# Validar fechas en formato mm/dd/yyyy
def validar_fechas(date):
    return bool(re.match(r'^(0[1-9]|1[0-2])/(0[1-9]|[12][0-9]|3[01])/(\d{4})$', date))

# Aquí se extraen los correos electrónicos
text = "Para más información puedes escribirnos a empresa@dominio.com, soporte@ejemplo.org, juanito@gmail.com y pepito123@hotmail.com."
emails = extraer_emails(text)
print("Correos electrónicos extraídos:", emails)

# Aquí se extraen los comentarios de un código fuente
code = """
// Comentario de línea
int main() {
    /* Comentario de bloque */
    printf("Hola Mundo"); // Otro comentario
}
"""
comments = extraer_comentarios(code)
print("Comentarios extraídos:", comments)

# Aquí se validan las fechas
dates = ["00/15/2023", "02/29/2024", "13/01/2021", "04/31/2023"]
for date in dates:
    print(f"{date} es válida: {validar_fechas(date)}")
