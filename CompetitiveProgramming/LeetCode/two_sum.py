#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def main():
  nums = [2,7,11,15]
  target = 9

  for idx, i in enumerate(nums):
    k = target - i
    for jdx, j in enumerate(nums):
      if (idx == jdx):
        continue
      if j == k:
        print(idx, jdx)


if __name__ == '__main__':
  main()
