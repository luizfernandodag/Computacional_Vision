import os
os.system('cls')
os.listdir()

actual_dir = os.getcwd()
print(actual_dir)

os.chdir(r'C:\Users\Luiz\Documents\A-Cursos\A-Fazendo agora\3-\Asimov\Visão Computacional\Computacional_Vision')
os.chdir(actual_dir)
#os.mkdir('pasta2')
print(os.getcwd())

#os.rename('teste.txt','teste2.txt')
os.remove('teste.csv')
