class RomanNumerals:
    rom = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
    num = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

    @staticmethod
    def to_roman(number):
        r = ''
        i = 0
        while number:
            t = number // RomanNumerals.num[i]
            number %= RomanNumerals.num[i]
            while t:
                r += RomanNumerals.rom[i]
                t -= 1
            i += 1
        return r

    @staticmethod
    def from_roman(roman_numeral):
        r = 0
        for i, v in enumerate(roman_numeral):
            t = RomanNumerals.num[RomanNumerals.rom.index(v)]
            second_num = RomanNumerals.num[RomanNumerals.rom.index(roman_numeral[i + 1])] if i + 1 != len(
                roman_numeral) else -1
            if t >= second_num:
                r += t
            else:
                r -= t
        return r