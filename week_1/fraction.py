#Hoàn thiện các phương thức trong file Fraction.py theo các mô tả sau:

#Hàm is_minimalist_fraction(numerator, denominator) kiểm tra phân số gồm tử số là numerator, và mẫu số là denominator có phải phân số tối giản hay không nếu đúng trả lại giá trị là True, ngược lại trả lại giá trị là False?
import math
def is_minimalist_fraction(numerator, denominator):
    return math.gcd(numerator, denominator) == 1


#Hàm get_minimalist_fraction(numerator, denominator) thực hiện tính và trả lại phân số tối giản của phân số đầu vào (phân số được trả lại là 2 giá trị tương ứng là tử số và mẫu số)

def get_minimalist_fraction(numerator, denominator):
    if is_minimalist_fraction(numerator, denominator):
        return (numerator, denominator)

    gcd_frac = math.gcd(numerator, denominator)

    return get_minimalist_fraction(numerator // gcd_frac, denominator //gcd_frac)


