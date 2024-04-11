def getBondDuration(y, face, couponRate, m, ppy=1):
    coupon_payment = face * couponRate / ppy
    bondDuration = 0
    bondPrice = 0

    # Calculate each cash flow's present value and weight by the time
    for t in range(1, m * ppy + 1):
        if t != m * ppy:
            # Coupon payment present value
            pv = coupon_payment / ((1 + y/ppy) ** t)
        else:
            # Final coupon payment plus face value present value
            pv = (coupon_payment + face) / ((1 + y/ppy) ** t)

        bondPrice += pv
        # Weight the pv by the time and add to duration
        bondDuration += t * pv

    # Divide by the bond's price to get the Macaulay duration
    bondDuration /= bondPrice

    return bondDuration