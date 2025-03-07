import os

print(os.listdir())

with open("new_file.txt", "w") as f:
    f.write("Hello World")

print(os.listdir())

os.remove("new_file.txt")
print(os.listdir())


# 結果:
# >>>
# ['boot.py']
# 11
# ['boot.py', 'new_file.txt']
# ['boot.py']
