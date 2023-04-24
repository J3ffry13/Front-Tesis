# Creamos funcion para validar que el texto ingresado
def validate_entry(text, new_text):
    # Valdiamos que el texto ingresado no sea mayor a 5 dígitos
    if len(new_text) > 5:
        return False
    # Validamos que el texto ingresado sea numero (entero o decimal)
    if new_text.isdecimal() or new_text == '.':
        # Validamos que el texto ingresado no sea mayor a 100
        if float(new_text) > 100:
            return False
    return text.isdecimal() or text == '.'