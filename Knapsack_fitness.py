def Knapsack_fitness(Q,p,w,c,type):
    import numpy as np

    ro = np.max(np.divide(p,w))
    w_sum = np.sum(np.multiply(w,Q))
    pen2 = np.multiply(np.multiply(w_sum>c,ro),w_sum - c)
    pen1 = np.multiply(w_sum>c,np.log2(1+pen2))
    pq = np.multiply(p,Q)
    if type == 1:
        return np.subtract(np.sum(pq),pen1)
    elif type == 2:
        return np.subtract(np.sum(pq),pen2)
    elif type == 3:
        return np.sum(pq)