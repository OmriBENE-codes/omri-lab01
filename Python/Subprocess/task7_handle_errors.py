#Handling Command Errors Gracefully
import subprocess

def run_command(command):
    try:
        result = subprocess.run(command, capture_output=True, text=True, check=True)
        output = result.stdout
        print("command executed!")
        print("output: ", output)

    except subprocess.CalledProcessError as er:
        print(f'Error: The command faild to execute {er.returncode}')
        print(f'Error output: {er.stderr}')

    except FileNotFoundError:
        print(f'Error: The command {command[0]} was not found.')

    except Exception:
        print(f'An unexpected error occured: {er}')

command = ['ls', '/nonexistent-directory'] #Example of a command that will fail
command = ['ls', 'C://Users//USER//Python//omri-lab01//Python//Subprocess']
run_command(command)

