import subprocess

with open("myfile.py", "at") as outf:
    subprocess.Popen(["tesseract", "skeat_400.png", "skeat"])

    
