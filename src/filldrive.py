#!/usr/bin/python3
'''
This program creates a number of file with certain size automatically
'''
import sys
import random
import time
import begin


def pickrandcharater():
    '''pick a random character from the ascii table'''

    random_ascii_value = random.randint(32, 126)
    return chr(random_ascii_value)



def get_unit_size(unit):
    '''Determine the size based on the units'''
    unit = unit.upper()

    if unit in ['B']:
        return 1
    elif unit in ['K', 'KB']:
        return 1024
    elif unit in ['M', 'MB']:
        return 1024 * 1024
    elif unit is 'G' or unit is 'GB':
        return 1024 * 1024 * 1024
    elif unit in ['T', 'TB']:
        return 1024 * 1024 * 1024 * 1024
    else:
        raise Exception('Unrecognize unit')


def generate_file(filename, unit, size):
    '''generate the file'''
    size = size * get_unit_size(unit)

    try:
        file = open(filename, mode='w', buffering=1024)

        for file_iteration in range(0, size):
            file.write(pickrandcharater())
    finally:
        file.close()


# if __name__ == "__main__":
if begin.start():
    pass

@begin.start(auto_convert=True)
def run(filename='filldrive.fll',
        size=1,
        unit='B',
        count=1,
        interval=1,
        silent=True):
    '''
    The filldrive script allows you to create text files
    in your system based on specific requirements
    '''

    cursor_animation = ['-', '\\', '|', '/', '-', '\\', '|', '/']
    for i in range(0, count):
        generate_file(filename + str(i), unit, size)

        if not silent:
            sys.stdout.write(cursor_animation[i % len(cursor_animation)])
            sys.stdout.write('\b')
            sys.stdout.flush()

        time.sleep(interval)
