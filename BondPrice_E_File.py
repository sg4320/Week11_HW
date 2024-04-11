def getBondPrice_E(face, couponRate, yc):
    # Calculate the bond's maturity by the length of the yield curve
    m = len(yc)
    
    # Initialize the price of the bond
    bond_price = 0
    
    # Calculate the coupon payment
    coupon_payment = face * couponRate
    
    # Loop through each year up to maturity
    for t in range(1, m + 1):
        # Calculate the present value of the coupon payment
        # If it's the last year, add the face value to the coupon payment
        cash_flow = coupon_payment + (face if t == m else 0)
        # Discount the cash flow to present value using the yield for that year
        bond_price += cash_flow / ((1 + yc[t-1]) ** t)
    
    return bond_price
