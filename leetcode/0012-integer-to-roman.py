class Solution:
    def intToRoman(self, num: int) -> str:
        result = ''

        if num // 1000 > 0:
            result += (num // 1000) * 'M'
            num = num % 1000
        
        if num // 100 == 9:
            result += 'CM'
            num -= 900
        if num // 100 >= 5:
            result += 'D'
            num -= 500
        if num // 100 == 4:
            result += 'CD'
            num -= 400
        if num // 100 > 0:
            result += (num // 100) * 'C'
            num = num % 100
        
        if num // 10 == 9:
            result += 'XC'
            num -= 90
        if num // 10 >= 5:
            result += 'L'
            num -= 50
        if num // 10 == 4:
            result += 'XL'
            num -= 40
        if num // 10 > 0:
            result += (num // 10) * 'X'
            num = num % 10
        
        if num == 9:
            result += 'IX'
            num -= 9
        if num >= 5:
            result += 'V'
            num -= 5
        if num == 4:
            result += 'IV'
            num -= 4
        if num > 0:
            result += num * 'I'
        
        return result
