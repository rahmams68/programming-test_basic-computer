class QuestionTwoSolution:
    def isPalindrome(self, x: int):
        number = str(x)
        reversed_number = number[::-1]
        
        if number == reversed_number:
            print(x, 'is a palindrome!')
            return True
        
        print(x, 'is not a palindrome!')
        return False

    def test(self):
        self.isPalindrome(56765)
        self.isPalindrome(9090)
        self.isPalindrome(776677)

solution = QuestionTwoSolution()
solution.test()