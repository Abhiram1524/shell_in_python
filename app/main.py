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
            elif:
                found=False
                for path_org in os.environ.get("PATH","").split(":"):
                    example=os.path.join(path_org,cmd[1])
                    if os.access(example,os.X_OK):
                        sys.stdout.write(f"{cmd[1]} is {example}\n")
                        found=True
                        break
                    
            else:
                sys.stdout.write(f"{cmd[1]}: not found\n")
        else:
            sys.stdout.write(f"{command}: command not found\n")
        
    


if __name__ == "__main__":
    main()
