# Timesheets

## Purpose
A program to automatically calculate monthly work time and monthly salary based on info in Excel files also 
prepare reports with predefined format.

## Structure
The DB is a dictionary, where: 
1. The names of the employees must be in english.
2. The names of the projects in the common timesheets must be included in the names of the separate timesheets file. 
Case-insensitive.

## To compile
pyinstaller --onefile --noconsole main.py
