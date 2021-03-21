import os
import subprocess
import sys

# Runs a single game
def run_single_game(process_command):
    print("Start run a match")
    p = subprocess.Popen(
        process_command,
        shell=True,
        stdout=sys.stdout,
        stderr=sys.stderr
        )
    # daemon necessary so game shuts down if this script is shut down by user
    p.daemon = 1
    p.wait()
    print("Finished running match")

# Get location of this run file
parent_dir = os.path.abspath(os.path.dirname(os.path.realpath(__file__)))

# Get if running in windows OS
is_windows = sys.platform.startswith('win')
print("Is windows: {}".format(is_windows))
algo2 = None

# If script run with params, use those algo locations when running the game
if len(sys.argv) > 1:
    algo1 = sys.argv[1]
if len(sys.argv) > 2:
    algo2 = sys.argv[2]
if algo2 is None:
    print('No enough algos provided, EXITTING')
    exit()

# If folder path is given instead of run file path, add the run file to the path based on OS
# trailing_char deals with if there is a trailing \ or / or not after the directory name
if is_windows:
    if "run.ps1" not in algo1:
        trailing_char = "" if algo1.endswith("\\") else "\\"
        algo1 = algo1 + trailing_char + "run.ps1"
    if "run.ps1" not in algo2:
        trailing_char = "" if algo2.endswith("\\") else "\\"
        algo2 = algo2 + trailing_char + "run.ps1"
else:
    if "run.sh" not in algo1:
        trailing_char = "" if algo1.endswith('/') else "/"
        algo1 = algo1 + trailing_char + "run.sh"
    if "run.sh" not in algo2:
        trailing_char = "" if algo2.endswith('/') else "/"
        algo2 = algo2 + trailing_char + "run.sh"

algo1 = os.path.join(os.pardir, 'algos', algo1)
algo2 = os.path.join(os.pardir, 'algos', algo2)

print("Algo 1: ", algo1)
print("Algo 2:", algo2)

run_single_game("cd {} && java -jar engine.jar work {} {}".format(parent_dir, algo1, algo2))