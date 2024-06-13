import sys


def main():
    while true:
    
    sys.stdout.write("$ ")
    sys.stdout.flush()

    # Wait for user input
    command=input()
    """no_space=command.strip()
    if no_space:
        cmd=no_space.split()
        cmd1=cmd[0]"""
    sys.stdout.write(f"{command}: command not found\n")
    


if __name__ == "__main__":
    main()
