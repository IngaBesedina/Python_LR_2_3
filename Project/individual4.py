#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    max = 0
    cnt = 1
    st = 'ssaaadrggggg trgddddmj'
    for i in range(len(st)-1):
        if st[i] == st[i+1]:
            cnt += 1
        elif max < cnt:
            max = cnt
        else:
            cnt = 1

    print(f"Исходная строка: {st}")
    print(f"Наибольшее количество идущих подряд символов: {max}")
