from datetime import datetime
import sys

def solution():
    date = datetime.today()
    sys.stdout.write('%d\n%d\n%d\n'%(date.year, date.month, date.day))

if __name__ == '__main__':
    solution()