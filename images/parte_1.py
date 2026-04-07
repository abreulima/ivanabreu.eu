 # escrever
    tecla = rl.get_char_pressed()

    while tecla > 0:
        if 32 <= tecla <= 125 and len(entrada) < 50:
            entrada += chr(tecla)
        tecla = rl.get_char_pressed()

    # apagar
    if rl.is_key_pressed(rl.KEY_BACKSPACE) and len(entrada) > 0:
        entrada = entrada[:-1]

    # apertar ENTER
    if rl.is_key_pressed(rl.KEY_ENTER) and entrada.strip() != "":
        historia = "Voce digitou: " + entrada
        entrada = ""
