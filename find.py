import pickle

with open('saved.pkl', 'rb') as handle:
    data = pickle.load(handle)
print("Loaded")
while True:
    s=input('Enter scrambled text:')
    s="".join(sorted(list(s)))
    print(s)
    if s=="":break
    if s in data:
        print('Most Likely:',data[s])
    else:
        print("Error")
