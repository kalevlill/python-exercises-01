def celsius_to_fahrenheit(celsius):
    fahrenheit = (9/5) * celsius +32
    return fahrenheit

celsius_temp = 10 # jede Celsius Temp kann man hier einfuegen
fahrenheit_temp = celsius_to_fahrenheit(celsius_temp)

print(f"{celsius_temp}°C entspricht {fahrenheit_temp}°F")
