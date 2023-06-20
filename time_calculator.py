def add_time(horario_inicial, duracao, dia_inicio=None):
    hora_inicio, minuto_inicio = map(int, horario_inicial[:-3].split(':'))
    periodo_inicio = horario_inicial[-2:]

    hora_duracao, minuto_duracao = map(int, duracao.split(':'))

    if periodo_inicio == 'PM' and hora_inicio != 12:
        hora_inicio += 12

    minuto_final = (minuto_inicio + minuto_duracao) % 60
    carry_hora = (minuto_inicio + minuto_duracao) // 60
    hora_final = (hora_inicio + hora_duracao + carry_hora) % 24

    if hora_final < 12:
        periodo_final = 'AM'
        if hora_final == 0:
            hora_final = 12
    else:
        periodo_final = 'PM'
        if hora_final > 12:
            hora_final -= 12

    num_dias_depois = (hora_inicio + hora_duracao + carry_hora) // 24

    if dia_inicio:
        dia_inicio = dia_inicio.capitalize()
        dias_da_semana = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
        indice_dia_inicio = dias_da_semana.index(dia_inicio)
        indice_dia_final = (indice_dia_inicio + num_dias_depois) % 7
        dia_final = dias_da_semana[indice_dia_final]
        string_dia = f", {dia_final}"
    else:
        string_dia = ""

    horario_saida = f"{hora_final}:{minuto_final:02d} {periodo_final}{string_dia}"

    if num_dias_depois == 1:
        horario_saida += " (próximo dia)"
    elif num_dias_depois > 1:
        horario_saida += f" ({num_dias_depois} dias depois)"

    return horario_saida

add_time("3:00 PM", "3:10")

add_time("11:30 AM", "2:32", "Monday")

add_time("11:43 AM", "00:20")

add_time("10:10 PM", "3:30")

add_time("11:43 PM", "24:20", "tueSday")

add_time("6:30 PM", "205:12")