class Student:
    def __init__(self):
        self.grades = {}

        def add_student_grade(self, student_name, subject, score):
            if student_name not in self.grades:
                self.grades[student_name] = {}
            self.grades[student_name][subject] = score
            print(f"{student_name}님의 {subject} 과목 성적이 {score}점으로 기록되었습니다.")

        def view_student_grades(self, student_name):
            if student_name not in self.grades:
                print(f"f{student_name}님의 성적 기록이 없습니다.")
            else:
                subjects = self.grades[student_name]
                total_score = sum(subjects.values())
                average_score = total_score / len(subjects)
                print(f"/n{student_name}님의 성적:")
                for subjects, score in subjects.items():
                    print(f"{subjects}: {score}점")
                print(f"평균점수: {average_score:.2f}점")

        def view_all_grades(self):
            if not self.grades:
                print("아직 기록된 성적이 없습니다.")
            else:
                print("/n 전체 학생 성적 목록:")
                for student, subjects in subjects.items():
                    print(f"평균 점수: {average_score:.2f}점")

        def run(self):
            print("학생 성적 관리 시스템입니다.")
            while True:
                print("/n: 성적 추가")
                print("2: 특정 학생 성적 조회")
                print("3: 전체 학생 성적조회")
                print("4: 종료")
                choice = input("원하는 직업을 선택하세요:")

            if choice == "1":
                student_name = input("학생 이름을 입력하세요: ")
                subject = input("과목을 입력하세요:")
                score = float(input(f"{subject} 과목의 점수를 입력하세요: "))
                self.add_student_grade(student_name, subject, score)
            elif choice == "2":
                student_name = input("조회할 학생 이름을 입력하세요: ")
                self.view_all_grade()
            elif choice == "3":
                self.view_all_grade
            elif choice == "4":
                print("성적 관리 시스템을 종료합니다.")
