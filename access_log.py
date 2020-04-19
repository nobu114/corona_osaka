import re
# import sys
import pathlib


path = pathlib.Path(__file__).joinpath(
    "..", "log", "access.log"
).resolve()
"""
for line in path.open():
    line = line.strip()
    print(line)
"""
with path.open(mode="r") as f:
    f_rstrip = [s.rstrip("\n") for s in f.readlines()]
hoge = re.split('[" ]', f_rstrip[0])
print(hoge)
print(len(hoge))