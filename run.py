#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def optional_introduce(func):
    
    def wrapper (*args, introduce=False, **kwargs):
        if introduce is True:
            print(func.__name__)
        func(*args, **kwargs)
        
    return wrapper 

@optional_introduce
def print_given(*args, **kwargs):
    answer = ""
    for arg in args:
        print(f"{arg} {type(arg)}")
        
    for k,v in kwargs.items():
        print(f"{k} {v} {type(v)}")
    
    return answer
    
print("\n", "="*50, "  test 1", "\n")
print(print_given( 1, 2, 3, [1, 2, 3], 'one', 'two', 'three', two = 2, one = 1, three = 3))
print("\n", "="*50,"  test 2", "\n")
print(print_given( 2, 3, [1, 2, 3], 'one', 'two', 'three', two = 2, one = 1, three = 3))
print("\n", "="*15, " here input function name ", "="*15," test 3", "\n")
print(print_given(1, 2, 3, [1, 2, 3], 'one', 'two', 'three', two = 2, one = 1, three = 3, introduce=True))
print("\n", "="*50, "\n")