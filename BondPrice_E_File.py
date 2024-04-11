def getBondPrice_E(face, couponRate, m, yc):
    coupon_payment = face * couponRate
    bondPrice = 0

    # Loop over each time period and corresponding yield curve rate
    for t, y in enumerate(yc, start=1):
        if t != m:
            # Present value of coupon payments
            pv = coupon_payment / ((1 + y) ** t)
        else:
            # Present value of the final coupon payment plus face value
            pv = (coupon_payment + face) / ((1 + y) ** t)
        
        bondPrice += pv

    return bondPrice
