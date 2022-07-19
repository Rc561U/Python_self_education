

lst = [1, "abc", -5, 7.68, True]
rr = [i for i in lst if type(i) in (int,float)]
print(rr)