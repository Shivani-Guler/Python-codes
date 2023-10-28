#rupee=50
#no_of_choc=rupee+rupee/2
#print(no_of_choc)

amount=25
wrapper_per_choc=2
cost_per_choc=1
chocs=amount/cost_per_choc
print(chocs)
wrappers=chocs
while wrappers>=wrapper_per_choc:
    choc_gen,wrappers=divmod(wrappers,wrapper_per_choc)
    wrappers+=choc_gen
    chocs+=choc_gen
print(f"chocs={chocs}")