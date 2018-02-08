# Andrew Xia
# 180208
# Basic submission



if __name__ == '__main__':
  with open("data/train.csv", 'r') as infile:
    totalSurvived = 0
    count = 0
    i = 0
    for line in infile:
      a = line.split(",")
      # print a

      if a[1] == "0":
        count += 1
      elif a[1] == "1":
        count += 1
        totalSurvived += 1

  # print totalSurvived
  # print count

  probSurvive = totalSurvived * 1.0 / count

  # dumb classifier, randomly output based on survival chance
  import random as r
  with open("submission/0208.csv", "w") as outfile:
    outfile.write("PassengerId,Survived\n")
    for i in range(892,892 + 418):
      if r.random() < probSurvive:
        outfile.write(str(i) + ",1\n")
      else:
        outfile.write(str(i) + ",0\n")

