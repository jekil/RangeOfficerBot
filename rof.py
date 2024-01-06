# Range Officer Bot is your companion in IPSC Handgun training.
# Copyright (C) 2024 Alessandro Tanasi
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import argparse
import os
import simpleaudio as sa
from random import randint
from time import sleep


# Sounds.
BEEP_FILE = "beep.wav"
ARE_YOU_READY_FEMALE = "are_you_ready-female.wav"
ARE_YOU_READY_MALE = "are_you_ready-male.wav"
IF_CLEAR_FEMALE = "if_clear-female.wav"
IF_CLEAR_MALE = "if_clear-male.wav"
IF_FINISHED_FEMALE = "if_you_are_finished-female.wav"
IF_FINISHED_MALE = "if_you_are_finished-male.wav"
LOAD_FEMALE = "load_and_make_ready-female.wav"
LOAD_MALE = "load_and_make_ready-male.wav"
SAFETY_FEMALE = "safety-female.wav"
SAFETY_MALE = "safety-male.wav"
STANDBY_FEMALE = "stand_by-female.wav"
STANDBY_MALE = "stand_by-male.wav"
STOP_FEMALE = "stop-female.wav"
STOP_MALE = "stop-male.wav"


def get_sound(filename):
    """Get sound path."""
    return os.path.join(os.getcwd(), "sounds", globals()[filename])

def play_sound(name):
    """Plays a sound."""
    wave_obj = sa.WaveObject.from_wave_file(get_sound(name))
    play_obj = wave_obj.play()
    play_obj.wait_done()

def beep_sound():
    """Play beep sound."""
    print("BEEP")
    play_sound("BEEP_FILE")

def random_beep():
    """Play beep sound with a random interval from 1 to 4 seconds."""
    sleep(randint(1,4))
    beep_sound()

def run_stage(args):
    print("Load and make ready")
    play_sound("LOAD_" + args.character.upper())
    sleep(4)
    print("Are you ready?")
    play_sound("ARE_YOU_READY_" + args.character.upper())
    sleep(2)
    play_sound("STANDBY_" + args.character.upper())
    random_beep()
    # Random STOP given by Range Officer.
    if args.stop and randint(1, 5) == 1:
        sleep(randint(0, args.exception))
        play_sound("STOP" + args.character.upper())
    else:
        sleep(args.exercise_time)
    # Random SAFETY given by Range Officer.
    if args.safety and randint(1, 5) == 1:
        play_sound("SAFETY_" + args.character.upper())
    else:
        play_sound("IF_FINISHED_" + args.character.upper())
        sleep(4)
        play_sound("IF_CLEAR_" + args.character.upper())

def end_loop():
    """Ends repeat cycle, when in repat mode."""
    print("Range Officer completed the job!")
    sleep(4)
    print("Range office is working again!")
    sleep(1)

if __name__ == "__main__":

    parser = argparse.ArgumentParser(
                prog="ROF",
                description="Simulate a IPSC Range Officer for Handgun competitions",
                epilog="Thanks for playing!")
    parser.add_argument("-b", "--beep-only", dest="beep", action="store_true", help="Act as beeper only")
    parser.add_argument("-r", "--repeat", dest="repeat", action="store_true", help="Repeat forever defined action")
    parser.add_argument("-s", "--stage", dest="stage", action="store_true", help="Run a stage")
    parser.add_argument("-p", "--stop", dest="stop", action="store_true", help="Range Officer use the STOP command at random")
    parser.add_argument("-y", "--safety", dest="safety", action="store_true", help="Range Officer use the SAFETY command at random")
    parser.add_argument("-t", "--exercise-time", dest="exercise_time", action="store", default=4, help="Time needed to shot the stage")
    parser.add_argument("-c", "--character", dest="character", action="store", choices=["female", "male"], default="male", help="Select Range Officer character")
    args = parser.parse_args()

    # Safety check.
    if args.beep and args.stage:
        print("You cannot use beep mode and stage mode at the same time. Exiting.")
    elif not args.beep and not args.stage:
        print("No selected mode. Using stage mode as default.")
        args.stage = True

    # Main login.
    if args.beep:
        if args.repeat:
            while True:
                print("Selected mode: beeper (repeat).")
                random_beep()
                end_loop()
        else:
            print("Selected mode: beeper.")
            random_beep()
    elif args.stage:
        if args.repeat:
            while True:
                print("Selected mode: stage (repeat).")
                run_stage(args)
                end_loop()
        else:
            print("Selected mode: stage.")
            run_stage(args)

