import sys


def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        command=input()
        cmd=command.split()
        if command=="exit 0":
            sys.exit(0)
        else:
            sys.stdout.write(f"{command}: command not found\n")
    


if __name__ == "__main__":
    main()
