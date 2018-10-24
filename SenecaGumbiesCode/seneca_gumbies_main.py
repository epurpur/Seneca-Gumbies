import Seasons_of_year as sy
import seneca_actions as sa
import time
import sys


def main():
    print("~~~~~~~~~~SENECA GUMBIES~~~~~~~~~~~")
    time.sleep(2)
    print("Today you have a day off and get to climb at Seneca. How good this day is depends on a lot of factors including weather, day of the week, etc.")

    sy.current_season()

def finish():
    print(f"Today you climbed the following routes: {sa.routes_climbed}")
    print(f"Today you climbed {sa.pitches_climbed} pitches.")
    print(f"Your energy levels are at {sa.energy_level}")
    sys.exit

if __name__ == '__main__':
    main()

