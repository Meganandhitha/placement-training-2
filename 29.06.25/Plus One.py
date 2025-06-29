class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            
            digits[i] = 0

        return [1] + digits

class Solution(object):
  def plusOne(self, digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    carry = 1
    for i in reversed(range(0, len(digits))):
      digit = (digits[i] + carry) % 10
      carry = 1 if digit < digits[i] else 0
      digits[i] = digit
    if carry == 1:
      return [1] + digits
    return digits
