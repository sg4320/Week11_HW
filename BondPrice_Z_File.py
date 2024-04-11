def getBondPrice_Z(face, couponRate, times, yc):
    # Calculate the coupon payment
    coupon_payment = face * couponRate
    
    # Initialize the bond price
    bondPrice = 0
    
    # Calculate the present value of each cash flow
    for t, y in zip(times, yc):
        if t != times[-1]:
            # Present value of coupon payments
            pv = coupon_payment / ((1 + y) ** t)
        else:
            # Present value of the final coupon payment plus face value
            pv = (coupon_payment + face) / ((1 + y) ** t)
        
        bondPrice += pv
    
    return bondPrice