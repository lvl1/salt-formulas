import subprocess

def current_state(name):
    return (name + " is cool")

def generate(output,name):
    subprocess.call(['pelican', '-o', output, name])
    return "Whoopee!"
