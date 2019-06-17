def Knapsack_repair(x,p,w,C,type):
    import numpy as np
    #---------------------
    def not_func(arr):
        return np.abs(np.subtract(arr,1))
    #----------------------

    s = np.shape(x)
    if type ==1:
        while np.sum(np.multiply(w,x)) > C:
            I = np.floor(s[1]*np.random.rand())
            x[0,int(I)] = 0
    if type == 2:
        while np.sum(np.multiply(w,x)) > C:
            temp = np.multiply(np.divide(w,p),x)
            mx_pos = np.argmax(temp)
            x[0,mx_pos] = 0
        while np.sum(np.multiply(w,x)) <= C:
            temp = np.multiply(np.divide(w,p),not_func(x))
            mx_pos = np.argmax(temp)
            x[0,mx_pos] = 1
        x[0,mx_pos] = 0
    return  x


