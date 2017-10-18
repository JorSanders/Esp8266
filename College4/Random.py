import urandom as urandom
import math


class Random:
    def randRange(self, top, bottom=0):

        # Need to raise the top by 1 or the highest number cant be generated
        top += 1

        # to prevert errors if top < bottom swap them
        if top < bottom:
            tmp = top
            top = bottom
            bottom = tmp

        # If the bottom number is bigger than 0 withdraw it from the top
        if (bottom < 0):
            return False
        elif (bottom > 0):
            top -= bottom

        # How many random bits do we need
        bits = math.log(top, 2)

        # Final number should be multiplied by
        factor = 1

        # If the top number doesnt match a bit value.
        # Calculate by how much we need to multiply later
        if (bits % 1):
            bits = math.ceil(bits)
            dif = math.pow(2, bits) - top
            factor = (top + dif) / top

        # create the random number multiply it and add the bottom
        randomNum = urandom.getrandbits(int(bits))

        randomNum /= factor

        randomNum += bottom

        return int(randomNum)