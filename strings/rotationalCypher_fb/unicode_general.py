#  rotateCharacter(c, rotationFactor) => { ((c - 'A' + rotationFactor) % 26) + 'A'; }

# O(n) time || O(n) space
def rotationalCipher(input, rotation_factor):
      
  r = []
  for i, k in enumerate(input):
    c = ord(k)
    shift = 0
    
    # lowercase
    if c >= ord('a') and c <= ord('z'):
      shift = (c - ord('a') + rotation_factor) % 26 + ord('a')
    # uppercase
    if c >= ord('A') and c <= ord('Z'):
      shift = (c - ord('A') + rotation_factor) % 26 + ord('A')
    # digits
    if c >= ord('0') and c <= ord('9'):
      shift = (c - ord('0') + rotation_factor) % 10 + ord('0')
      
    if shift > 0:
      r.append(chr(shift))
    else:
      r.append(k)
    
  return ''.join(r)
