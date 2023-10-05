from pathlib import Path

def getProjectRoot():
    return str(Path(__file__).parent.parent)