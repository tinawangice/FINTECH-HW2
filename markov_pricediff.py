import pandas as pd
import scipy.linalg


def call_pricediff(date):
    price_df = pd.read_csv('%s_price_diff' % str(date), '\t')
    price_df.columns = ['diff']
    bins = [-float('inf'), -0.05, -0.03, -0.01, 0.01, 0.03, 0.05, float('inf')]
    labels = ['<-0.05', '-0.05 ~ -0.03', '-0.03 ~ -0.01', '-0.01 ~ 0.01', '0.01 ~ 0.03', '0.03 ~ 0.05', '>0.05']
    price_df['binned'] = pd.cut(price_df['diff'], bins=bins, labels=labels)
    price_df['pre_bin'] = price_df['binned'].shift(1)
    price_df = price_df[['pre_bin', 'binned']].groupby(['pre_bin', 'binned']).size().reset_index(name='counts')
    arr = price_df['counts'].values
    p_mat = arr.reshape(7, 7).astype(float)
    p_mat = p_mat / p_mat.sum(axis=1)[:, None]
    p_mat_df = pd.DataFrame(data=p_mat, columns=labels, index=labels)
    print(p_mat_df)
    return p_mat


def call_spread(date):
    spread_df = pd.read_csv('%s_spread' % str(date), '\t')
    spread_df.columns = ['spread']
    bins = [-float("inf"), 0.01, 1, 2, 3, 4, 5, float('inf')]
    labels = [0, '0-1', '1-2', '2-3', '3-4', '4-5', '>5']
    spread_df['binned'] = pd.cut(spread_df['spread'], bins=bins, labels=labels)
    spread_df['pre_bin'] = spread_df['binned'].shift(1)
    spread_df1 = spread_df[['pre_bin', 'binned']].groupby(['pre_bin', 'binned']).size().reset_index(name='counts')
    arr = spread_df1['counts'].values
    s_mat = arr.reshape(7, 7).astype(float)
    s_mat = s_mat / s_mat.sum(axis=1)[:, None]
    spread_mat_df = pd.DataFrame(data=s_mat, columns=labels, index=labels)
    print(spread_mat_df)
    return s_mat


def stationary_dis(mat):
    ev, left_v = scipy.linalg.eig(mat, left=True, right=False)
    dom_eig = []
    for i in range(7):
        dom_eig.append(left_v[i][0])
    dom_eig_norm = dom_eig / sum(dom_eig[:])
    res = '['
    for x in dom_eig_norm:
        res += str("%.3f," % x)
    res = res[:-1] + ']'
    print(res)
    print(dom_eig_norm)
