import sys
commands={"exit","echo","type"}


def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        command=input().strip()
        cmd=command.split()
        if command=="exit 0":
            sys.exit(0)
        elif cmd[0]=="echo":
            sys.stdout.write(" ".join(cmd[1:]) + "\n")
        elif cmd[0]=="type":
            if cmd[1] in commands:
                sys.stdout.write(f"{cmd[1]} is a shell builtin\n")
            else:
                sys.stdout.write(f"{cmd[1]}: not found\n")
        else:
            sys.stdout.write(f"{command}: command not found\n")
        
    


if __name__ == "__main__":
    main()
