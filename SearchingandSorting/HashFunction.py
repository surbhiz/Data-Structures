def hash(a_string, table_size):
    sum = 0
    for pos in range(len(a_string)):
        sum += ord(a_string[pos])*(pos+1)
    return sum % table_size


print(hash('cat', 11))
print(hash('act', 11))
