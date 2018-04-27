#!/usr/bin/env python3

"""lib file for commands"""

import re
import db_query

def process_text(vtext):
    """Process the text that is returned by Google Assistant"""
    if 'who' in vtext:
        classname = re.sub(r'^.*teaching ', "", vtext)
        print(classname)
        db_query.who(classname)


