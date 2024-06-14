import sys
import os
import subprocess

# Define a set of built-in commands
commands = {"exit", "echo", "type","cd"}

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
         elif cmd[0] == "cd":
            if len(cmd) > 1:
                try:
                    os.chdir(cmd[1])
                except FileNotFoundError:
                    sys.stdout.write(f"cd: {cmd[1]}: No such file or directory\n")
                except PermissionError:
                    sys.stdout.write(f"cd: {cmd[1]}: Permission denied\n")
                except Exception as e:
                    sys.stdout.write(f"cd: {cmd[1]}: {str(e)}\n")
            else:
                sys.stdout.write("cd: usage: cd directory\n")    
        else:
            try:
                subprocess.run(cmd)
            except FileNotFoundError:
                sys.stdout.write(f"{cmd[0]}: command not found\n")
            except Exception as e:
                 sys.stdout.write(f"Error executing {cmd[0]}: {str(e)}\n")

            
    

if __name__ == "__main__":
    main()
