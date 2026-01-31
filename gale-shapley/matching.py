class gale_shapley:
    def __init__(
        self,
        hospital_prefs: dict,
        student_prefs: dict,
    ):
        self.hospital_prefs = hospital_prefs
        self.student_prefs = student_prefs
        self.free_hospitals = list(hospital_prefs.keys())
        self.proposals = {hospital: [] for hospital in hospital_prefs}
        self.matches = {}
        self.num_proposals = 0
    
    def match(self):
        while self.free_hospitals:
            hospital = self.free_hospitals[0]
            hospital_pref_list = self.hospital_prefs[hospital]
            
            for student in hospital_pref_list:
                if student not in self.proposals[hospital]:
                    self.proposals[hospital].append(student)
                    self.num_proposals += 1
            
                    if student not in self.matches:
                        self.matches[student] = hospital
                        self.free_hospitals.remove(hospital)
                        break
                    else:
                        current_hospital = self.matches[student]
                        student_pref_list = self.student_prefs[student]
                        
                        if student_pref_list.index(hospital) < student_pref_list.index(current_hospital):
                            self.matches[student] = hospital
                            self.free_hospitals.remove(hospital)
                            self.free_hospitals.append(current_hospital)
                            break
        
        return self.matches
    
    def get_num_proposals(self):
        return self.num_proposals

if __name__ == "__main__":
    hospital_prefs = {}
    student_prefs = {}
    with open("input_test.txt", "r") as f:
        lines = f.readlines()
    
    if len(lines) == 0:
        print('INVALID INPUT: Input is empty.'
    )
    if not lines[0].strip().isdigit():
        print('INVALID INPUT: First line must contain a single integer.')
        exit()
    else:
        n_check = int(lines[0].strip())

    if len(lines) != 2 * n_check + 1:
        print('INVALID INPUT: Uneven hospital and student preferences OR extra whitespace detected.')

    for i in range(1, len(lines)):
        if i <= n_check:
            hospital_prefs[i] = list(map(int, lines[i].strip().split()))
        else:
            student_prefs[i - n_check] = list(map(int, lines[i].strip().split()))

    gs = gale_shapley(hospital_prefs, student_prefs)
    matches = gs.match()
    num_proposals = gs.get_num_proposals()
    
    # output in the given format
    with open('output_test.txt', 'w') as f:
        for student, hospital in matches.items():
            f.write(f"{hospital} {student}\n")

    print("Number of proposals:", num_proposals)

