import numpy as np
from matplotlib import pyplot as plt
import os
import sys


# o functie care inverseaza bitii pentru a transforma codurile cifrelor de partea stanga in codurile cifrelor de pe
# partea dreapta
def reverse_byte(byte: list[int]) -> list[int]:
    new_b = []
    for i in range(len(byte)):
        if byte[i] == 1:
            new_b.append(0)
        else:
            new_b.append(1)
    
    return new_b


def generate_barcode(barcode, img_path):

    if len(barcode) not in (11, 12) or not barcode.isnumeric() :
       print()
    
    
    # plasa toate cifrele codului de bare intr-o lista
    barcode_list = [int(x) for x in barcode]
    
    # calculam cifra de control si o adaugam in lista in cazul in care aceasta nu a fost precizata de catre utilizator
    checksum = None
    if len(barcode) != 12:
        checksum = 0
        for x in range(0, len(barcode_list), 2):
            checksum += barcode_list[x]
            
        checksum *= 3
        
        for x in range(1, len(barcode_list), 2):
            checksum += barcode_list[x]
        
        checksum = (10 - checksum % 10) % 10
        
        barcode_list.append(checksum)
    
    # un dictionar in care memoram toate codurile pentru fiecare cifra de pe partea stanga a codului de bare
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
    
    
    
    
    
    # sunt adauga toate codurile cifrelor intr-o lista, precum si limitele prestabilite pentru inceput, mijloc si final
    barcode_bytes = []
    barcode_bytes += [1, 0, 1]
    
    for x in range(len(barcode_list)//2):
        barcode_bytes += digit_codes[barcode_list[x]]
        
    barcode_bytes += [0,1,0,1,0]
    
    for x in range(len(barcode_list)//2, len(barcode_list)):
        barcode_bytes += reverse_byte(digit_codes[barcode_list[x]])
        
    barcode_bytes += [1, 0, 1]
    
    
    barcode_guard_patterns = [1,0,1] + 42 * [0] + [0,1,0,1,0] + 42 * [0] + [1,0,1]
    
    # sunt prelungite limitele prestabilite pentru a oferi codului un aspect asemanator cu cel gasit de pe produsele
    # din magazine
    barcode_bytes = [barcode_bytes for x in range(30)]
    
    for x in range(5):
        barcode_bytes.append(barcode_guard_patterns)
    
    # cream si salvam imaginea folosind librariile numpy si matplotlib
    matrix = np.array(barcode_bytes)
    
    plt.imshow(matrix, cmap='gray_r', interpolation='none')
    
    plt.gcf().set_size_inches(matrix.shape[1] / 10, matrix.shape[0] / 10)
    
    plt.axis('off')
    
    
    if checksum:
        barcode = barcode + str(checksum)
    
    if os.path.isdir(img_path):
        barcode_name = f'barcode-{barcode}.png'
        save_path = os.path.join(img_path, barcode_name)
    else:
        save_path = img_path
    
    plt.savefig(save_path, bbox_inches='tight', pad_inches=0.5, dpi=100)
    
    print("Barcode generated!")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python barcode-gen-UPC-A.py <barcode> <img_location>")
    
    barcode = sys.argv[1]
    img_path = sys.argv[2]
    generate_barcode(barcode, img_path)
