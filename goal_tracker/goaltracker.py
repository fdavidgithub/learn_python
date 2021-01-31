"""
GoalTracker - Command Line Interface

Usage:
    goaltracker.py -s | --show
    goaltracker.py -h | --help
    goaltracker.py -v | --version
"""
from datastructs import TreeNode
from extra import build
import sys

def version():
    print("GoalTracker version beta")

def help():
    print(__doc__)

def show():
    goal = build()
    goal.printTree()
 
def main():
    args = sys.argv[1:]

    if args:
        for arg in args:
            if arg in ("-h", "--help"):
                help()
                break
            elif arg in ("-v", "--version"):
                version()
                break
            elif arg in ("-s", "--show"):
                show()
                break
    else:
        help()
        
   
if __name__ == '__main__':
    main() 


