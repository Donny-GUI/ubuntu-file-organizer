import os

username = os.getlogin()
cc = os.getcwd()

files = os.listdir(f"/home/{username}")
myfile = "~/.bashrc"
for file in files:
	if file == "~/.bash_aliases":
		myfile = file
with open(myfile, "a") as commander:
	commander.write("\nalias cleaner='python3 ~/cleaner.py\n")
print(f"please source {myfile}")

print("after that, cleaner command should be available to you")