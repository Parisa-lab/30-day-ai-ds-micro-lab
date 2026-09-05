def vector_length(vector):
    return len(vector) 

def vector_components(vector, i):
    return vector[i]
    
def vector_change_components(vector, i, new):
    vector[i] = new
    
def vector_add(a, b):
    if len(a) == len(b):
        return [a[i] + b[i] for i in range(len(a))]
    else:
        raise ValueError("Vectors must have the same dimension.")
        
def vector_subtract(a, b):
    if len(a) == len(b):
        return [a[i] - b[i] for i in range(len(a))]
    else:
        raise ValueError("Vectors must have the same dimension.")
        
def vector_scalar_multiply(vector, scalar):
    return [scalar * vector[i] for i in range(len(a))]    

x = [3, 6, 9]
i = 1
new_num = 50

print("Vector:", x)

print("Dimension:", vector_length(x))

print(f"x{i} is: {vector_components(x, i)}")

vector_change_components(x, i, new_num)  
print("Updated vector is:", x)

a = [3, 50, 9]
b = [1, 2, 4]
scalar = 3
print("Sum:", vector_add(a, b))
print("Subtraction:", vector_subtract(a, b))
print("Scalar multiplication:", vector_scalar_multiply(a, scalar))
