import pickle
with open('sample.pk1','rb') as f:
    load_num = pickle.load(f)
    print(load_num)
