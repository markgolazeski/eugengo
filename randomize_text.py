#!/usr/bin/env python

# Take the good topics and turn them into gibberish, so they stay secret :P

import string
import random

upper_lower = string.printable[10:62]

in_file = open('eugene_topics.txt', 'r')
out_file = open('random_topics.txt', 'w')
in_lines = in_file.readlines()
out_lines = [''.join([ random.choice(upper_lower) if c in upper_lower else c for c in line]) for line in in_lines]
for line in out_lines:
  out_file.write(line)
