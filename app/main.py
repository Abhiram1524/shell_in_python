import sys


def main():
    
    sys.stdout.write("$ ")
    sys.stdout.flush()

    # Wait for user input
    input()
    command=input()
    """no_space=command.strip()
    if no_space:
        cmd=no_space.split()
        cmd1=cmd[0]"""
    sys.stdout.write(f"{command}: command not found\n")
    


if __name__ == "__main__":
    main()
