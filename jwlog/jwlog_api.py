#!/usr/bin/env python
# coding: utf-8

def tty_to_html(value):
    newvalue = []
    delete_colors = ["\x1b[1;34m","\x1b[0m","\x1b[1;33m","\x1b[1;31m","\x1b[1;44m"]
    for delete_color in delete_colors:
        value = value.replace(delete_color,'')
    for value in value.split("\n"):
        if value == '':
            continue
        if "[E]" in value:
            newvalue.append("""<font color="red">%s</font>""" % (value))
        elif "[W]" in value:
            newvalue.append("""<font color="#f8ac59">%s</font>""" % (value))
        elif "[D]" in value:
            newvalue.append("""<font color="#59f892">%s</font>""" % (value))
        else:
            newvalue.append("""<font>%s</font>""" % (value))
    return newvalue