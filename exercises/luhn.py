class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.replace(' ', '')
        if self.card_num.isdigit():
            self.card_num = [int(num) for num in self.card_num]
        else:
            self.card_num = ['0']

    def valid(self):
        # Invalid if one digit
        if len(self.card_num) == 1:
            return False
        # Doubling every second digits from the right
        else:
            summation = 0
            for idx, num in enumerate(reversed(self.card_num)):
                # multiply by 1 for odd index and 2 for even
                if idx % 2 == 0:
                    num *= 1
                else:
                    num *= 2
                # minus by 9 if num is greater than 9
                if num > 9:
                    num -= 9
                else:
                    num = num
                summation += num

            # check if summation is evenly divisible by 10
            if summation % 10 == 0:
                return True
            else:
                return False


print(Luhn("234 567 891 234").valid())
