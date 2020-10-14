time = int(input("Введите время: "))
time = time % 86400

hours = time // 3600
minutes = (time % 3600) // 60
seconds = (time % 3600) % 60

print(f"Текущее время - {hours:02}:{minutes:02}:{seconds:02}")
