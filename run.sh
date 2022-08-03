#!/bin/bash

source ./timetable/bin/activate
python3 index.py
pdfschedule timetable.yaml
deactivate