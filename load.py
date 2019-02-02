import pickle
import re
f=open('words_alpha.txt').readlines()
data={}
i=0
for line in f:
    line=re.sub(" ",'',line)
    line=re.sub("\n",'',line)
    sort="".join(sorted(list(line)))
    print(i,line,sort)
    i+=1
    if sort not in data:
        data[sort]=[line]
    else:
        data[sort].append(line)
        
    
    
with open('saved.pkl', 'wb') as handle:
    pickle.dump(data, handle, protocol=pickle.HIGHEST_PROTOCOL)
