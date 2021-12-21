with open(r'Python\Advent of Code\2020\day5input') as f:
    seats = f.read().split()

#first star
def foo(seats, seat_ids=[]):
    for seat in seats:
        row, column = seat[:-3], seat[-3:]
        row = int(''.join(['1' if i == 'B' else '0' for i in row]),2)
        column =  int(''.join(['1' if i == 'R' else '0' for i in column]),2)
        seat_ids.append(row*8+column)
    return seat_ids

print('The highest seat ID:', max(foo(seats)))

#second star
def doo(seats, my_seat = 0):
    seats = foo(seats)
    for seat_num in range(min(seats), max(seats)):
        if seat_num not in seats:
            return seat_num

print('My seat ID:', doo(seats))