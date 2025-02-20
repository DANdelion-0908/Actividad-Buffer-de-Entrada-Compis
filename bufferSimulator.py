def cargar_buffer(entrada, inicio, tamano_buffer):
    buffer = entrada[inicio:inicio + tamano_buffer]
    if len(buffer) < tamano_buffer:
        buffer.append("eof")
    return buffer

def procesar_buffer(entrada, tamano_buffer = 10, inicio = 0, avance = 0, lexema = ""):
    buffer = cargar_buffer(entrada, inicio, tamano_buffer)
    
    while True:
        print("                                    ", buffer)
        while avance < len(buffer):
            char = buffer[avance]
            avance += 1
            
            if char == " " or char == "eof":
                if lexema:
                    print(f"Lexema procesado: {lexema}")
                    lexema = ""
                if char == "eof":
                    return
            else:
                lexema += char
        
        # recargar el buffer hasta encontrar eof
        inicio += tamano_buffer
        avance = 0
        buffer = cargar_buffer(entrada, inicio, tamano_buffer)


entrada = list("Esto es un ejemplo de entrada con eof")
procesar_buffer(entrada)

