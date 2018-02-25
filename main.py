from get_spread_pricediff import get_data
import markov_pricediff as mp

def main(date):
    get_data(date)
    print("price_diff_matrix:\n")
    p_mat = mp.call_pricediff(date)
    print("spread_matrix:\n")
    s_mat = mp.call_spread(date)
    print("price_station:\n")
    mp.stationary_dis(p_mat)
    print("\n\nspread_station:\n")
    mp.stationary_dis(s_mat)


main(20180103)