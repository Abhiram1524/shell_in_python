import sys
import os

# Define a set of built-in commands
commands = {"exit", "echo", "type"}

def main():
    while True:
        sys.stdout.write("$ ")
        sys.stdout.flush()
        command = input().strip()
        cmd = command.split()
        
        if command == "exit 0":
            sys.exit(0)
        elif cmd[0] == "echo":
            sys.stdout.write(" ".join(cmd[1:]) + "\n")
        elif cmd[0] == "type":
            if len(cmd) > 1:
                target_command = cmd[1]
                if target_command in commands:
                    sys.stdout.write(f"{target_command} is a shell builtin\n")
                else:
                    found = False
                    for path_org in os.environ.get("PATH", "").split(":"):
                        example = os.path.join(path_org, target_command)
                        if os.access(example, os.X_OK):
                            sys.stdout.write(f"{target_command} is {example}\n")
                            found = True
                            break
                    if not found:
                        sys.stdout.write(f"{target_command}: not found\n")
            else:
                sys.stdout.write("type: usage: type command\n")
        else:
            sys.stdout.write(f"{command}: command not found\n")

if __name__ == "__main__":
    main()
