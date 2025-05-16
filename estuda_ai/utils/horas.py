from datetime import datetime, date


def pega_hora():
    hoje = datetime.now()
    hora = hoje.time()
    hora_formatada = hora.strftime('%H:%M:%S')
    return hora_formatada


data_hoje = date.today()
hora_atual = datetime.now().time()



