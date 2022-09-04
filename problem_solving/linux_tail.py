'''
tail functionality in linux

Return last 3 lines of a log file
'''
def tail(logFilePath: str, lineCount: int):
    lineLength = 20
    with open(logFilePath, 'r') as logFile:
        seekPosition = lineCount * lineLength
        logFile.seek(seekPosition, 2)

        lines = logFile.readlines()
        if len(lines) > lineCount:
            # repeat logic to arrive at optimal starting point
            pass

        for i in range(lineCount):
            line = logFile.readline()
            print(line)

