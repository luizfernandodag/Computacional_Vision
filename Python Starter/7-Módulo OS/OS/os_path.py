import os 
os.system('cls')


d = os.getcwd()
print(f"cur dir: {d}")

d2 = os.path.join(d,'Pasta')
print(f"path2:{d2}")

ultima_pasta = os.path.basename(d2)
print(f"Ultima pasta:{ultima_pasta}")
#print(os.getcwd().split('\\'))


print(os.path.split(os.getcwd()))

#Os.path.getmtime() -> pegar timestam da última modificação
curr_dir = os.getcwd()
lt = os.path.getmtime(curr_dir)
from datetime import datetime 
print(datetime.utcfromtimestamp(lt))

#os.path.isfile()-> perguintar se é um arquivo

print(f"{curr_dir} is file?: {os.path.isfile(curr_dir)}")
