"""
  0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg


a = symm diff of length-2 and length-3 (from 1 and 7)
bd = symm diff of length-2 and length-4 (from 1 and 4)
g = symm diff of (union of length-3 and length-4) with bd (7 U 4 and 9)




 """




segmentsToDigitDict = {
    'abcefg': 0, # 6
    'cf': 1, # 2
    'acdeg': 2, # 5
    'acdfg': 3, # 5
    'bcdf': 4, # 4
    'abdfg': 5, # 5
    'abdefg': 6, #6
    'acf': 7, # 3
    'abcdefg': 8, # 7
    'abcdfg': 9 # 6
}