import numpy as np

dict_occ = {}
dict_mark = {}
partitions = {}
counter_ = 0
string = "ababcbacadefegdehijhklij"
string = np.array(list(string))
keys = (np.unique(string))

for val in keys:
    dict_mark[val] = 1

for i in range(len(string)):
    key = string[i]
    if key in dict_occ:
        dict_occ[key][1] = i
    else:
        dict_occ[key] = [i,i]


for key in dict_occ:
    dict_mark[key] = 0
    for key2 in dict_occ:
        if (dict_mark[key2]):
            if (dict_occ[key][0] >= dict_occ[key2][0] and  dict_occ[key][0] <= dict_occ[key2][1]):            
                
                dict_mark[key2] = 0
                partitions[counter_] = dict_occ[key]
                partitions[counter_].append(dict_occ[key2])

            elif(dict_occ[key2][0] >= dict_occ[key][0] and  dict_occ[key2][0] <= dict_occ[key][1]):            
                    
                dict_mark[key2] = 0
                partitions[counter_] = dict_occ[key]
                partitions[counter_].append(dict_occ[key2])
                
    if counter_ in partitions:
        counter_+=1

print(partitions)



                    




print(partitions)
