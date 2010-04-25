#!/usr/bin/env python
# -*- coding: ascii -*-


#   Copyright 2010 Ashish Sharma <eraser029@gmail.com>
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

""" This script runs the irc bot.
"""

from IrcBot import IrcBot


def main():
    """Entry point of the module"""
    bot = IrcBot.IrcBot()
    bot.connect()
    bot.mainloop()
    bot.cleanup()

# Execute only when ran explicitly and not when just imported.    
if __name__ == "__main__" :
    main()

