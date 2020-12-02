plants_dict = {
    'G': 'Grass',
    'C': 'Clover',
    'R': 'Radishes',
    'V': 'Violets'
}

student_list = ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Fred', 'Ginny', 'Harriet', 'Ileana', 'Joseph', 'Kincaid', 'Larry']


class Garden:
    def __init__(self, diagram, students=None):
        self.diagram = diagram
        if students is None:
            self.students = student_list
        else:
            self.students = students

    def plants(self, student):
        sorted_students = sorted(self.students * 2, key=str.lower)
        plants_list = []
        for string in self.diagram.split():
            idx = sorted_students.index(student)
            plants_list.append(plants_dict.get(string[idx]))
            plants_list.append(plants_dict.get(string[idx+1]))
        return plants_list


garden = Garden("VCRRGVRG\nRVGCCGCV", students=["Samantha", "Patricia", "Xander", "Roger"])
print(garden.plants("Patricia"))
