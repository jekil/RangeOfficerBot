# Range Officer Bot

Range Officer Bot is a software developed to help you running your dry fire exercise for ISPC Handgun simulating a real stage.
This project was created with ❤️ by [jekil](https://jekil.sexy) to help you in a better a safe training for IPSC competitions.

## Features

Range Officer Bot can work in two modes:

- **Beep Mode**: plays only a start signal (beep), it can be used to test your reflexes.
- **Stage Mode**: simulate the execution of a stage, with Range Officer Bot giving you all the commands from [IPSC Handgun Competition Rules](https://www.ipsc.org/wp-content/uploads/2023/12/IPSC-Handgun-Competition-Rules-Jan-2024-Edition-Final-27-Dec-2023.pdf). The normal prcedure is simulated:

    - Start of "the Course of Fire" with "Load And Make Ready" command (IPSC rule 8.3.1).
    - "Are You Ready?" command (IPSC rule 8.3.2).
    - "Standby" command (IPSC rule 8.3.3).
    - Random 1 to 4 seconds delay of start signal (beep) after timer trigger (IPSC rule 8.3.3 and rule 8.3.4).
    - Wait for a custom delay, giving you the time to execute your dry fire exercise.
    - Finished the dry fire exercise gives the command "If You Are Finished, Unload And Show Clear" (IPSC rule 8.3.6).
    - Put your gun in holster with command "If Clear, Hammer Down, Holster" (IPSC rule 8.3.7).

In Stage Mode you can also simulate, with a random probability of 20%, the Range Officer giving you some special commands:

    - "Stop", during the execution of your dry fire exercise to simulate the Range Officer stopping you for an issue (IPSC rule 8.3.5).
    - "Safety, Holster", at the end of your dry fire exercise to simulate putting your gun loaded in holster

## How To

Range Officer Bot is a command line tool, written in Python and requires Python 3 to work.

You need to install required dependencies with the command (I suggest to use a [virtualenv](https://virtualenv.pypa.io/en/latest/))::

    pip install -r requirements.txt

You can print the help with option *-h*::

    $ python rof.py -h
    usage: ROF [-h] [-b] [-r] [-s] [-p] [-y] [-t EXERCISE_TIME] [-c {female,male}]

    Simulate a IPSC Range Officer for Handgun competitions

    optional arguments:
      -h, --help            show this help message and exit
      -b, --beep-only       Act as beeper only
      -r, --repeat          Repeat forever defined action
      -s, --stage           Run a stage
      -p, --stop            Range Officer use the STOP command at random
      -y, --safety          Range Officer use the SAFETY command at random
      -t EXERCISE_TIME, --exercise-time EXERCISE_TIME
                            Time needed to shot the stage
      -c {female,male}, --character {female,male}
                            Select Range Officer character

    Thanks for playing!

## Credits

Sounds has been created using Text-To-Speech from [TTSMP3](https://ttsmp3.com/), using Kimberly profile for female character and Matthew profile for male character.
MP3 has been converted to WAV using [Cloudconvert](https://cloudconvert.com/mp3-to-wav). 
