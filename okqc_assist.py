#!/usr/bin/env python3
# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""A demo of the Google CloudSpeech recognizer."""

import aiy.audio
import aiy.cloudspeech
import aiy.voicehat
import parse_req
import time

def main():
    aiy.i18n.set_language_code('en-US')
    recognizer = aiy.cloudspeech.get_recognizer()
    #recognizer.expect_phrase('turn off the light')
    #recognizer.expect_phrase('turn on the light')
    #recognizer.expect_phrase('blink')
    recognizer.expect_phrase('who')
    recognizer.expect_phrase('what')
    recognizer.expect_phrase('where')
    recognizer.expect_phrase('when')

    button = aiy.voicehat.get_button()
    led = aiy.voicehat.get_led()
    aiy.audio.get_recorder().start()

    while True:
        print('Press the button and speak')
        button.wait_for_press()
        print('Listening...')
        text = recognizer.recognize()
        if text is None:
            print('Sorry, I did not hear you.')
        else:
            print('You said "', text, '"')
            if 'who' in text:
                classname = parse_req.lookup_prof_class(text)
                results = parse_req.lookup_prof(classname)
                try:
                    message = 'is being taught by professor'
                    print(classname, message)
                    texttosay = classname + ' ' + message
                    #print('I am here')
                    
                    for names in results:
                        print(names[0])
                        texttosay = texttosay + ' ' + names[0]
                    #print(texttosay)
                    aiy.audio.say(texttosay)
                except:
                    print("Something went horribly wrong.")
                    
            elif 'what' in text:
                classnum = parse_req.get_classnum_class(text)
                results = parse_req.get_classnum(classnum)
                try:
                    message = 'has a course number of'
                    print(classnum, message)
                    texttosay = classnum + ' ' + message + ' '
                    #print('I am here')
                    
                    for names in results:
                        print(names[0])
                        textresult = parse_req.remove_classsectnum(names[0])
                        print(textresult)
                        #texttosay = texttosay + ' ' + textresult
                        #trying to add spaces in the letters and numbers
                        #so course letters like BUS would not be said literally
                        for letter in textresult:
                            texttosay = texttosay + letter + ' '
                        print(texttosay)
                        break
                    #print(texttosay)
                    aiy.audio.say(texttosay)
                except:
                    print("Something went horribly wrong.")

            elif 'where' in text:
                classname = parse_req.get_roomnum_class(text)
                results = parse_req.get_roomnum(classname)
                try:
                    message = 'is being held in'
                    print(classname, message)
                    texttosay = classname + ' ' + message
                    #print('I am here')
                    
                    for names in results:
                        print(names[0])
                        roomnum_text = parse_req.fix_roomnumtext(names[0])
                        texttosay = texttosay + ' ' + roomnum_text
                    print(texttosay)
                    aiy.audio.say(texttosay)
                except:
                    print("Something went horribly wrong.")

            elif 'when' in text:
                classname = parse_req.get_daytime_class(text)
                results = parse_req.get_daytime(classname)
                try:
                    message = 'is being run in'
                    print(classname, message)
                    texttosay = classname + ' ' + message
                    #print('I am here')
                    
                    for section_tuples in results:
                        #combined_info = section_tuples[0] + ' ' + section_tuples[1] + ' ' + section_tuples[2] + ' ' + section_tuples[3] + ' '
                        combined_info = section_tuples + ' '
                        print(combined_info)
                        texttosay = texttosay + combined_info
                    print(texttosay)
                    aiy.audio.say(texttosay)
                except:
                    print("Something went horribly wrong.")

            #if 'turn on the light' in text:
            #    led.set_state(aiy.voicehat.LED.ON)
            #elif 'turn off the light' in text:
            #    led.set_state(aiy.voicehat.LED.OFF)
            #elif 'blink' in text:
            #    led.set_state(aiy.voicehat.LED.BLINK)
            elif 'end program' in text:
                break

if __name__ == '__main__':
    main()
