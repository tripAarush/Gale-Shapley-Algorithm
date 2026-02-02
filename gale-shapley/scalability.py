import random
import time
import sys
import subprocess
import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
INPUT_FILE = BASE_DIR / "test files" / "input_test.txt"

def generate_random_input(n):
    hospitals = list(range(1, n + 1))
    students = list(range(1, n + 1))
    
    hospital_prefs = {}
    student_prefs = {}
    
    for hospital in hospitals:
        prefs = students[:]
        random.shuffle(prefs)
        hospital_prefs[hospital] = prefs
    
    for student in students:
        prefs = hospitals[:]
        random.shuffle(prefs)
        student_prefs[student] = prefs
    
    with open(INPUT_FILE, "w") as f:
        # keeping the input format by mapping list values to string
        f.write(f"{n}\n")
        for i in range(1, n + 1):
            f.write(" ".join(map(str, hospital_prefs[i])) + "\n")
        for i in range(1, n + 1):
            f.write(" ".join(map(str, student_prefs[i])) + "\n")

# returning elapsed time after running a command (each file)
def run_and_time(cmd, cwd=None):
    start = time.perf_counter()
    subprocess.run(cmd, cwd=cwd, check=True)
    end = time.perf_counter()
    return end - start

# returns lists of times for matching and verifying
def benchmark(ns, trials=5, repo_dir="."):
    match_times = []
    verify_times = []

    for n in ns:
        # generate input for this n
        generate_random_input(n)

        # keeping track of total times for averaging
        mt = 0.0
        vt = 0.0
        for _ in range(trials):
            random.seed(time.time_ns())
            generate_random_input(n)

            mt += run_and_time([sys.executable, "matching.py"], cwd=repo_dir)
            vt += run_and_time([sys.executable, "verifier.py"], cwd=repo_dir)

        match_times.append(mt / trials)
        verify_times.append(vt / trials)

        print(f"n={n}  matching={match_times[-1]}s  verifier={verify_times[-1]}s")

    return match_times, verify_times

# plotting graphs
def plot_results(ns, match_times, verify_times):
    plt.figure()
    plt.plot(ns, match_times, marker="o")
    plt.xlabel("n (hospitals/students)")
    plt.ylabel("time (seconds)")
    plt.title("Matching engine runtime")
    plt.grid(True)

    plt.figure()
    plt.plot(ns, verify_times, marker="o")
    plt.xlabel("n (hospitals/students)")
    plt.ylabel("time (seconds)")
    plt.title("Verifier runtime")
    plt.grid(True)

    plt.show()


if __name__ == "__main__":
    ns = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
    match_times, verify_times = benchmark(ns, trials=5, repo_dir=".")
    plot_results(ns, match_times, verify_times)