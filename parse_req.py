#!/usr/bin/env python3

"""lib file for commands"""
"""Process the text that is returned by Google Assistant"""
import re
import db_query

def lookup_prof_class(vtext):
    """
    Get classname from query before looking up professor
    Pre: Voice text from user passed to this function
    Post: Returns classname from text, assuming valid class
    """
    #classname = re.sub(r'^.*teaching ', "", vtext)
    classnameresult = re.match('who is teaching (.*)', vtext)
    print('lookup_prof_class:', classnameresult.group(1))
    #return(classname)
    return(classnameresult.group(1))

def lookup_prof(classname):
    """
    Get professor names for the class being taught
    Pre: This function gets a valid class
    Post: Returns a tuple that contains information
    """
    print('lookup_prof:')
    return(db_query.search(classname, "LAST"))

def get_classnum_class(vtext):
    """
    Get classname from query before looking up class id/course #
    Pre: Voice text from user passed to this function
    Post: Returns classname from text, assuming valid class
    """
    #classname = re.sub(r'^.*course number for ', "", vtext)
    classnameresult = re.match('(.*) course number for (.*)', vtext)
    print('get_classnum_class:', classnameresult.group(2))
    #return(classname)
    return(classnameresult.group(2))

def get_classnuminfo(classinfo, numresult):
    """
    Get classnum/course # info based on classname
    Pre: Assumes valid classname passed to this function
    Post: Returns course # info according to valid classname
    """
    #classes are always in this format CSI 116 01
    # 1 -> course type designation ex: CSI
    # 2 -> course number ex: 116
    # 3 -> section number ex: 01
    classnumresult = re.match(r"([A-Z][A-Z][A-Z])  ([0-9][0-9][0-9])  ([F0-9][0-9])", classinfo.upper())
    print('get_classnuminfo:', classnumresult.group(numresult))
    return(classnumresult.group(numresult))

def get_classnum(classname):
    """
    Get class number associated with the classname
    Pre: Assume a valid classname is passed to the function
    Post: Returns result based on the classname
    """
    print('get_classnum:')
    return(db_query.search(classname, "CODE"))

def remove_classsectnum(classnum):
    """
    # Removes class section number associated with the class
    Pre: Assumes a valid course # (that should include section #) is provided
    Post: Returns course # with the section # removed
    """
    #classnumresult = re.match(r"([A-Z][A-Z][A-Z])  ([0-9][0-9][0-9])  ([F0-9][0-9])", classnum.upper())
    #return(classnumresult.group(1) + ' ' + classnumresult.group(2))
    print('remove_classsectnum:', get_classnuminfo(classnum, 1), get_classnuminfo(classnum, 2))
    return(get_classnuminfo(classnum, 1) + ' ' + get_classnuminfo(classnum, 2))

def get_roomnum_class(vtext):
    """
    Get class name before getting room number
    Pre: Assumes good voice text input
    Post: Returns classname
    """
    #classname_result = re.match(r'Where is (.*) section ([F0-9][0-9]) being taught?', vtext)
    classname_result = re.match(r'where is (.*) being', vtext)
    #print(classname_result.group(1))
    print('get_roomnumclass:', classname_result.group(1))
    return(classname_result.group(1))

def get_roomnum(classname):
    """
    Get room number based on classname
    Pre: Assumes valid classname
    Post: Returns room # info
    """
    #classname_result = re.match(r'Where is (.*) section ([F0-9][0-9]) being taught?', classname)
    print('get_roomnum:')    
    return(db_query.search(classname, "ROOM"))

def fix_roomnumtext(roomnum):
    """
    Fix room number for text-to-voice converter
    Pre: Assumes valid course num
    Post: Returns complete room info (text replacement)
    """
    
    upperroomnum = roomnum.upper()
    print('fix_roomnumtext:')
    PPlace = 'PP'
    PPlaceVal = "President\'s Place"
    Sav = 'S'
    SavVal = 'Saville Hall'
    newroomnum = ''
    for somechar in upperroomnum:
        if somechar.isdigit():
            newroomnum = newroomnum + ' ' + somechar
        else:
            newroomnum = newroomnum + somechar
            
    if PPlace in upperroomnum:
        #roomnumresult = re.match(r"[P][P][0-9][0-9][0-9]", roomnum)
        newroomnum = re.sub(PPlace, PPlaceVal, newroomnum)
        return(newroomnum)
    elif Sav in upperroomnum:
        newroomnum = re.sub(Sav, SavVal, newroomnum)
        return(newroomnum)
    else:
        print("Not a valid room")

def get_daytime_class(vtext):
    """
    Get class name before getting day+time of class
    Pre: Assumes good voice text input
    Post: Returns classname
    """

def get_daytime(vtext):
    """
    Get days and times based on class
    Pre: Assumes valid classname
    Post: Returns list of tuples containing class day and times
    """
    print('get_daytime:')
    classname = re.match(r'when is (.*) being run', vtext)
    print('daytime:', classname)
    #may want a customized function for obvious reasons
    #db_query.daytime(classname)
    #db_query.search(classname, "DAY")
    #db_query.search(classname, "BEG2")
    #db_query.search(classname, "ND3")
