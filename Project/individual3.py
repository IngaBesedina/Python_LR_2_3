#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    s = input("Введите слово: ")
    if 'о' in s:
        idx = s.find('о')
        s = s[:idx] + s[idx+1:]
    if 'л' in s:
        idx = s.rfind('л')
        s = s[:idx] + s[idx+1:]
print(f"Результат: {s}")
