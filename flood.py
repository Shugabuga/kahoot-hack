from main import kahoot
import threading

def kahoot_run(pin, x, name):
  send = kahoot(pin, name+str(x))
  send.connect()
  
def test_connection(pin):
  send = kahoot(pin, "Test Name")
  return send.test_conn()
  
def start_kahoot_run():
  t = threading.Thread(target=kahoot_run, args=(pin,x,name,))
  t.daemon = True
  t.start()
  
def get_input():
  pin = input("Please Enter the kahoot pin: ")
  name = input("Please Enter the base name: ")
  exc = input("Please Enter how many names to add: ")
  try:
    return int(pin), str(name), int(exc)
  except:
    print("Please input properly")
    error(0,"not proper input", True)

def esc():
  while True:
    esc = input("> ")
    if esc.lower() == 'e':
      break
    else:
      print("> invalid input")
  
if __name__ == '__main__':
  pin, name, exc = get_input()
  if test_connection(pin):
    print("connecting ...")
    for x in range(exc):
      start_kahoot_run()
    print("\nFinished\nLeave running to keep accounts connected\nPress E to Exit")
    esc()
  else:
    print("Game does not exists with that pin")
