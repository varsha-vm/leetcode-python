def swap_values(new_list, ind1, ind2):
    new_list[ind1], new_list[ind2] = new_list[ind2], new_list[ind1]
    return new_list


swap_values([10000,1000,100,10,0], 0, 4)  