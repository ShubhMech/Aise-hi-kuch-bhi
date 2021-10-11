# -*- coding: utf-8 -*-
"""
Created on Mon Oct 11 23:48:20 2021

@author: Asus
"""

import hp, code, zombie, hunger_games
import random

if __name__ == "__main__":
    m = random.choice([hp, code, zombie, hunger_games])
    m.madlib()