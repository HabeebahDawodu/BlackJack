from unittest import TestCase, main
from unittest.mock import patch
from test_helper import run_test

class TestBlackjack(TestCase):

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_example(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand less than 21.
        The dealer wins by having a higher hand than the user.

        This does not count as one of your tests.
        '''
        output = run_test([3, 5, 8], ['y', 'n'], [3, 5, 10], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "You have 8. Hit (y/n)? y\n" \
                   "Drew an 8\n" \
                   "You have 16. Hit (y/n)? n\n" \
                   "Final hand: 16.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "Dealer has 8.\n" \
                   "Drew a 10\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output, expected)


    
    # Make sure all your test functions start with test_ 
    # Follow indentation of test_example
    # WRITE ALL YOUR TESTS BELOW. Do not delete this line.

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_case_1(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand less than 21.
        The user wins by having a higher hand than the dealer.
        '''
        output_1 = run_test([3, 5, 10], ['y', 'n'], [3, 5, 9], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "You have 8. Hit (y/n)? y\n" \
                   "Drew a 10\n" \
                   "You have 18. Hit (y/n)? n\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "Dealer has 8.\n" \
                   "Drew a 9\n" \
                   "Final hand: 17.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output_1, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_case_2(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand less than 21.
        They push by having equal hands.
        '''
        output_2 = run_test([3, 5, 10], ['y', 'n'], [3, 5, 10], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "You have 8. Hit (y/n)? y\n" \
                   "Drew a 10\n" \
                   "You have 18. Hit (y/n)? n\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "Dealer has 8.\n" \
                   "Drew a 10\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Push.\n"
        self.assertEqual(output_2, expected)

    
    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_case_3(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards with a hand of 21(BLACKJACK).
        They push by having equal hands.
        '''
        output_3 = run_test([3, 5, 13, 3], ['y', 'y', 'n'], [3, 8, 13], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "You have 8. Hit (y/n)? y\n" \
                   "Drew a King\n" \
                   "You have 18. Hit (y/n)? y\n" \
                   "Drew a 3\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew an 8\n" \
                   "Dealer has 11.\n" \
                   "Drew a King\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Push.\n"
        self.assertEqual(output_3, expected)   

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_case_4(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand greater than 21(BUST).
        The dealer wins because user automatically loses whenever user BUSTs.
        '''
        output_4 = run_test([9, 9, 8], ['y', 'n'], [3, 9, 10], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 9\n" \
                   "Drew a 9\n" \
                   "You have 18. Hit (y/n)? y\n" \
                   "Drew an 8\n" \
                   "Final hand: 26.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 9\n" \
                   "Dealer has 12.\n" \
                   "Drew a 10\n" \
                   "Final hand: 22.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output_4, expected)


    
    # Make sure all your test functions start with test_ 
    # Follow indentation of test_example
    # WRITE ALL YOUR TESTS BELOW. Do not delete this line.

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_case_5(self, input_mock, randint_mock):
        '''
        The dealer receives cards that end up with a hand over 21(BUST) and user recieves cards that end up with a hand of 21(BLACKJACK).
        The user wins has he attains BLACKJACK first.
        '''
        output_5 = run_test([3, 5, 13, 3], ['y', 'y', 'n'], [3, 9, 10], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "You have 8. Hit (y/n)? y\n" \
                   "Drew a King\n" \
                   "You have 18. Hit (y/n)? y\n" \
                   "Drew a 3\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 9\n" \
                   "Dealer has 12.\n" \
                   "Drew a 10\n" \
                   "Final hand: 22.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output_5, expected)

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_case_6(self, input_mock, randint_mock):
        '''
        The user receives cards that end up with a hand greater than 21(BUST) and the user receives cards that end up with a hand of 21(BLACKJACK).
        The dealer wins because user automatically loses whenever user BUSTs.
        '''
        output_6 = run_test([9, 9, 8], ['y', 'n'], [3, 8, 13], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 9\n" \
                   "Drew a 9\n" \
                   "You have 18. Hit (y/n)? y\n" \
                   "Drew an 8\n" \
                   "Final hand: 26.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew an 8\n" \
                   "Dealer has 11.\n" \
                   "Drew a King\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"  
        self.assertEqual(output_6, expected) 
    

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_case_7(self, input_mock, randint_mock):
        '''
        Both the dealer and user receive cards that end up with a hand less than 21.
        The user wins by having a higher hand than the dealer.
        '''
        output_7 = run_test([3, 5, 10], ['y', 'n'], [3, 5, 9], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "You have 8. Hit (y/n)? y\n" \
                   "Drew a 10\n" \
                   "You have 18. Hit (y/n)? n\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "Dealer has 8.\n" \
                   "Drew a 9\n" \
                   "Final hand: 17.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output_7, expected) 

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_case_8(self, input_mock, randint_mock):
        '''
        The user receives cards that end up with a hand greater than 21(BUST) and the dealer receives cards that end up with a hand of 21(BLACKJACK).
        The dealer wins because user automatically loses whenever user BUSTs.
        '''
        output_8 = run_test([9, 9, 8], ['y', 'n'], [3, 8, 13], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 9\n" \
                   "Drew a 9\n" \
                   "You have 18. Hit (y/n)? y\n" \
                   "Drew an 8\n" \
                   "Final hand: 26.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew an 8\n" \
                   "Dealer has 11.\n" \
                   "Drew a King\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output_8, expected)  

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_case_9(self, input_mock, randint_mock):
        '''
        The user receives cards that end up with a hand less than 21 and dealer receives cards that end up with a hand of 21(BLACKJACK).
        The dealer wins because he attains BLACKJACK first.
        '''
        output_9 = run_test([3, 5, 10], ['y', 'n'], [3, 8, 13], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "You have 8. Hit (y/n)? y\n" \
                   "Drew a 10\n" \
                   "You have 18. Hit (y/n)? n\n" \
                   "Final hand: 18.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew an 8\n" \
                   "Dealer has 11.\n" \
                   "Drew a King\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"  
        self.assertEqual(output_9, expected)  


    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_case_10(self, input_mock, randint_mock):
        '''
        The user receives cards that end up with a hand less than 21 and dealer receives cards that end up with a hand over 21(BUST).
        The user wins because dealer BUSTs first and automatically loses.
        '''
        output_10 = run_test([3, 5, 10], ['y', 'n'], [3, 9, 10], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "You have 8. Hit (y/n)? y\n" \
                   "Drew a 10\n" \
                   "You have 18. Hit (y/n)? n\n" \
                   "Final hand: 18.\n" \
                    "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 9\n" \
                   "Dealer has 12.\n" \
                   "Drew a 10\n" \
                   "Final hand: 22.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"  
        self.assertEqual(output_10, expected)



    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_case_11(self, input_mock, randint_mock):
        '''
        The dealer receives cards that end up with a hand less than 21 and user receives cards that end up with a hand over 21(BUST).
        The dealer wins because user automatically loses by attaining BUST first.
        '''
        output_11 = run_test([9, 9, 8], ['y', 'n'], [3, 5, 9], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 9\n" \
                   "Drew a 9\n" \
                   "You have 18. Hit (y/n)? y\n" \
                   "Drew an 8\n" \
                   "Final hand: 26.\n" \
                   "BUST.\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "Dealer has 8.\n" \
                   "Drew a 9\n" \
                   "Final hand: 17.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "Dealer wins!\n"
        self.assertEqual(output_11, expected) 

    @patch('blackjack_helper.randint')
    @patch('builtins.input')
    def test_case_12(self, input_mock, randint_mock):
        '''
        The dealer receives cards that end up with a hand less than 21 and user receives cards that end up with a hand of 21(BLACKJACK).
        The user wins because he attains BLACKJACK first.
        '''
        output_12 = run_test([3, 5, 13, 3], ['y', 'y', 'n'], [3, 5, 9], randint_mock, input_mock)
        expected = "-----------\n" \
                   "YOUR TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "You have 8. Hit (y/n)? y\n" \
                   "Drew a King\n" \
                   "You have 18. Hit (y/n)? y\n" \
                   "Drew a 3\n" \
                   "Final hand: 21.\n" \
                   "BLACKJACK!\n" \
                   "-----------\n" \
                   "DEALER TURN\n" \
                   "-----------\n" \
                   "Drew a 3\n" \
                   "Drew a 5\n" \
                   "Dealer has 8.\n" \
                   "Drew a 9\n" \
                   "Final hand: 17.\n" \
                   "-----------\n" \
                   "GAME RESULT\n" \
                   "-----------\n" \
                   "You win!\n"
        self.assertEqual(output_12, expected) 


      


    
     

    # Write all your tests above this. Do not delete this line.

if __name__ == '__main__':
    main()
