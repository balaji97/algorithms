items = [2, 4, 6, 8, 10, 21]

def binary_search(items, item):
  if len(items) == 0:
    return False
  
  mid = int(len(items)/2)

  if len(items) == 1:
    if(items[mid] == item):
      return True
    else:
      return False
  
  return binary_search(items[:mid], item) or binary_search(items[mid:], item)

if __name__ == "__main__":
  print(binary_search(items, 6))
