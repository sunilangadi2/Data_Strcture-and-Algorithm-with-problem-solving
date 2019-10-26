
def is_unique(string):
  if len(string) > 128:
    return False

  boolean_tracker = [False] * 128
  for char in string:
  	#ord gives the ascci value of char
    if boolean_tracker[ord(char)] == False:
      boolean_tracker[ord(char)] = True
    else:
      return False
  return True

print(is_unique('sunil'))
