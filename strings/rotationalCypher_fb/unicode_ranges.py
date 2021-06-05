def rotationalCipher(input, rotation_factor):
  
  r = []
  for i, k in enumerate(input):
    letter = ord(k)
    shift = 0
    
    # lowercase
    if letter >= 65 and letter <= 90:
      letter -= 65
      shift = 65 + (letter + rotation_factor) % 26
    # uppercase
    if letter >= 97 and letter <= 122:
      letter -= 97
      shift = 97 + (letter + rotation_factor) % 26
    # digits
    if letter >= 48 and letter <= 57:
      letter -= 48
      shift = 48 + (letter + rotation_factor) % 10
      
    if shift > 0:
      r.append(chr(shift))
    else:
      r.append(k)
    
  return ''.join(r)
