import subprocess
import os

computer = "whoami"
ipa = "ifconfig"
lshw = "lshw -short"

print("Who am I?")
os.system(computer)
print("What is my network configuration?")
subprocess.run(ipa)
print("What is my type of hardware?")
os.system(lshw)