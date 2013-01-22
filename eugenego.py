#! /usr/bin/env python

# Arguments
# -o output HTML file
# -f input file of topics
# -t specify squares with topics... somehow
# -F Add to make the center square a "FREE" square

#import argparse #blah do this later
import sys
import random
import time

def header():
  header = """<html>
    <head>
      <link href='styles.css' rel='stylesheet' type='text/css' />
      <link href='http://fonts.googleapis.com/css?family=Risque|Playfair+Display+SC|Cabin+Condensed|Uncial+Antiqua|Norican' rel='stylesheet' type='text/css'>
    </head>
    <body>\n<h1 class="title">Eugenego</h1>\n\n<h3 class="motto">Eugenego is played for keeps</h3>\n\n
    <h4 class="rules">Name of the game must be shouted on victory</h4>"""
  return header

def seed_info(millis):
  info = "\n<h5> Board generated with seed:%(millis)i </h5>\n" % {"millis": millis}
  return info

def footer():
  footer = """\n</body>\n</html>"""
  return footer

def table(data):
  table_html = "<table>\n"
  for i,datum in enumerate(data):
    if i == 0:
      table_html = table_html + "<tr>\n"
    elif i % 5 == 0:
      table_html = table_html + "\n</tr>\n<tr>\n"
    table_html = table_html + "\t<td>" + datum + "</td>\n"
    if i == 24:
      table_html = table_html + "\n</tr>\n"
  table_html = table_html + "</table>"
  return table_html

millis = int(time.time())
output = "output_" + str(millis) + ".html"
input_file_name = "eugene_topics.txt"
free_square = False
topics_hash = None

input_file = open(input_file_name, 'r')
output_file = open(output, 'w')

lines = [i.strip() for i in input_file.readlines()]
sampling = random.sample(lines, 25)

if free_square:
  sampling[12] = "FREE"

output_file.write(header())
output_file.write(table(sampling))
output_file.write(seed_info(millis))
output_file.write(footer())
