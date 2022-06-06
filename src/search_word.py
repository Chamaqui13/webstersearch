
import requests, json
from requests.exceptions import HTTPError

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

def webster_search(word, api_key):
    try:
        url = "https://dictionaryapi.com/api/v3/references/collegiate/json/" + word + "?key=" + api_key
        print(url)
        response  = requests.get(url)
        #Check for the successful response
        response.raise_for_status()
        #return response.json()[0]
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)
    except HTTPError as http_err:
        print(f'HTTP error: {http_err}')
    except Exception as err:
        print(f'Error: {err}')
        raise SystemExit(err)
    else:
        #print(response.text)
        if is_json(response.text) and type(response.json()[0]) is dict: 
            return response.json()[0]
        else:
            if is_list(response.text):
                raise SystemExit(f'Error word not found, Do you mean any of these?: {response.text}')
            else:
                raise SystemExit(f'Error: {response.text}')

def parse_word(my_dict):
    #my_dict = response.json()[0]
    str = my_dict["hwi"]["prs"][0]["mw"] + " ("  + my_dict["fl"] +  ") " + my_dict["def"][0]["sseq"][0][0][1]["dt"][0][1]
    return str
