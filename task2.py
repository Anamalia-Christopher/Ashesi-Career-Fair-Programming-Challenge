import pandas as pd

df = pd.read_csv("sample_complex_ebola_data.csv", index_col=0)
partial_df = pd.read_csv("sample_partial_time_series1.csv")#, index_col=0)
# print(df)
# partial_df.column=["h"]
print(len(partial_df))
# print(partial_df.column)
# partial_df.column=["h"]
print(partial_df.ix[0,0].dtype)
# print(partial_df.ix[9,0])
print((list(partial_df)))



def brute_force_for_finding_match():
    store=[]
    booster=[]
    # for i in range(len(partial_df)):
    #     if partial_df.ix[i, 0] in booster:
    #         continue
    #     for j in range(len(df)):
    #         if partial_df.ix[i, 0] == df["Value"][j]:
    #             store.append(df.iloc[j])
    #
    #             booster.append(partial_df.ix[i, 0])

    y = [partial_df.ix[j, 0] for j in range(len(partial_df))]

    print(y)
    for i in range(len(df)):

        if df["Value"][i] in y:
            store.append(df.iloc[i])
    print(store)
    print(len(store))

brute_force_for_finding_match()