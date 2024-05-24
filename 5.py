import os
import subprocess
import shutil
import sys

# Папка, в которую будут записаны все библиотеки
output_folder = "libraries"

# Создание папки, если она не существует
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    
# Вызов команды pip для получения списка установленных библиотек
packages = subprocess.check_output([sys.executable, '-m', 'pip', 'freeze']).decode().split('\n')

# Удаление пустых строк и версий библиотек
packages = [pkg.split("==")[0] for pkg in packages if pkg]



src = "None"  # or src = None

# Проверяем, что переменная src не является пустой строкой или None
if src is not None and src != "":
    dst = os.path.join(output_folder, os.path.basename(src))
    # далее выполняем необходимые действия с переменной dst
else:
    print("Значение переменной src отсутствует или является пустым")
 


# Копирование файлов библиотек в папку
for package in packages:
    try:
        module = __import__(package)
        src = module.__file__
        dst = os.path.join(output_folder, os.path.basename(src))
        if os.path.isfile(src):
            shutil.copy(src, dst)
        else:
            shutil.copytree(src, dst)
            # Если не удалось скопировать как файл - папка
        
        print(f"Библиотека {package} успешно скопирована!")
    except ImportError as e:
        print(f"Не удалось найти модуль: {package}")

# Вывод успешного завершения
print("Все библиотеки успешно скопированы!")
