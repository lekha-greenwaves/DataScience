from sys import argv
filename, time, salary, prize = argv
time = int(time)
salary = int(salary)
prize = int(prize)
total = time * salary + prize
print(f"заработная плата составила  {total}")
