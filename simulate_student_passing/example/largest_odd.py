def largest_odd(x, y, z):
    odds_list = []
    for num in x, y, z:
        if num % 2 != 0:
            odds_list.append(num)
    
    current_lrg_odd = -1
    if len(odds_list) > 0:
        for odd in odds_list:
            if odd > current_lrg_odd:
                current_lrg_odd = odd
    
    return current_lrg_odd