import requests

f2 = open("text.txt", "w")
file = open('sub.txt', 'r')
for line in file:
  try:
    if type((requests.head(line)).status_code) == (int):
      f2.write(line.strip()+'\n')
    else:
      continue;
  except:
    continue;
#  _     _             ____        _         
# | |   (_)_   _____  / ___| _   _| |__  ___ 
# | |   | \ \ / / _ \ \___ \| | | | '_ \/ __|
# | |___| |\ V /  __/  ___) | |_| | |_) \__ \
# |_____|_| \_/ \___| |____/ \__,_|_.__/|___/