class Student:
    def __init__(self):
        self.student_list = {}

        def check_in(self, student_name):
            if student_name in self.student_list:
                print(f"{student_name}님은 이미 출석 체크가 완료되었습니다.")
            else:
                self.student_list[student_name] = '출석'
                print(f"{student_name}님의 출석이 기록되었습니다.")

        def view_student(self):
            if not self.student_list:
                print("아직 출석한 학생이 없습니다.")
            else:
                print("/n현재 출석 명단:")
                for student, status in self.student_list.items():
                    print(f"{student}: {status}")

        def run(self):
            print("학생 출석 관리 시스템입니다.")
            while True:
                print("/n 1: 출석 체크")
                print("2: 출석 기록 조회")
                print("3: 종료")
                choice = input("원하는 직업을 선택하세요: ")

                if choice == "1":
                    student_name = input("학생 이름을 입력하세요: ")
                    self.check_in(student_name)
                elif choice == "2":
                    self.view_student()
                elif choive == "3":
                    print("출석 관리 시스템을 종료합니다.")
                    break
                else:
                    print("잘못된 입력입니다. 다시 시도해주세요.")