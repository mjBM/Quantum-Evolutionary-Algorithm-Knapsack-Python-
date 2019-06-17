def Knapsack_quantum(agents,profits,weights,capacity,H,repair,penalty,iteration,teta):
    import math
    import numpy as np
    from Knapsack_observe import Knapsack_observe
    from Knapsack_repair import Knapsack_repair
    from Knapsack_fitness import Knapsack_fitness

    def compare(matrix, flo):
        return [[x > flo for x in y] for y in matrix]
    #-----------------------------------------------------------------------------------
    def convert_2_matrix(mtrx):
        return np.matrix(mtrx)
    #------------------------------------------------------------------------------------
    def H_gate_min(v):
        min_vec = v[:] > np.arccos(np.sqrt(H))
        min_vec_not = np.logical_not(min_vec)
        tmp1 = np.multiply(min_vec,np.arccos(np.sqrt(H)))
        tmp2 = np.multiply(min_vec_not,v[:])
        res = tmp1 + tmp2

        return res
    #------------------------------------------------------------------------------------
    def H_gate_max(v):
        max_vec = v[:] < np.arccos(np.sqrt(1-H))
        max_vec_not = np.logical_not(max_vec)
        tmp1 = np.multiply(max_vec,np.arccos(np.sqrt(1-H)))
        tmp2 = np.multiply(max_vec_not,v[:])
        res = tmp1 + tmp2
        return res
    #*************************************************************
    # *************************************************************
    # *************************************************************
    # *************************************************************
    # *************************************************************
    # *************************************************************
    # *************************************************************
    # *************************************************************
    # ---------------------------------------------------------------------------------initialization
    local_group_size = 10
    local_migration_condition = 30
    global_migration_condition = 70
    best_global_fitness = -math.inf
    tmp_size =  np.size(profits)
    ind_size = tmp_size                                              # length of chromosom (each individual)
    iteration_fitness = convert_2_matrix([0 for x in range(iteration)])
    best_agent_fitness = convert_2_matrix([0 for x in range(agents)])                     # best agent fitness of each iteration
    Q = convert_2_matrix([[np.pi/4 for x in range(ind_size)]for j in range(agents)])    # quantum individuals   (probabilitie)
    p = convert_2_matrix([[0 for x in range(ind_size)]for j in range(agents)])            # observed individuals (binary)
    B = convert_2_matrix([[0 for x in range(ind_size)]for j in range(agents)])            # best observe of each iteration(best local Observe)
    fitness = convert_2_matrix([0 for x in range(agents)])                                # best fitness of each individual at current iteration
    mut = list()                                                        # mutaiton list
    #---------------------------------------------------------------------------------II - IV
    for i in range(agents):
        # print(np.shape(p[i]))
        p[i] = Knapsack_observe(Q[i])                                   #set observe of Q(i) in P(i) array
        p[i] = Knapsack_repair(p[i],profits,weights,capacity,repair)    #rapair for size of knapsack
        fitness[0,i] = Knapsack_fitness(p[i],profits,weights,capacity,penalty)     #calculate fitness of each P array
        best_agent_fitness[0,i] = fitness[0,i]                                         #calculate best agent fitness of each iteration
        B[i] = p[i]                                                       #B(i) is best observe of each iteration(best local Observe)
    # --------------------------------------------------------------------------------- V - VI
    for j in range(iteration):
        for i in range(agents):
            p[i] = Knapsack_observe(Q[i])                                               # observing of  Q(i) array
            p[i] = Knapsack_repair(p[i], profits, weights, capacity, repair)            # rapair knapsack
            fitness[0,i] = Knapsack_fitness(p[i], profits, weights, capacity, penalty)    #calculate fitness of each P array
            #VII) calculate delta_teta sign - ---------------------
    #         if fitness[0,i] > best_agent_fitness[0,i]:                                       #Q(i) must Converge to 0,if P(i)=0
    #               % clear help; % and Converge to 1, if P(i)=1
    # % help=(2 * (sin(Q(i).ind).* cos(Q(i).ind) > 0)-1)...
    # %.* (2 * P(i).ind-1) * teta;
    # % Q(i).ind=Q(i).ind+help;
    # % else % Q(i) must Converge to 0, if B(i)=0
    # % clear help; % and Converge to 1, if B(i)=1
    # % help=(2 * (sin(Q(i).ind).* cos(Q(i).ind) > 0)-1)...
    # %.* (2 * B(i).ind-1) * teta;
    # % Q(i).ind=Q(i).ind+help;
    # % end
    # Q Gate-------------------------------------------------
            if fitness[0,i] > best_agent_fitness[0,i]:        # Q(i) must Converge to 0, if P(i)=0 and Converge to 1, if P(i)=1
                mut = []                                   # clear mut (help in matlab)
                # mut = np.multiply((np.multiply(2 , np.multiply(np.sin(Q[i]),np.cos(Q[i]))> 0) )-1 , np.subtract(np.multiply(2 , p[i]) , 1))
                mut = np.multiply(((np.multiply(2 * np.sin(Q[i]) , np.cos(Q[i]))> 0) -1) , 2 * p[i] - 1)
                # print(np.shape(mut))
                mut = np.multiply(mut,teta)
                Q[i] = Q[i] + mut
                # print(np.shape(Q[i]))
            else:                                         # Q(i) must Converge to 0, if B(i)=0 and Converge to 1, if B(i)=1
                mut = []                                                                # clear mut (help in matlab)
                mut = np.multiply(((np.multiply(2 * np.sin(Q[i]) , np.cos(Q[i]))> 0) -1) , 2 * B[i] - 1)
                mut = mut*teta
                Q[i] = Q[i] + mut
            #  ------  H-Gate
            Q[i] = H_gate_min(Q[i])
            Q[i] = H_gate_max(Q[i])
        #VIII) _ IX)---------------------------------------
        for i in range(agents):
            if fitness[0,i] > best_agent_fitness[0,i]:      # agent Comparisoon
                B[i] = p[i]
                best_agent_fitness[0,i] = fitness[0,i]
        Mx = np.max(best_agent_fitness)
        Mx_index = np.argmax(best_agent_fitness)
        if Mx > best_global_fitness:
            best_global_observe = p[Mx_index]
            best_global_fitness = Mx
        iteration_fitness[0,j] = best_global_fitness     # global fitness array
        #X)-------------------------------------------------------
        local_migration = False
        global_migration = False
        if np.mod(j,local_migration_condition) == 0:
            local_migration = True
        if np.mod(j,global_migration_condition) ==0:
            global_migration = True
        # if isconvergence(agents,ind_size, Q, 0.98):  # Convergence
        #     for i in range(agents):
        #         B[i] = best_global_observe   # exchange individual Best observe with best global observe
        #         best_agent_fitness[0,i] = best_global_fitness   #exchange individual Best fitness with best global fitness
        if global_migration:
            for i in range(agents):
                B[i] = best_global_observe                  #exchange individual Best observe with best global observe
                best_agent_fitness[0,i] = best_global_fitness #exchange individual Best fitness with best global fitness
        elif local_migration:
            local_group_no = int(np.floor(agents/local_group_size))
            for i in range(local_group_no):
                if i == local_group_no - 1 :
                    delete = best_agent_fitness[0,local_group_size:]          # last group
                else:
                    delete = best_agent_fitness[0,i * local_group_size:(i+1)*local_group_size]
                best_local_fitness = np.max(delete)            #fitness
                ix = np.argmax(delete)
                ix = i * local_group_size + ix
                best_local = B[ix]                          # binary shape of best local fitness
                grp_begin = i * local_group_size
                grp_end= (i+1) * local_group_size
                for kk in range(grp_begin,grp_end):
                    B[kk] = best_local                                  #exchange individual Best observe with best local observe
                    best_agent_fitness[0,kk] = best_local_fitness         #exchange individual Best fitness with best local observe
    return iteration_fitness





