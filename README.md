# diff
Output file difference, linux command ```diff``` enhancement.

Use [Levenshtein](https://pypi.org/project/python-Levenshtein/) to output minimum difference between line modifications output from linux command ```diff```.

Use ```python diff.py (original file address) (new file address) (output file address)``` to execute.

Try ```python diff.py sample/a.txt sample/b.txt sample/c.txt``` to see sample effect.

sample/a.txt:
蝙蝠侠打不过超人
蝙蝠侠有钱
蝙蝠侠高富帅
蜘蛛侠没钱
abcd
野村综研
这行一样
这行不一样

sample/b.txt:
蝙蝠侠打不过超人
蜘蛛侠有钱
蝙蝠侠高富帅
蜘蛛侠穷
bacd
野村総研
这行一样
ここ違う

sample/c.txt:
line #2: 蜘蛛
line #4: 穷
line #5: ba
line #6: 総
line #8: ここ違う

Linux `diff a.txt b.txt` output:
2c2
< 蝙蝠侠有钱
---
> 蜘蛛侠有钱
4,6c4,6
< 蜘蛛侠没钱
< abcd
< 野村综研
---
> 蜘蛛侠穷
> bacd
> 野村総研
8c8
< 这行不一样
\ No newline at end of file
---
> ここ違う
\ No newline at end of file