def vector_length(vector):
    return len(vector) 

def vector_components(vector, i):
    return vector[i]
    
def vector_change_components(vector, i, new):
    vector[i] = new
    return vector

x = [2, 5, 3]
i = 1
new_num = 10

print(vector_length(x))

print(vector_components(x, i))

x = vector_change_components(x, i, new_num)  
print(x)
