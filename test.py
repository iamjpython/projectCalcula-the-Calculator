import unittest
from calculator import solve


class Test(unittest.TestCase):
    def test_add(self):
        Solve = "42+34+76+48"
        self.assertEqual(solve(Solve), 200)

    def test_adding_decimal_numbers(self):
        Solve = "12.42+34+76+48.56"
        self.assertEqual(solve(Solve), 170.98000000000002)

    def test_subtract(self):
        Solve = "52-12-17-2"
        self.assertEqual(solve(Solve), 21)

    def test_subtracting_decimal_numbers(self):
        Solve = "48.10-10.56-15.25-5.04"
        self.assertEqual(solve(Solve), 17.25)

    def test_multiply(self):
        Solve = "12*3*3*1"
        self.assertEqual(solve(Solve), 108)

    def test_multiplying_decimal_numbers(self):
        Solve = "3.12*4.5*6.25"
        self.assertEqual(solve(Solve), 87.75)

    def test_divide(self):
        Solve = "78/4/6"
        self.assertEqual(solve(Solve), 3.25)

    def test_dividing_decimal_numbers(self):
        Solve = "64.48/4.5/2.2"
        self.assertEqual(solve(Solve), 6.513131313131313)

    def test_add_and_subtract(self):
        Solve = "5+7-8+7+4+2-6"
        self.assertEqual(solve(Solve), 11)

    def test_add_and_subtract_decimal_numbers(self):
        Solve = "12.4+6.8-5.56-8.35+3.45"
        self.assertEqual(solve(Solve), 8.740000000000002)

    def test_add_and_multiply(self):
        Solve = "1+2+3+4+5+6*2+1+2+3*4"
        self.assertEqual(solve(Solve), 42)

    def test_add_and_multiply_decimal_numbers(self):
        Solve = "5.5+3.5+8.25+9.25*2.5"
        self.assertEqual(solve(Solve), 40.375)

    def test_multiply_and_divide(self):
        Solve = "5*5*4/10*2"
        self.assertEqual(solve(Solve), 20)

    def test_multiply_and_divide_decimal_numbers(self):
        Solve = "2.33*5.24/1.5*3.281"
        self.assertEqual(solve(Solve), 26.705590133333338)

    def test_combined_1(self):
        Solve = "5*3+5-2/2+14/7*3"
        self.assertEqual(solve(Solve), 25)

    def test_combined_2(self):
        Solve = "1+9/3+1*5-100/5"
        self.assertEqual(solve(Solve), -11)

    def test_combined_3(self):
        Solve = "(5*3)/5*9+100"
        self.assertEqual(solve(Solve), 127)

    def test_fraction(self):
        Solve = "(3/5)*(5/3)"
        self.assertEqual(solve(Solve), 1)

    def test_addition_of_two_negative_numbers(self):
        Solve = "(-2)+(-2)"
        self.assertEqual(solve(Solve), -4)

    def test_addition_of_two_negative_decimal_numbers(self):
        Solve = "(-5.5)+(-3.75)"
        self.assertEqual(solve(Solve), -9.25)

    def test_addition_of_one_positive_and_one_negative_number(self):
        Solve = "(28)+(-9)"
        self.assertEqual(solve(Solve), 19)

    def test_addition_of_one_positive_and_one_negative_decimal_number(self):
        Solve = "(24.33)+(-18.674)"
        self.assertEqual(solve(Solve), 5.655999999999999)

    def test_subtraction_of_two_negative_numbers(self):
        Solve = "(-9)-(-3)"
        self.assertEqual(solve(Solve), -6)

    def test_subtraction_of_two_negative_decimal_numbers(self):
        Solve = "(-12.54)-(-17.125)"
        self.assertEqual(solve(Solve), 4.585000000000001)

    def test_subtraction_of_one_negative_and_one_positive_number(self):
        Solve = "(-14)-(10)"
        self.assertEqual(solve(Solve), -24)

    def test_subtraction_of_one_negative_and_one_positive_decimal_number(self):
        Solve = "(-9.99)-(14.667)"
        self.assertEqual(solve(Solve), -24.657)

    def test_multiplication_of_two_negative_numbers(self):
        Solve = "(-9)*(-7)"
        self.assertEqual(solve(Solve), 63)

    def test_multiplication_of_two_negative_decimal_numbers(self):
        Solve = "(-4.5)*(-9.25)"
        self.assertEqual(solve(Solve), 41.625)

    def test_multiplication_of_one_negative_and_one_positive_number(self):
        Solve = "(-23)*(3)"
        self.assertEqual(solve(Solve), -69)

    def test_multiplication_of_one_negative_and_one_positive_decimal_number(self):
        Solve = "(-24.55)*(9.129)"
        self.assertEqual(solve(Solve), -224.11695)

    def test_division_of_two_negative_numbers(self):
        Solve = "(-10)/(-5)"
        self.assertEqual(solve(Solve), 2)

    def test_division_of_two_negative_decimal_numbers(self):
        Solve = "(-5.6)/(-4.2)"
        self.assertEqual(solve(Solve), 1.3333333333333333)

    def test_division_of_one_negative_and_one_positive_number(self):
        Solve = "(-8)/(4)"
        self.assertEqual(solve(Solve), -2)

    def test_division_of_one_negative_and_one_positive_decimal_number(self):
        Solve = "(-8.25)/(3.67)"
        self.assertEqual(solve(Solve), -2.2479564032697548)

    def test_multiplication_before_addition(self):
        Solve = "5+7*8"
        self.assertEqual(solve(Solve), 61)

    def test_parentheses_first(self):
        Solve = "(3+6)*2"
        self.assertEqual(solve(Solve), 18)

    def test_multiplication_and_division(self):
        Solve = "12/6*3/2"
        self.assertEqual(solve(Solve), 3)

    def test_exponents_of_exponents(self):
        Solve = "5^3^2"
        self.assertEqual(solve(Solve), 1953125)

    def test_pemdas(self):
        Solve = "7+(6*5^2+3)"
        self.assertEqual(solve(Solve), 160)

    def test_sin_1(self):
        Solve = "sin(45)"
        self.assertEqual(solve(Solve), 0.8509035245341184)

    def test_sin_2(self):
        Solve = "sin(12+23)/12"
        self.assertEqual(solve(Solve), -0.035681889124679254)

    def test_sin_3(self):
        Solve = "sin(pi/5)"
        self.assertEqual(solve(Solve), 0.5875275257138919)

    def test_sin_4(self):
        Solve = "sin(36)/sin(48)"
        self.assertEqual(solve(Solve), 1.2909506487527551)

    def test_cos_1(self):
        Solve = "cos(12)"
        self.assertEqual(solve(Solve), 0.8438539587324921)

    def test_cos_2(self):
        Solve = "cos(15+15)/20"
        self.assertEqual(solve(Solve), 0.0077125724943792025)

    def test_cos_3(self):
        Solve = "cos(2*pi/7)"
        self.assertEqual(solve(Solve), 0.6238455049284951)

    def test_cos_4(self):
        Solve = "cos(45)/cos(30)"
        self.assertEqual(solve(Solve), 3.4056210764992865)

    def test_tan_1(self):
        Solve = "tan(60)"
        self.assertEqual(solve(Solve), 0.320040389379563)

    def test_tan_2(self):
        Solve = "tan(12+16)/36"
        self.assertEqual(solve(Solve), -0.007817489015674035)

    def test_tan_3(self):
        Solve = "tan(pi/2)"
        self.assertEqual(solve(Solve), 1255.7655915007897)

    def test_tan_4(self):
        Solve = "tan(60)/tan(45)"
        self.assertEqual(solve(Solve), 0.19758321478680327)

    def test_arcsin_1(self):
        Solve = "arcsin(1)"
        self.assertEqual(solve(Solve), 1.5707963267948966)

    def test_arcsin_2(self):
        Solve = "arcsin(sin(30/pi))"
        self.assertEqual(solve(Solve), -0.1293621666191541)

    def test_arccos_1(self):
        Solve = "arccos(1)"
        self.assertEqual(solve(Solve), 0)

    def test_arccos_2(self):
        Solve = "arccos(cos(30)/2*pi)"
        self.assertEqual(solve(Solve), 1.3261896007239238)

    def test_arctan_1(self):
        Solve = "arctan(1)"
        self.assertEqual(solve(Solve), 0.7853981633974483)

    def test_arctan_2(self):
        Solve = "arctan(tan(60)/4*pi)"
        self.assertEqual(solve(Solve), 0.24613757912750195)

    def test_sqrt_1(self):
        Solve = "sqrt(36)"
        self.assertEqual(solve(Solve), 6)

    def test_sqrt_2(self):
        Solve = "sqrt(64+36)"
        self.assertEqual(solve(Solve), 10)

    def test_sqrt_3(self):
        Solve = "sqrt(11^2+(19 -11/tan(39))^2)"
        self.assertEqual(solve(Solve), 19.380861851434787)

    def test_sqrt_4(self):
        Solve = "sqrt(9+(6/sin(31))^2)"
        self.assertEqual(solve(Solve), 15.150099386113009)

    def test_sqrt_5(self):
        Solve = "sqrt(9+(6/cos(31))^2)"
        self.assertEqual(solve(Solve), 7.212726190084341)

    def test_sqrt_6(self):
        Solve = "sqrt((16^2-10^2)/4)"
        self.assertEqual(solve(Solve), 6.244997998398398)

    def test_factorial_1(self):
        Solve = "fact(3)"
        self.assertEqual(solve(Solve), 6)

    def test_factorial_2(self):
        Solve = "fact(9)"
        self.assertEqual(solve(Solve), 362880)

    def test_factorial_3(self):
        Solve = "fact(4*3)"
        self.assertEqual(solve(Solve), 479001600)

    def test_factorial_4(self):
        Solve = "fact(12-9)"
        self.assertEqual(solve(Solve), 6)

    def test_log_1(self):
        Solve = "log(56)"
        self.assertEqual(solve(Solve), 1.7481880270062005)

    def test_log_2(self):
        Solve = "log(21)/log(6)"
        self.assertEqual(solve(Solve), 1.6991803252671502)

    def test_ln_1(self):
        Solve = "ln(5)"
        self.assertEqual(solve(Solve), 1.6094379124341003)

    def test_ln_2(self):
        Solve = "(1/3)*ln(9)"
        self.assertEqual(solve(Solve), 0.7324081924454064)

    def test_ln_3(self):
        Solve = "ln(sqrt(5))"
        self.assertEqual(solve(Solve), 0.8047189562170503)

    def test_rndm_eqn_1(self):
        Solve = "sin(45)+6*pi/tan(60)"
        self.assertEqual(solve(Solve), 59.71847344757921)

    def test_rndm_eqn_2(self):
        Solve = "-sin(45)+sqrt((cos(45)/tan(45))/arcsin(sin(45+45)))"
        self.assertEqual(solve(Solve), -0.30943757317164633)

    def test_rndm_eqn_3(self):
        Solve = "(5*sin(45)) - (6*arcsin(sin(60)/pi/2))"
        self.assertEqual(solve(Solve),  4.545852426157926)

if __name__ == "__main__":
    unittest.main()
