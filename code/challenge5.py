from typing import Dict, List, Tuple

def decode(encoded: str, codebook: Dict[str, str])-> str:
   decoded = ""
   # get a list of the codes in descending order of code length i.e. longest code first
   codes_by_length = order_codes( codebook )
   # get decode book - by inverting the codebook
   decode_book = make_decodebook( codebook )
   sum_match_length = 0
   num_matches = 0

   while len(encoded):
      prefix_match = find_longest_match(encoded, codes_by_length)
      if prefix_match:
         # remove the matched prefix from encoded
         encoded = encoded[len(prefix_match):]
         decoded = decoded+decode_book[prefix_match]
         sum_match_length += len(prefix_match)
         num_matches += 1
         print("Prefix matched:", prefix_match, "length:", len(prefix_match))
         print("Total length matched so far:", sum_match_length)
         print("Decoded so far:", decoded)
         print()
      else:
         break

   # Length of valid encoded string should be 0 after matching
   print("Check encoded length at end:", len(encoded)) 
   if len(encoded):
      print("Error: not a valid encoding")
      decoded="-1"
   print("Total number of matches:", num_matches)
   print()
   return decoded

# from the generic codebook, extract the codes and lengths in a list
# in order of descending lengths of code.  This assumes
# the generic codebook is ordered with codes as values in
# ascending order of code length
def order_codes(codebook: Dict[str,str])-> List[ Tuple[str, int] ]:
   code_list = [ ( codebook[k], len(codebook[k]) ) for k in codebook.keys()  ]
   code_list = code_list[::-1]
   return code_list

# Invert a dictionary by interchanging keys and values
# Assumes keys and values are unique
def make_decodebook(codebook: Dict[str, str])->Dict[str, str]:
   decode_book = {codebook[k] : k for k in codebook}
   return decode_book

# def make_specific_codebook(codebook_gen: Dict[int, str], letters_byfreq: str)->Dict[str, str]:
#    codebook_specific = { letters_byfreq[k] : codebook_gen[k] for k in range(len(letters_byfreq))}
#    return codebook_specific

# Finds the longest prefix match for encoded string from list of codes
# Returns an empty string if no match is found
def find_longest_match(encoded: str, code_list: List[Tuple[str, int]])->str:
   longest_match=""
   for s in code_list:
      if encoded[ : s[1] ] == s[0]:
         longest_match = s[0]
         break
   return longest_match


if __name__ == '__main__':


    encoded =  "1111101111111111000111111100101111110101111111110011011111111111000100111111010" + \
               "0111100110111111100101111010010111111000111111111110001101111110101110011011111" + \
                "1111110001101111010011111100101111110010110111111101001111001101111111111100010" + \
                "11101100011111110111111111001110111111111110001111110111111101011111111110001111" + \
                "11011111110011111111111000111101111111011111111010011111111110001001111110100110" + \
                "01111111111000111011111111110101111101111111010111110111111010011110011111111110" + \
                "00100111111010011001111111111000111111011111111110001110011111011111110011111110" + \
                "01011111011111100011101111111111100011111111010111101110111111111110001111111110" + \
                "11111110101111111100011001111111111000111111111110001111111111100011111111010111" + \
                "1010011111110101111111111000100111111011011111101101101001111111000111111100111" + \
                "11111111000111111011111101001111111111000111111110101111011101111111111100011111" + \
                "11011011110111111110000011111110011101"
   
    codebook={    'a': '00',
                  'b': '01',
                  'c': '10',
                  'd' : '1100',
                  'e' : '1101',
                  'f': '1110',
                  'g' : '111100',
                  'h': '111101',
                  'i': '111110',
                  'j': '1111110000',
                  'k' : '1111110001',
                  'l' : '1111110010',
                  'm' : '1111110011',
                  'n' : '1111110100',
                  'o' : '1111110101',
                  'p' : '1111110110',
                  'q' : '1111110111',
                  'r' : '1111111000',
                  's' : '1111111001',
                  't' : '1111111010',
                  'u' : '1111111011',
                  'v' : '1111111100',
                  'w' : '1111111101',
                  'x' : '1111111110',
                  'y' : '1111111111',
                  'z' : '11111111110000',
                  '!' : '11111111110001'   # replace ' ' with '!' for clear display
            }


    # Test making the decode book
    decode_book = make_decodebook(codebook)
    print("Decode_book length:", len(decode_book))
    print("Decode Book:")
    print(decode_book)
    print()

    # extract the codes in a list in descending code length
    code_list = order_codes(codebook)
    print("Code list length:", len(code_list))
    print("Code List:")
    print(code_list)
    print()

    # check encoded string
    print(encoded)
    print("Length of encoded string:", len(encoded))
    print()

    # test the prefix match
    prefix = find_longest_match(encoded, code_list)
    print("Longest matched prefix:")
    print(prefix)
    print("Prefix decoded: ", decode_book[prefix])
    print()

    # test the decoding
    decoded = decode(encoded, codebook)
    print("Length of decoded string:", len(decoded))
    print("Decoded string:")
    print(decoded)
    print()

# Expected output: (replace ! with space character)
#
# Check encoded length at end: 0
# Total number of matches: 114
#
# Length of decoded string: 114
# Decoded string:
# i!love!angelhack!code!challenge!because!it!is!fun!and!exciting!and!i!dislike!the!word!!!that!appears!in!the!phrase
