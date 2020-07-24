# DATA
unit_symbol = "℃"
unit_name = "celsius"

# METEO DATA 4 TIMES A DAY
locality_name = "Chisinau"
date = "24.07.2020"
temp_mo = 10.91
temp_no = 30.68
temp_ev = 25.11
temp_ni = 6.32

# CALCULATIONS
temp_avg = (temp_mo + temp_no + temp_ev + temp_ni) / 4
# prima metoda de a rotungi cifrele cu fractie, utilizarea //4 in loc de /4
# rotungirea spre suma fixa
temp_min = min(temp_mo,  temp_no, temp_ev, temp_ni)
temp_max = max(temp_mo, temp_no, temp_ev, temp_ni)
is_hot_day = temp_no >= 25
is_cold_night = temp_ni < 10
hot_24h = (is_cold_night is False) and (is_hot_day is True)
# daca noaptea nu este mai putin de 10 grade si ziua este mai mult de 25,
# atunci vom avea True, in caz contrat False

# PRESENTATION
print(" 🌨   ☼  🌤  "*5)
print("Locality: " + locality_name)
print("Date:     " + date)
print("avg Temp: " + str(round(temp_avg, 1)) + unit_symbol)
# print("avg Temp: ", int(temp_avg), unit_symbol)
# a doua metoda convertarea in tipul int, rotungirea spre suma fixa
print("min Temp: " + str(round(temp_min, 1)) + unit_symbol)
print("max Temp: " + str(round(temp_max, 1)) + unit_symbol)
# a treia metoda folosirea la rezultatul final a functiei round()
# rotungirea spre suma mai apropiata
print("Hot day?: " + str(is_hot_day))
print("Cold night?: " + str(is_cold_night))
print("Hot during 24 hour?: " + str(hot_24h))
print(" 🌨   ☼  🌤  "*5)
