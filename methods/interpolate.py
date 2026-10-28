def lagint(x,xp,yp):
    def lagx(j,x,xp):
        num = 1.0
        den = 1.0
        for i in range(len(xp)):
            if i == j:
                continue
            num *= (x - xp[i][0])
            den *= (xp[j][0] - xp[i][0])
        
        return num/den

    lx = 0
    for j in range(len(xp)):
        lx += lagx(j, x, xp) * yp[j][0]
    
    return lx