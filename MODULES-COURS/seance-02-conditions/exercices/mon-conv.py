temperature = float(input("Entrez la température : "))
unite = input("Est-ce en C ou F ? ").upper()

if unite == "C":
    fahrenheit = (temperature * 9/5) + 32
    print(f"{temperature}°C = {fahrenheit}°F")
elif unite == "F":
    celsius = (temperature - 32) * 5/9
    print(f"{temperature}°F = {celsius}°C")
else:
    print("Unité non reconnue")