import numpy as np
from matplotlib import pyplot as plt

barcode = input("Enter an 11 (or 12) digit barcode: ")

if len(barcode) not in (11, 12) or barcode == 'test' or not barcode.isnumeric() :
    barcode = '03600029145'
    print("This is a sample barcode!")

barcode_list = [int(x) for x in barcode]

if len(barcode) != 12:
    checksum = 0
    for x in range(0, len(barcode_list), 2):
        checksum += barcode_list[x]
        
    checksum *= 3
    
    for x in range(1, len(barcode_list), 2):
        checksum += barcode_list[x]
    
    checksum = (10 - checksum % 10) % 10
    
    barcode_list.append(checksum)

digit_codes = {
    0: [0, 0, 0, 1, 1, 0, 1],
    1: [0, 0, 1, 1, 0, 0, 1],
    2: [0, 0, 1, 0, 0, 1, 1],
    3: [0, 1, 1, 1, 1, 0, 1],
    4: [0, 1, 0, 0, 0, 1, 1],
    5: [0, 1, 1, 0, 0, 0, 1],
    6: [0, 1, 0, 1, 1, 1, 1],
    7: [0, 1, 1, 1, 0, 1, 1],
    8: [0, 1, 1, 0, 1, 1, 1],
    9: [0, 0, 0, 1, 0, 1, 1],
}


def reverse_byte(byte: list[int]) -> list[int]:
    new_b = []
    for i in range(len(byte)):
        if byte[i] == 1:
            new_b.append(0)
        else:
            new_b.append(1)
            
    return new_b
    
    
barcode_bytes = []
barcode_bytes += [1, 0, 1]

for x in range(len(barcode_list)//2):
    barcode_bytes += digit_codes[barcode_list[x]]
    
barcode_bytes += [0,1,0,1,0]

for x in range(len(barcode_list)//2, len(barcode_list)):
    barcode_bytes += reverse_byte(digit_codes[barcode_list[x]])
    
barcode_bytes += [1, 0, 1]


barcode_guard_patterns = [1,0,1] + 42 * [0] + [0,1,0,1,0] + 42 * [0] + [1,0,1]

barcode_bytes = [barcode_bytes for x in range(30)]


for x in range(5):
    barcode_bytes.append(barcode_guard_patterns)

matrix = np.array(barcode_bytes)

plt.imshow(matrix, cmap='gray_r', interpolation='none')

plt.gcf().set_size_inches(matrix.shape[1] / 10, matrix.shape[0] / 10)

plt.axis('off')

plt.savefig(f'barcode-{barcode + str(checksum)}.png', bbox_inches='tight', pad_inches=0.5, dpi=100)

print("The barcode has been generated!")


