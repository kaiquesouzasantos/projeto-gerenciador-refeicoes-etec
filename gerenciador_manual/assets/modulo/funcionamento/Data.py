from datetime import datetime

class Data:
    def func_retorna_data():
        return datetime.now().strftime('%d/%m/%Y')

    def func_retorna_periodo():
        return datetime.now().strftime('%H:%M')

    def func_retorna_periodo_segundo():
        return datetime.now().strftime('%H:%M:%S')
    
    def func_retorna_hora_float():
        return float(datetime.now().strftime('%H.%M'))
    
    def func_retorna_periodo_str():
        horario = Data.func_retorna_hora_float()

        if(horario >= 11.2 and horario <= 13.0):
            return 'Matutino'
        elif(horario >= 16.2 and horario <= 18):
            return 'Vesperino'
        elif(horario >= 21.2 and horario <= 23):
            return 'Noturno'
        else:
            return 'Fora de Servico'