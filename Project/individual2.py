#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    s = input("Введите слово: ")
    if s == s[-1:-len(s)-1:-1]:
        print("Слово является палиндромом")
    else:
        print("Слово не является палиндромом")
