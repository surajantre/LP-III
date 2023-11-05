import heapq
from collections import defaultdict, Counter

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(data):
    frequency = Counter(data)
    heap = [HuffmanNode(char, freq) for char, freq in frequency.items()]
    heapq.heapify(heap)

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = HuffmanNode(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)

    return heap[0]

def build_huffman_codes(root, current_code, huffman_codes):
    if root is None:
        return

    if root.char:
        huffman_codes[root.char] = current_code
    build_huffman_codes(root.left, current_code + '0', huffman_codes)
    build_huffman_codes(root.right, current_code + '1', huffman_codes)

def huffman_encoding(data):
    if len(data) == 0:
        return "", None

    root = build_huffman_tree(data)
    huffman_codes = {}
    build_huffman_codes(root, "", huffman_codes)

    encoded_data = ''.join([huffman_codes[char] for char in data])
    return encoded_data, root

def huffman_decoding(encoded_data, root):
    if not encoded_data:
        return ""

    current = root
    decoded_data = ""
    for bit in encoded_data:
        if bit == '0':
            current = current.left
        else:
            current = current.right

        if current.char:
            decoded_data += current.char
            current = root

    return decoded_data

if __name__ == "__main__":
    data = "This is the example of haffman encoding"
    
    encoded_data, tree = huffman_encoding(data)
    print(f"Encoded data: {encoded_data}")
    
    decoded_data = huffman_decoding(encoded_data, tree)
    print(f"Decoded data: {decoded_data}")
