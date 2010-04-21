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

""" This module implements an irc bot.
"""

import sys
import socket
import ConfigParser
from IrcBot.responses import static as S
from IrcBot.responses import dynamic as D

class IrcBot:
    """Implements a very easily customizable IRC Bot.
    """
    def __init__(self):
        """This function intializes the Bot configuration.
        """
        self.conf = {}
        self.con = None
        self._read_configuration()
        self.conf['channel'] = '#' + self.conf['channel']
        self.static = S.static()
        self.dynamic = D.dynamic()

    def _read_configuration(self, path='./config/irc-bot.cfg' ):
        """This function reads configuration file and 
        then sets the appropriate dict values.
        @param path - path to the configuration file (default is ./config/irc-bot.conf)
        """
        try:
            config = ConfigParser.ConfigParser()
            config.read(path)
            self.conf = dict( [ kv for kv in config.items ('Connection') ] )
        
        except ConfigParser.ParsingError as err:
            print "Error occured while parsing configuration file\n", err
            sys.exit(0)

    def connect(self):
        """This function opens connection to IRC server and keeps  
        """
        self.con = socket.socket ( socket.AF_INET, socket.SOCK_STREAM )
        try:
            self.con.connect( ( self.conf['network'], 
                int( self.conf['port'] ) ) )
        except socket.error , err:
            print 'Error while opening connection socket\n', err
            sys.exit()
        except TypeError, err:
            print 'Wrong configuration data\n', err
   
    def mainloop(self):
        """starts the mail loop of the bot """
        self.con.send ( 'nick ' + self.conf['nick'] + '\r\n' )
        self.con.send ( 'USER %s %s %s :%s \r\n' %
            (self.conf['nick'],self.conf['nick'],self.conf['nick'],self.conf['name']) )
        self.con.send ( 'JOIN ' + self.conf['channel'] + '\r\n' )
        self.con.send ( 'PRIVMSG ' + self.conf['channel'] + 
            ' :Hello, I am the Bot for this channel. /help for help message.\r\n')
        while True:
            data = self.con.recv ( 4096 )
            self.parser(data)
            print data

    def parser(self, data):
        """Parses input data to look for words to which the bot can respond"""
        context = {}
        context['conn'] = self.con
        context['data'] = data

    def cleanup(self):
        """Perform cleanup operations"""
        self.con.close()


def main():
    """Entry point of the module"""
    bot = IrcBot()
    bot.connect()
    bot.mainloop()
    bot.cleanup()

# Execute only when ran explicitly and not when just imported.    
if __name__ == "__main__" :
    main()

