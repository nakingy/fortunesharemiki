import random

n = random.randint(0,2)

if n == 0:
  unsei = "daikichi_大吉"
elif n == 1:
  unsei = "chukichi_中吉"
else:
  unsei = "shokichi_小吉"

print("あなたの今日の運勢は \"" + unsei + "\" です")
print("uranaisyuryo_占い終了")
