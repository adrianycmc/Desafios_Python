# Desafio 073: Tuplas com Times de Futebol - Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre: 
# A) Apenas os 5 primeiros colocados. 
# B) Os últimos 4 colocados da tabela. 
# C) Uma lista com os times em ordem alfabética. 
# D) A posição do time da Chapecoense.

times = ("Botafogo", "Palmeiras", "Flamengo", "Fortaleza", "Internacional", "São Paulo", "Corinthians", "Bahia", "Cruzeiro", "Vasco da Gama", "EC Vitória", "Atlético-MG", "Fluminense", "Grêmio", "Juventude", "Bragantino", "Athletico-PR", "Criciuma", "Atlético-GO", "Cuiaba")

print("\n" + f"Os 5 primeiros colocados são: {times[:5]}")
print("\n" + f"Os 4 últimos colocados são: {times[-4:]}")
print("\n" + f"Os times em ordem alfabética são: {sorted(times)}")

pos = times.index("Flamengo") + 1
print("\n" + f"O time do Flamengo está na {pos}ª posição." + "\n")
