from subtest import Estudyante

studyante1 = Estudyante("Calcifer", "Philosophy", 3.8, True)
print("Student's name: " + studyante1.name)
print("Student's major: " + studyante1.major)
print("Student's gpa: " + str(studyante1.gpa))
if studyante1.gpa >= 3.5:
    print(studyante1.name + " is on honor roll")
else:
    print("Student not on honor roll")