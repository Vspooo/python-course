# 1)написати прогу яка вибирає зі введеної строки цифри і виводить їх через ком

string = 'as 23 fdfdg544'

print(", ".join([item for item in string if item.isdigit()]))