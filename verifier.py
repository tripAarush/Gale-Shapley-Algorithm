# need to verify if a match is valid and stable and return true if so
def validity_checker(hospital_prefs, student_prefs, matches):
    n = len(hospital_prefs)

    if len(matches) != n:
        print(f"INVALID: Expected {n} matches does not match recieved amount of {len(matches)}")
        return False
    
    for hospital in range(1, n + 1):
        if hospital not in matches:
            print(f"INVALID: Hospital {hospital} does not have a match")
            return False

    # if hospitals are matched exactly once -> any duplicates    
    students_matched = []
    for hospital, student in matches.items():
        students_matched.append(student)

    if len(set(students_matched)) != n:
        print(f"INVALID: Student {student} is matched more than once")
        return False
        
    for student in range(1, n + 1):
        if student not in students_matched:
            print(f"INVALID: Student {student} does not have a match")
            return False
        
    return True

def stability_checker(hospital_prefs, student_prefs, matches):  
    reverse_sToh = {s: h for h, s in matches.items()}
    n = len(matches)
    for h in range(1, n + 1):
        for s in range(1, n + 1):
            if matches[h] == s:
                continue
            h_match = matches[h]
            s_match = reverse_sToh[s]

            h_pref = hospital_prefs[h].index(s) < hospital_prefs[h].index(h_match)
            s_pref = student_prefs[s].index(h) < student_prefs[s].index(s_match)

            if h_pref and s_pref:
                print(f"UNSTABLE PAIR: Hospital {h}, Student {s}")
                return False
    
    return True
            
def verifier(hospital_prefs, student_prefs, matches):
    if not validity_checker(hospital_prefs, student_prefs, matches):
        return False
    
    if not stability_checker(hospital_prefs, student_prefs, matches):
        return False
    
    print("VALID STABLE")
    return True

if __name__ == "__main__":
    hospital_prefs = {}
    student_prefs = {}

    with open("input_test.txt", "r") as f:
        lines = f.readlines()

    if len(lines) == 0:
        print("INVALID INPUT: Input is empty.")
    
    if len(lines[0].strip()) == 0:
       print("INVALID INPUT: First line is empty")
       exit()

    n = int(lines[0].strip())

    if len(lines) != 2 * n + 1:
        print("INVALID INPUT: Hospital and student preferences amount are not equal OR extra whitespaces are detected")
        exit()
    
    for i in range(1, len(lines)):
        if i <= n:
            hospital_prefs[i] = list(map(int, lines[i].strip().split()))
        else:
            student_prefs[i - n] = list(map(int, lines[i].strip().split()))

    matches = {}

    with open("output_test.txt", "r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("Number"):
                contintue
                
            converting = line.split()

            if len(converting) == 2:
                hospital = int(converting[0])
                student = int(converting[1])
                matches[hospital] = student
    
    print("Verifying matching results")
    verifier(hospital_prefs, student_prefs, matches)