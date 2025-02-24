def extract_numeric_values(text):
    # Verifica si el texto contiene comas
    if isinstance(text, str) and ',' in text:
        # Divide el texto por comas y convierte a float
        return [float(value) for value in text.split(',') if value.strip().isdigit()]
    elif isinstance(text, str):
        # Convierte el valor único a float
        return [float(text)] if text.strip().isdigit() else []
    else:
        return []
