import os
import subprocess

TOOLS = [
    'git',
    'notion-mcp'
]

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

def main():

    # Attend stop notion-mcp
    subprocess.run(
        ['docker', 'compose', 'down'],
        cwd=os.path.join(BASE_DIR, 'services', 'notion')
    )



if __name__ == "__main__":
    main()