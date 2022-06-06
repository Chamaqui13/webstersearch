import json

def is_list(mylist):
  try:
    lista = json.loads(mylist)
  except ValueError as e:
    return False
  if type(lista) is list:
    return True
  else:
      return False

def is_json(myjson):
  try:
    json.loads(myjson)
  except ValueError as e:
    return False
  return True