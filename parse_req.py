#!/usr/bin/env python3

"""lib file for commands"""
"""Process the text that is returned by Google Assistant"""
import re
import db_query

def lookup_prof_class(vtext):
    classname = re.sub(r'^.*teaching ', "", vtext)
    print('lookup_prof:', classname)
    return(classname)

def lookup_prof(classname):
    """Get professor names for the class being taught"""
    return(db_query.search(classname, "LAST"))

def get_classnum_class(vtext):
    classname = re.sub(r'^.*course number for ', "", vtext)
    print('classnum:', classname)
    return(classname)

def get_classnum(classname):
    """Get class number associated with the class"""
    return(db_query.search(classname, "CODE"))

def get_roomnum(vtext):
    """Get room number based on class"""
    classname = re.sub(r'^.*teaching ', "", vtext)
    print('roomnum:', classname)
    db_query.search(classname, "ROOM")

def get_daytime(text):
    """Get days and times based on class"""
    classname = re.sub(r'^.*teaching ', "", vtext)
    print('daytime:', classname)
    #may want a customized function for obvious reasons
    #db_query.daytime(classname)
    db_query.search(classname, "DAY")
    db_query.search(classname, "BEG2")
    db_query.search(classname, "ND3")
