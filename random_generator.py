import random
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