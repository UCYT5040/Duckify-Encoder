# How it works:
# space ( ) shows a new character.
# Every new character has a value.
# duck (🦆) is worth 1
# corn (🌽) is worth 10
# lettuce (🥬) is worth 100
# It checks how many lettuce it can subtract.
# Then, how many corn.
# Last, how many duck.
# Example:
# Duckify 'a'
# ord('a') = 97
# Duckified: '🌽🌽🌽🌽🌽🌽🌽🌽🌽🦆🦆🦆🦆🦆🦆🦆' 9 corn * 10 per corn = 90 + 7 duck * 1 per duck = 97
# -----
# Example:
# Duckify 'abc'
# ord('a') = 97
# ord('b') = 98
# ord('c') = 99
# Duckified: '🌽🌽🌽🌽🌽🌽🌽🌽🌽🦆🦆🦆🦆🦆🦆🦆 🌽🌽🌽🌽🌽🌽🌽🌽🌽🦆🦆🦆🦆🦆🦆🦆🦆 🌽🌽🌽🌽🌽🌽🌽🌽🌽🦆🦆🦆🦆🦆🦆🦆🦆🦆' # space ( ) is used to show a new character
def can_subtract(minuend, subtrahend):
  return minuend - subtrahend >= 0
print("Please note that duckify_output.txt will be used for outputting both encode and decode. If you decode and use duckify_output.txt as input, it will be replaced with new contents.")
mode = input("Encode, EncodeFile, or Decode? ").lower()
if mode in ['encode', 'en', 'e', 'enco', 'encoded']:
  toEncode = input("Enter string to encode: ")
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
  open("duckify_output.txt", "w").write(output)
  print("Written to duckify_output.txt.")
elif mode in ['decode', 'de', 'd', 'deco', 'decoded']:
  toDecode = input("Enter file name of string to decode (defualt is duckify_output.txt): ")
  if toDecode == '': toDecode = 'duckify_output.txt'
  chars = open(toDecode, "r").read().split()
  output = ""
  for char in chars:
    value = 0
    for emoji in char:
      if emoji == "🥬": value += 100
      elif emoji == "🌽": value += 10
      elif emoji == "🦆": value += 1
    output += chr(value)
  open("duckify_output.txt", "w").write(output)
  print("Written to duckify_output.txt.")
elif mode in ['encodefile', 'enfi', 'ef', 'encofile', 'encodedfile']:
  toEncode = open(input("Enter file name of string to encode: "), "r").read()
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
  open("duckify_output.txt", "w").write(output)
  print("Written to duckify_output.txt.")