# Напишите функцию number_to_words(num), которая принимает
# в качестве аргумента натуральное число num и возвращает
# его словесное описание на русском языке.
#
# Примечание 1.
# Считайте, что число 1 ≤ num ≤ 99.
#
# Примечание 2.
# Следующий программный код:
#
# print(number_to_words(7))
# print(number_to_words(85))
# должен выводить:
#
# семь
# восемьдесят пять
def number_to_words(num):
    num = int(input())
    a = ['one', 'two','three', 'four', 'five', 'six', 'seven', 'eight', ' nine', 'ten', 'eleven', 'twelve']
    b =['twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninty']
    if num<13:
        return()
    if num ==1:
        print(a[0])
    elif num ==2:
        print(a[1])
    elif num ==3:
        print(a[2])
    elif num == 4:
        print(a[3])
    elif num == 5:
        print(a[4])
    elif num == 6:
        print(a[5])
    elif num == 7:
        print(a[6])
    elif num == 8:
        print(a[7])
    elif num == 9:
        print(a[8])
    elif num == 10:
        print(a[9])
    elif num == 11:
        print(a[10])
    elif num == 12:
        print(a[11])
    elif num == 2:
        print(a[1])
