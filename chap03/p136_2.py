#with open('sample.txt','r') as f:
 #   data = f.readline()
  #  line = data.strip()

with open('sample.txt','r') as f:
    for line in f:
        print(line.strip())
