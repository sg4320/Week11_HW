def GetBondPrice(y,face,couponRate, m,ppy=1):
        # Calculate the coupon payment
    coupon_payment = face * couponRate / ppy
    # Initialize the bond price
    bondPrice = 0

    # Sum the present value of the coupons
    for t in range(1, m * ppy + 1):
        bondPrice += coupon_payment / ((1 + y / ppy) ** t)

    # Add the present value of the face value
    bondPrice += face / ((1 + y / ppy) ** (m * ppy))

    return bondPrice