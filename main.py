from logic_module import Calculate_grade
from input_module import get_student_data
from output_module import display_result

Student_name,Student_score=get_student_data()
grade=Calculate_grade(Student_score)
display_result(Student_name,Student_score,grade)
