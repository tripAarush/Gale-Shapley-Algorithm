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
                    num_proposals += 1
            
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
                else:
                    self.free_hospitals.remove(hospital)
        
        return self.matches
    
    def get_num_proposals(self):
        return self.num_proposals

