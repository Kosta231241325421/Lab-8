#Lab 8.2
import os
x=input('Ввести файл  ')
dir, name=os.path.split(x)
file_name, form=os.path.splitext(name)
print("Info:")
print("Шлях:",dir)
print("Ім'я:",name)
print("Формат:",form)

