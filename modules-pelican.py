import subprocess

def current_state:
    return "cool"

def generate(output,name):
    subprocess.call(['pelican', '-o', output, name])
    return "Whoopee!"
