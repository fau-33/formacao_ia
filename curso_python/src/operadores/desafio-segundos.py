# Peça ao usuario que insira um valor total em segundos
# e converta para horas, minutos e segundos.

pergunta_segundos = input("Digite o total de segundos: ")
total_segundos = int(pergunta_segundos)

UMA_HORA_EM_SEGUNDOS = 3600
UM_MINUTO_EM_SEGUNDOS = 60

horas = total_segundos // UMA_HORA_EM_SEGUNDOS
minutos = (total_segundos % UMA_HORA_EM_SEGUNDOS) // UM_MINUTO_EM_SEGUNDOS
segundos = total_segundos % UM_MINUTO_EM_SEGUNDOS

print(f"{horas}h {minutos}m {segundos}s")