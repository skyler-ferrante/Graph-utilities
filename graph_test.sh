#!/bin/sh

# Test with titles
./make_box.py "Make box plot" <data/box.txt &
./make_scatter.py "Make scatter plot" <data/scatter.txt &
./make_bar.py "Make bar chart" <data/bar_and_pie.txt &
./make_pie.py "Make pie chart" <data/bar_and_pie.txt &

# Test without titles
./make_box.py <data/box.txt &
./make_scatter.py <data/scatter.txt &
./make_bar.py <data/bar_and_pie.txt &
./make_pie.py <data/bar_and_pie.txt &
