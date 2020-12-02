def convert_hour(minute):
    return int(minute // 60) % 24


class Clock:
    def __init__(self, hour, minute):
        self.minute = hour*60 + minute

    def __repr__(self):
        return f'{str(convert_hour(self.minute)).zfill(2)}:{str(self.minute % 60).zfill(2)}'

    def __eq__(self, other):
        return repr(self) == repr(other)

    def __add__(self, minutes):
        self.minute += minutes
        self.hour = convert_hour(self.minute)
        return self

    def __sub__(self, minutes):
        self.minute -= minutes
        self.hour = convert_hour(self.minute)
        return self


print(Clock(14, 37) == Clock(15, 37))
