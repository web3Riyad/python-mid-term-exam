class Star_Cinema:
    hall_list = []

    def entry_hall(self, hall):
        self.hall_list.append(hall)

class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no) -> None:
        super().__init__()
        self.__seats = {}
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        hall_info = {"rows": rows, "cols": cols, "hall_no": hall_no}
        self.entry_hall(hall_info)

    def entry_show(self, show_id, movie_name, time):
        show = (show_id, movie_name, time)
        self.show_list.append(show)
        seat = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        self.__seats[show_id] = seat

    def print_seats(self, show_id):
        if show_id in self.__seats:
            for row in self.__seats[show_id]:
                print(' '.join(str(seat) for seat in row))
        else:
            print(f"No seats found for show ID: {show_id}")

    def book_seats(self, show_id, row, col):
        if show_id in self.__seats:
            if row<5 and col<5:
                if self.__seats[show_id][row][col] == 0:
                    self.__seats[show_id][row][col] = 1
                    print(f"Seat at row {row+1}, col {col+1} booked successfully.")
                else:
                    print(f"Seat at row {row+1}, col {col+1} is already booked!")
            else:
                print("Seat number is out of range")
        else:
            print(f"No seats found for show ID: {show_id}")

def main():

    hall_1 = Hall(5, 5, 000)
    hall_1.entry_show(100, 'Movie_1', "25/8/24 11:00 PM")
    hall_1.entry_show(100, "movie_2", "25/8/24 08:00 PM")
    hall_1.entry_show(101, "movie_3", "25/8/24 10:00 AM")
    hall_1.entry_show(101, "movie_4", "25/8/24 03:00 PM")


    while True:
        print("1) VIEW ALL SHOWS TODAY")
        print("2) VIEW AVAILABLE TICKETS")
        print("3) BOOK TICKET")
        print("4) Replica for counter")
        print("5) Exit")
        take_input = int(input("ENTER OPTION : "))

        if take_input == 5:
            break
        elif take_input == 1:
            for show in hall_1.show_list:
                print(show)
        elif take_input == 2:
            check = int(input("Enter Show ID : "))
            hall_1.print_seats(check)
        elif take_input == 3 :
            show_id=int(input("Enter show id : "))
            ticket_need=int(input("Enter quantity of ticket : "))
            for i in range(ticket_need):
                row_seat=int(input("Enter Row : "))
                col_seat=int(input("Enter col : "))
                hall_1.book_seats(show_id,row_seat,col_seat)
        elif take_input == 4 :
            running_show_list=[]
            cur_time=input("Enter current time like (25/8/24 11:00 PM) : ")
            for show in hall_1.show_list:
                if cur_time==show[2]:
                    print(show)
                    if show[0] not in running_show_list:
                        running_show_list.append(show[0])
                    for running in running_show_list:
                        hall_1.print_seats(running)

                    ans=input("Are you interested to buy a ticket : ")
                    if ans == "YES":
                        show_id=int(input("Enter show id : "))
                        ticket_need=int(input("Enter number ticket : "))
                        for i in range(ticket_need):
                            row_seat=int(input("Enter Row : "))
                            col_seat=int(input("Enter col : "))
                            hall_1.book_seats(show_id,row_seat,col_seat)
                    else:
                        break

                else:
                    print("There are no show running this time")
                    break

if __name__ == "__main__":
    main()
