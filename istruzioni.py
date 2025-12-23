# 1. VARIABILI E TIPI DI DATO
nome = "Andrea"
eta = 25
altura = 1.75
attivo = True

# 2. OPERATORI ARITMETICI
somma = 10 + 5
differenza = 10 - 5
prodotto = 10 * 5
divisione = 10 / 5
potenza = 2 ** 3
resto = 10 % 3

# 3. CONDIZIONALI
if eta >= 18:
    print("Maggiorenne")
elif eta >= 13:
    print("Adolescente")
else:
    print("Minore")

# 4. CICLI
# Ciclo for
for i in range(5):
    print(f"Iterazione {i}")

# Ciclo while
contatore = 0
while contatore < 3:
    print(f"Contatore: {contatore}")
    contatore += 1

# 5. LISTE
numeri = [1, 2, 3, 4, 5]
numeri.append(6)
numeri.pop(0)

# 6. DIZIONARI
persona = {
    "nome": "Andrea",
    "eta": 25,
    "citta": "Milano"
}

# 7. FUNZIONI
def saluta(nome):
    return f"Ciao {nome}!"

risultato = saluta("Andrea")
print(risultato)

# 8. STRINGHE
testo = "Python è fantastico"
print(testo.upper())
print(testo.split())

# 9. ECCEZIONI
try:
    valore = 10 / 0
except ZeroDivisionError:
    print("Errore: divisione per zero")