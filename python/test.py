import time

def worst_case_example(n):
    my_set = set()
    start_time = time.time()
    # Add elements with hash collisions
    for i in range(n):
        my_set.add(i)
        my_set.add(i + n)
    
    # Search for a key with hash collision
    key_to_search = n
    found = key_to_search in my_set
    end_time = time.time()
    
    if found:
        print(f"Key {key_to_search} found!")
    else:
        print(f"Key {key_to_search} not found!")
    
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time:.10f} seconds")
n = 10000000  # Adjust the value of n as needed
my_set1 = set()
my_set2 = set()
my_list=[]
start_time = time.time()


for i in range(n):
    my_set1.add(i)
    my_set1.add(i + n)
    my_set2.add(i)
    my_list.append(i)

# Search for a key with hash collision
key_to_search = n
found = key_to_search in my_set1
end_time = time.time()

if found:
    print(f"Key {key_to_search} found!")
else:
    print(f"Key {key_to_search} not found!")

elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.10f} seconds")