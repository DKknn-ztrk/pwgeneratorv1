# pwgeneratorv1

**screenshot from `pwgeneratorv1.py`**

![3](https://user-images.githubusercontent.com/54024035/146098975-710df2cc-aa48-4558-9f87-fb864c5c4acd.png)

```
import random
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHİJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbol = "[]{}#()*;,_-!%&/"
all = lower + upper + number + symbol
length = 18
password = "".join(random.sample(all,length))
print("Your new password is =  ",password)
```
