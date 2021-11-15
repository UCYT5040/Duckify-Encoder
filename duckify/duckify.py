def can_subtract(minuend, subtrahend):
  return minuend - subtrahend >= 0

def encode(toEncode):
  output = ""
  for char in toEncode:
    charInt = ord(char)
    while can_subtract(charInt, 100):
      output += '🥬'
      charInt -= 100
    while can_subtract(charInt, 10):
      output += '🌽'
      charInt -= 10
    while can_subtract(charInt, 1):
      output += '🦆'
      charInt -= 1
    output += ' '
  return output
def decode(toDecode):
  chars = toDecode.split()
  output = ""
  for char in chars:
    value = 0
    for emoji in char:
      if emoji == "🥬": value += 100
      elif emoji == "🌽": value += 10
      elif emoji == "🦆": value += 1
    output += chr(value)
  return output