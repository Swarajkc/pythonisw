import random
from typing import List

def lzw_compress(input_data: List[int]) -> List[int]:
    dictionary = {bytes([i]): i for i in range(256)}
    current = b""
    compressed = []
    dict_size = 256
    
    for byte in input_data:
        next_str = current + bytes([byte])
        if next_str in dictionary:
            current = next_str
        else:
            compressed.append(dictionary[current])
            if dict_size < 4096:
                dictionary[next_str] = dict_size
                dict_size += 1
            current = bytes([byte])
    
    if current:
        compressed.append(dictionary[current])
    
    return compressed

def lzw_decompress(compressed: List[int]) -> List[int]:
    dictionary = {i: bytes([i]) for i in range(256)}
    dict_size = 256
    current = bytes([compressed.pop(0)])
    decompressed = [current]
    
    for code in compressed:
        if code in dictionary:
            entry = dictionary[code]
        elif code == dict_size:
            entry = current + current[:1]
        else:
            raise ValueError("Bad compressed code: " + str(code))
        
        decompressed.append(entry)
        if dict_size < 4096:
            dictionary[dict_size] = current + entry[:1]
            dict_size += 1
        current = entry
    
    return b"".join(decompressed)

# Number of characters to generate in the sample array
N = 10000

# Generate an array of N random letters
sample = [ord('A') + random.randint(0, ord('Z') - ord('A')) for _ in range(N)]

# Compress the sample array
compressed = lzw_compress(sample)

# Decompress the compressed array
uncompressed = lzw_decompress(compressed)

# Compare the sizes of the compressed and uncompressed arrays
print(f"      Size of the sample array: {N}")
print(f"  Size of the compressed array: {len(compressed)}")
print(f"Size of the uncompressed array: {len(uncompressed)}")

# Test if the sample and the uncompressed arrays are identical
identical = sample == list(uncompressed)
if identical:
    print("The sample and uncompressed arrays are identical.")
else:
    print("Error! The sample and uncompressed arrays are NOT identical.")
