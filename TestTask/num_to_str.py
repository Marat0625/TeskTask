"""
    класс преобразующий двоичное число в словосочетание
"""

class int_to_word:

    def __init__(self, number):
        self._number = int(number)

    def to_word(self):
        str_num = str(self._number)
        str_num1 = str_num[0]
        try:
            str_num2 = str_num[1]
        except:
            pass
        str_out = ''

        if len(str_num) == 1:
            if str_num1 == '0':
                str_out = 'ноль'
            elif str_num1 == '1':
                str_out = 'одна'
            elif str_num1 == '2':
                str_out = 'две'
            elif str_num1 == '3':
                str_out = 'три'
            elif str_num1 == '4':
                str_out = 'четыре'
            elif str_num1 == '5':
                str_out = 'пять'
            elif str_num1 == '6':
                str_out = 'шесть'
            elif str_num1 == '7':
                str_out = 'семь'
            elif str_num1 == '8':
                str_out = 'восемь'
            elif str_num1 == '9':
                str_out = 'девять'
        if len(str_num) == 2 & self._number < 20 & self._number > 10:
            if str_num == '10':
                str_out = 'десять'
            elif str_num == '11':
                str_out = 'одиннадцать'
            elif str_num == '12':
                str_out = 'двенадцать'
            elif str_num == '3':
                str_out = 'тринадцать'
            elif str_num == '4':
                str_out = 'четырнадцать'
            elif str_num == '5':
                str_out = 'пятнадцать'
            elif str_num == '6':
                str_out = 'шестнадцать'
            elif str_num == '7':
                str_out = 'семнадцать'
            elif str_num == '8':
                str_out = 'восемнадцать'
            elif str_num == '9':
                str_out = 'девятнадцать'
        if len(str_num) == 2:
            if str_num1 == '2':
                str_out = 'двадцать'
            elif str_num1 == '3':
                str_out = 'тридцать'
            elif str_num1 == '4':
                str_out = 'сорок'
            elif str_num1 == '5':
                str_out = 'пятьдесят'
            elif str_num1 == '6':
                str_out = 'шестьдесят'
            elif str_num1 == '7':
                str_out = 'семьдесят'
            elif str_num1 == '8':
                str_out = 'восемьдесят'
            elif str_num1 == '9':
                str_out = 'девяносто'
            if str_num2 == '0':
                str_out += ''
            elif str_num2 == '1':
                str_out += 'одна'
            elif str_num2 == '2':
                str_out += 'две'
            elif str_num2 == '3':
                str_out += 'три'
            elif str_num2 == '4':
                str_out += 'четыре'
            elif str_num2 == '5':
                str_out += 'пять'
            elif str_num2 == '6':
                str_out += 'шесть'
            elif str_num2 == '7':
                str_out += 'семь'
            elif str_num2 == '8':
                str_out += 'восемь'
            elif str_num2 == '9':
                str_out += 'девять'
        return str_out

if __name__ == "__main__":
    num1 = int_to_word(7)
    print(num1.to_word())
            
            
            
