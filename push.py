import os
os.system("git add .")
a = str(input("\033[1;33;40m what did u do? \033[1;32m"))
os.system("git commit -m "+ a)
os.system("git push -f origin master")