import sys
from console.runner import run

def main():
    if len(sys.argv) < 2:
        print("Usage: ctrans <command>")
        return
    run(sys.argv[1:])

if __name__ == "__main__":
    main()
