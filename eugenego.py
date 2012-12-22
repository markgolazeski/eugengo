#! /usr/bin/env python

# Arguments
# -o output HTML file
# -f input file of topics
# -t specify squares with topics... somehow
# -F Add to make the center square a "FREE" square

#import argparse #blah do this later
import sys
import random

def header():
  header = """<html>
    <head>
      <link href='styles.css' rel='stylesheet' type='text/css' />
      <!--<link href='http://fonts.googleapis.com/css?family=Donegal+One' rel='stylesheet' type='text/css' />-->
      <link href='http://fonts.googleapis.com/css?family=Playfair+Display+SC' rel='stylesheet' type='text/css' />
    </head>
    <body>\n<h1>Eugenego</h1>\n\n<h3>It's played for keeps</h3>\n\n
    <h4>Name of the game must be shouted on victory</h4>"""
  return header

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

output = "output.html"
input_file_name = "random_topics.txt"
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
output_file.write(footer())
