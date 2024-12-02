class Movie:
    def __init__(self, title, showtime, seats=10):
        self.title = title
        self.showtime = showtime
        self.seats = ["O"] * seats

    def reserve_seat(self, seat_number):

        if 0 <= seat_number < len(self.seats):
            if self.seats[seat_number] == "O":
                self.seats[seat_number] = "X"
                print(f"{seat_number + 1}번 좌석이 예약되었습니다.")
            else:
                print(f"{seat_number + 1}번 좌석은 이미 예약되었습니다.")
        else:
            print("잘못된 좌석 번호입니다.")

    def view_seats(self):
        # 현재 좌석 상태 출력
        print(f"\n영화 제목: {self.title} | 상영 시간: {self.showtime}")
        print("좌석 상태: ", " ".join(self.seats))



class CinemaReservationSystem:
    def __init__(self):
        self.movies = []

    def add_movie(self, title, showtime, seats=10):

        movie = Movie(title, showtime, seats)
        self.movies.append(movie)
        print(f"영화 '{title}'이(가) 상영 시간 '{showtime}'로 추가되었습니다.")

    def select_movie(self, title):

        for movie in self.movies:
            if movie.title == title:
                return movie
        print("해당 영화가 없습니다.")
        return None

    def run(self):

        print("영화관 예약 시스템입니다.")
        while True:
            print("\n1: 영화 추가")
            print("2: 영화 좌석 예약")
            print("3: 영화 좌석 조회")
            print("4: 종료")
            choice = input("원하는 작업을 선택하세요: ")

            if choice == "1":
                title = input("영화 제목을 입력하세요: ")
                showtime = input("상영 시간을 입력하세요 (예: 18:30): ")
                seats = int(input("좌석 수를 입력하세요: "))
                self.add_movie(title, showtime, seats)
            elif choice == "2":
                title = input("예약할 영화 제목을 입력하세요: ")
                movie = self.select_movie(title)
                if movie:
                    movie.view_seats()
                    seat_number = int(input("예약할 좌석 번호를 입력하세요: ")) - 1
                    movie.reserve_seat(seat_number)
            elif choice == "3":
                title = input("조회할 영화 제목을 입력하세요: ")
                movie = self.select_movie(title)
                if movie:
                    movie.view_seats()
            elif choice == "4":
                print("영화관 예약 시스템을 종료합니다.")
                break
            else:
                print("잘못된 입력입니다. 다시 시도해주세요.")