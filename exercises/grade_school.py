class School:

    def __init__(self):
        pass
        self.school_dict = {}

    def add_student(self, name, grade):
        if grade not in self.school_dict:
            self.school_dict[grade] = [name]
        else:
            self.school_dict[grade].append(name)
            self.school_dict[grade] = sorted(self.school_dict[grade])

    def roster(self):
        if not self.school_dict:
            return []
        else:
            grades = sorted([*self.school_dict.keys()])
            names = []
            for grade in grades:
                names.append(self.school_dict[grade])
            return [item for sublist in names for item in sublist]

    def grade(self, grade_number):
        if grade_number not in self.school_dict:
            return []
        else:
            return list(self.school_dict[grade_number])

