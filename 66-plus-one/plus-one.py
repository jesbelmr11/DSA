class Solution(object):
    def plusOne(self, digits):

        arr = []

        for j in range(len(digits) - 1, -1, -1):

            num = digits[j]
            num = num + 1

            l = len(str(num))

            if l == 1:
                digits[j] = num
                return digits

            else:
                digits[j] = 0

        arr.append(1)

        for i in digits:
            arr.append(i)

        return arr