locations={}
locations['Asia']={}
locations['Asia']['India']=['Banglore']
locations['Asia']['China']=['Shanghai']

# print(locations)
def get_all_values(locations):
    f=[]
    for key,value in locations.items():
        for key,value in value.items():
            f.append(value[0]+" "+"-"+" "+key)
        print(f)
    
    
   


print(get_all_values(locations))