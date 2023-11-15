#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':
    s = input("Введите строку: ")
    print("Результат: ", s[-1:-len(s)-1:-1])
