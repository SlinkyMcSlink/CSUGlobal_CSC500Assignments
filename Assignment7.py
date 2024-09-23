
room_numbers = dict()
instructors = dict()
class_times = dict()

# CSC101
room_numbers['CSC101'] = 3004
instructors['CSC101'] = 'Haynes'
class_times['CSC101'] = '8:00 a.m.'

# CSC102
room_numbers['CSC102'] = 4501
instructors['CSC102'] = 'Alvarado'
class_times['CSC102'] = '9:00 a.m.'

# CSC103
room_numbers['CSC103'] = 6755
instructors['CSC103'] = 'Rich'
class_times['CSC103'] = '10:00 a.m.'

# NET110
room_numbers['NET110'] = 1244
instructors['NET110'] = 'Burke'
class_times['NET110'] = '11:00 a.m.'

# COM241
room_numbers['COM241'] = 1411
instructors['COM241'] = 'Lee'
class_times['COM241'] = '1:00 p.m.'

course = input('Hello, What course would you like the information for?\n')
while course != 'q': 
    if course in room_numbers.keys():
        print('The course: {} is in room {} at {} and taught by Professor {}'.format(course, room_numbers[course], class_times[course], instructors[course]))
    else:
        print('You have not ented a valid class...')
    course = input('Enter next course for information or \'q\' to quit.\n')
