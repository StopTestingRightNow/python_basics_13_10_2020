time = int(input("Введите время: "))
time = time % 86400

print(f"Текущее время - {(time//3600):02}:{((time%3600)//60):02}:{((time%3600)%60):02}")
