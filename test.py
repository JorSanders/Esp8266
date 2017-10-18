def circle(x0, y0, r):
    for y in range(y0 - r, y0 + r + 1):
        for x in range(x0 - r, x0 + r + 1):
            xd = x0 - x
            yd = y0 - y
            print("x: " + str(x) + "\txd: " + str(xd) +
                  "\ty: " + str(y) + "\tyd: " + str(yd) +
                  "\t r2: " + str(r*r) +
                  "\t x2: " + str(x*x) +
                  "\t y2: " + str(y*y)
                  )
            if xd * xd + yd * yd < r * r:
                a=1
                # print(x, y)


circle(30, 15, 10)
