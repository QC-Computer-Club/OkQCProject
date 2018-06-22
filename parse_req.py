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

def remove_classsectnum(classnum):
    """Removes class number associated with the class"""
    #classnum = classnum.upper()
    classnumresult = re.match(r"([A-Z][A-Z][A-Z])\s([0-9][0-9][0-9])\s([F0-9][0-9])", classnum.upper())
    return(classnumresult.group(1) + ' ' + classnumresult.group(2))

def get_roomnum_class(vtext):
    """Get class name before getting room number"""
    #classname_result = re.match(r'Where is (.*) section ([F0-9][0-9]) being taught?', vtext)
    classname_result = re.match(r'where is (.*) being', vtext)
    #print(classname_result.group(1))
    
    return(classname_result.group(1))

def get_roomnum(classname):
    """Get room number based on class"""
    #classname_result = re.match(r'Where is (.*) section ([F0-9][0-9]) being taught?', classname)
    print('roomnum:')    
    return(db_query.search(classname, "ROOM"))

def fix_roomnumtext(roomnum):
    """Fix room number for text-to-voice converter"""
    PPlace = 'Pp'
    PPlaceVal = "President\'s Place"
    Sav = 'S'
    SavVal = 'Saville Hall'
    newroomnum = ''
    for somechar in roomnum:
        if somechar.isdigit():
            newroomnum = newroomnum + ' ' + somechar
        else:
            newroomnum = newroomnum + somechar
            
    if PPlace in roomnum:
        #roomnumresult = re.match(r"[P][P][0-9][0-9][0-9]", roomnum)
        newroomnum = re.sub(PPlace, PPlaceVal, newroomnum)
        return(newroomnum)
    elif Sav in roomnum:
        newroomnum = re.sub(Sav, SavVal, newroomnum)
        return(newroomnum)
    else:
        print("Not a valid room")

def get_daytime(text):
    """Get days and times based on class"""
    classname = re.sub(r'^.*teaching ', "", vtext)
    print('daytime:', classname)
    #may want a customized function for obvious reasons
    #db_query.daytime(classname)
    db_query.search(classname, "DAY")
    db_query.search(classname, "BEG2")
    db_query.search(classname, "ND3")
