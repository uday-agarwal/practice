""" Log parser module.

This module provides a log parsing utility.
"""

import os
from datetime import datetime
from typing import Mapping

LOG_DIRECTORY_NAME = 'logs'
LOG_FILE_NAME = 'logfile.txt'
LOG_FULL_PATH = './' + LOG_DIRECTORY_NAME + '/' + LOG_FILE_NAME
OUTPUT_DIRECTORY_NAME = 'query_results'
OUTPUT_FULL_PATH = './' + LOG_DIRECTORY_NAME + '/' + OUTPUT_DIRECTORY_NAME

class LogParser:
    """
    Log parser class to read an input log file, query for a string and count
    the number of occcurrences of the string, also print the matching lines
    into an output file.
    """
    def __init__(self):
        """ Constructor.

        Creates output directory if needed.
        """
        self.__input_file = None
        self.__output_file = None

        # Create output directory as needed
        cwd = os.getcwd()
        os.chdir(LOG_DIRECTORY_NAME)
        if not os.path.exists(OUTPUT_DIRECTORY_NAME):
            os.mkdir(OUTPUT_DIRECTORY_NAME)
        os.chdir(cwd)

    def open_input_logfile(self):
        """ Open the input log file.

        Finds the latest available log file and opens it.
        If no file is found, no action is taken.

        Args:
            None

        Returns:
            None

        Raises:
            None
        """

        try:
            self.__input_file = open(LOG_FULL_PATH, 'r')
        except FileNotFoundError:
            pass

    def print_output(self, line: str):
        """ Blah.

        """
        # Create a new output file if it doesn't exist already
        if not self.__output_file:
            file_name = OUTPUT_FULL_PATH + '/output_' + \
                        datetime.now().strftime('%Y-%m-%dT%H-%M-%S') + '.txt'
            self.__output_file = open(file_name, 'x')
        self.__output_file.write(line)

    def cleanup(self):
        """ Cleanup.

        """
        if self.__input_file:
            self.__input_file.close()
        if self.__output_file:
            self.__output_file.close()

    def search(self, query_text: str) -> Mapping[int, int]:
        """ Search for ...

        Args:
            self: Class instance
            query_text: The text to search for

        Returns:
            A dict mapping blah blah.
            For example: blah blah.

        """
        self.open_input_logfile()
        if not self.__input_file:
            raise FileNotFoundError('Could not find a log file to parse')

        count = {}
        for line in self.__input_file:
            timestamp = line[0:19]
            if query_text in line[20:]:
                hour = timestamp[11:13]
                if hour in count:
                    count[hour] += 1
                else:
                    count[hour] = 1
                self.print_output(line)
        self.cleanup()
        return count

if __name__ == '__main__':
    os.chdir('./LLD/log_parser')
    log_parser = LogParser()
    log_count = log_parser.search('timeout failure')
    print('Found # of lines:', log_count)
