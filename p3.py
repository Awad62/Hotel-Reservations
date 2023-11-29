from datetime import datetime, timedelta

class BlkPrntBnb:
    def __init__(self):
        self._rooms = {}
        self._confirmations = {}
        self._confirmation_number = 0

    def add_room(self, room_number: int) -> bool:
        if room_number in self._rooms.keys():
            return False
        self._rooms[room_number] = []
        return True

    def get_rooms(self) -> dict:
        return self._rooms

    def delete_room(self, room_number: int) -> bool:
        if room_number in self._rooms.keys():
            del self._rooms[room_number]
            return True
        return False

    def reserve_room(self, room_number: int, check_in_date: str, check_out_date: str) -> tuple:
        check_in_date, check_out_date = self._convert_to_datetime(check_in_date),self._convert_to_datetime(check_out_date)
        if check_out_date - check_in_date < timedelta(1):  #
            return -1, False
        if not self._is_room_available(self._rooms[room_number], check_in_date, check_out_date):
            return -1, False
        self._confirmation_number += 1
        self._rooms[room_number].append((check_in_date, check_out_date))
        self._confirmations[self._confirmation_number] = (room_number, check_in_date, check_out_date)
        return self._confirmation_number, True 

    def get_reservation(self, confirmation_number: int) -> int:
        result = tuple()
        if confirmation_number in self._confirmations.keys():
            result = self._confirmations[confirmation_number]
        return result

    def get_room_number(self, confirmation_number: int) -> int:
        if confirmation_number in self._confirmations.keys():
            return self._confirmations[confirmation_number][0]
        return -1

    def delete_reservation(self, confirmation_number: int) -> bool:
        if confirmation_number not in self._confirmations:
            return False

        room, check_in_reservation,check_out_reservation  = self._confirmations[confirmation_number]
        reservation = check_in_reservation,check_out_reservation
        self._rooms[room].remove(reservation)
        del self._confirmations[confirmation_number]
        return True

    def get_all_reservations(self) -> list:
        result = []
        for reservation in self._confirmations.values():
            result.append(reservation)
        return result

    def get_reservation_by_room(self, room_number: int) -> list:
        return self._rooms[room_number]










    ###### helper methods ########

    def _convert_to_datetime(self, date_as_str: str) -> datetime:
        date, time = date_as_str.split()
        year, month, day = date.split('-')
        hour, minute, seconds = time.split(':')
        second, microsecond = seconds.split('.')
        return datetime(int(year), int(month), int(day), int(hour), int(minute), int(second), int(microsecond))

    def _is_room_available(self, reservations: list, requested_check_in: datetime, requested_check_out: datetime) -> bool:
        def _overlaps(curr_check_in: datetime, curr_check_out: datetime, next_check_in: datetime, next_check_out: datetime):
            return max(curr_check_in, next_check_in) <= min(curr_check_out, next_check_out)
        bookings = reservations.copy()
        bookings.append((requested_check_in, requested_check_out))
        bookings.sort(key = lambda r: r[0])
        result = [bookings[0]]
        for next_check_in, next_check_out in bookings[1:]:
            curr_check_in, curr_check_out = result[-1]
            if _overlaps(curr_check_in, curr_check_out, next_check_in, next_check_out):
                return False
            result[-1] = (next_check_in, next_check_out)
        return True


# d = '2022-11-23 23:57:28.258857'

d1 = '2022-7-10 17:00:00.0'
d2 = '2022-8-17 21:00:00.0'





bnb = BlkPrntBnb()
print(bnb.add_room(1))
print(bnb.add_room(2))
print(bnb.reserve_room(2,'2022-7-10 17:00:00.0','2022-8-17 21:00:00.0'))
print(bnb.reserve_room(1,'2022-7-10 17:00:00.0','2022-8-17 21:00:00.0'))
print(bnb.reserve_room(2,'2023-7-10 17:00:00.0','2023-8-17 21:00:00.0'))
print(bnb.get_room_number(1))
# print(bnb._confirmations)
# bnb.delete_reservation(1)
# print(bnb._confirmations)
print(bnb.get_reservation_by_room(2))
        






# x = {1 : 'a', 2 : 'b', 33 : 'c'}

# def ifits(n):
#     if n in x:
#         return True
#     return False

# print(ifits(33))

def convert_to_datetime(date_as_str: str) -> datetime:
    date, time = date_as_str.split()
    year, month, day = date.split('-')
    hour, minute, seconds = time.split(':')
    second, microsecond = seconds.split('.')
    all = [year,month,day,hour,minute,second,microsecond]
    all = next(int(a) for a in all)
    # print(all[3])
    # for x in all:
    #     print(all)
    # return datetime(year,month,day,hour,minute,second,microsecond)
    # return (all[0],all[1],all[2],all[3],all[4],all[5])
    # return datetime(int(year), int(month), int(day), int(hour), int(minute), int(second), int(microsecond))

# convert_to_datetime('2022-7-10 17:00:00.0')