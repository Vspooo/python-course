# написати прогу яка вибирає зі введеної строки числа і виводить їх через кому

string = 'as 23 fdfdg544 34'

print(", ".join("".join(ch if ch.isdigit() else " " for ch in string).split()))