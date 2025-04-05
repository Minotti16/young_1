from datetime import datetime

hoje = datetime.now()
proximo_ano = datetime(datetime.now().year + 1,1,1)
dias_restantes = (proximo_ano - hoje).days

print(dias_restantes)