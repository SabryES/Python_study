thisset={"apple","banana",'cherry'}
print(type(thisset))
print(len(thisset))

for x in thisset:
    print(x)

print("cherry" in thisset)
print("orange"in thisset)
thisset.add("orange")
# thisset.add("orange","heama") error
thisset.update("heama","hesa")
thisset.update(["heama","hesa"])
print("orange"in thisset)
print(thisset)

