import random
import time
from matching import gale_shapley
from verifier import verifier
import matplotlib.pyplot as plt
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
    
    return hospital_prefs, student_prefs

def matching_test(n):
    hospital_prefs, student_prefs = generate_random_input(n)

    start = time.time()
    gs = gale_shapley(hospital_prefs, student_prefs)
    matching = gs.match()
    matching_time = time.time() - start

    return matching_time

def verifier_test(n):
    hospital_prefs, student_prefs = generate_random_input(n)
    gs = gale_shapley(hospital_prefs, student_prefs)
    matching = gs.match()

    start = time.time()
    verifier(hospital_prefs, student_prefs, matching)
    verifier_time = time.time() - start

    return verifier_time

def graph(sizes, matcher_time, verifier_time):
    plt.figure(figsize=(10,6))

    plt.plot(sizes, matcher_time, marker = 'o', linewidth = 2, label = 'Matcher', color = 'pink')
    plt.plot(sizes, verifier_time, marker = 'o', linewidth = 2, label = 'Matcher', color = 'green')
    plt.xlabel('n (size of the set)', fontsize = 12)
    plt.ylabel('Run time (s)', fontsize = 12)
    plt.title('Scability', fontsize = 14)

    plt.savefig("scabilityGraph.jpg")



if __name__ == "__main__":
    with open("input_test.txt", "w") as f:
        n = 9 # example
        hospital_prefs, student_prefs = generate_random_input(n)
        
        # keeping the input format by mapping list values to string
        f.write(f"{n}\n")
        for i in range(1, n + 1):
            f.write(" ".join(map(str, hospital_prefs[i])) + "\n")
        for i in range(1, n + 1):
            f.write(" ".join(map(str, student_prefs[i])) + "\n")