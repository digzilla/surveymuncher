# surveymuncher.py
# this module contains the building blocks required to process survey data into useful geometry and other data
# current version is 0.1
# github.com/digzilla/surveymuncher
# comments welcome!


# ReadCsv reads a .csv file, validates it and outputs the data as a list of tuples, and also a line count and errors
# todo: work out how to best feed in paths - just expects a file in the same folder for now or with forward slashes
class ReadCsv:
    def __init__(self, csvfile):
        # start errorlog with empty list
        self.errorlog = []
        # check if there is a / for splitting
        if csvfile.find('/') != -1:
            # split filename by searching for / and taking what's after it
            self.filename = csvfile.rsplit('/',1)[1]
            # split filepath by splitting with filename
            self.filepath = csvfile.split(self.filename,1)[0]
        else:
            if csvfile = '':
                self.errorlog.append('The input \'csvfile\' is empty')
            else:
                self.errorlog.append('The input \'csvfile\' does not seem to contain a path (no \'/\' found)')
            self.filename = csvfile
            self.filepath = ''
        # start linecounter at 0
        self.linecounter = 0
        # start readtext as an empty list
        self.readtext = []

# testing suite

print('\n')
print('**************************')
print('class ReadCsv - test suite')
print('**************************')
print('\n')

# file with relative path and two slashes
testfile1 = ReadCsv('/test_data/AFOR-survey-combined-v01-edited.csv')
print('testfile1 - file with relative path and two slashes')
print('filepath = '+testfile1.filepath)
print('filename = '+testfile1.filename)
print('errorlog = '+str(testfile1.errorlog))
print('-------------------')

# file with no path and no slashes
testfile2 = ReadCsv('AFOR-survey-combined-v01-edited.csv')
print('testfile2 - file with no path and no slashes')
print('filepath = '+testfile2.filepath)
print('filename = '+testfile2.filename)
print('errorlog = '+str(testfile2.errorlog))
print('-------------------')

# file with no path and one slash
testfile3 = ReadCsv('/AFOR-survey-combined-v01-edited.csv')
print('testfile3 - file with no path and one slash')
print('filepath = '+testfile3.filepath)
print('filename = '+testfile3.filename)
print('errorlog = '+str(testfile3.errorlog))
print('-------------------')

# file with full path and multiple slashes
testfile4 = ReadCsv('S:/Allway/The Vault//Archive - Stage 1 (roughly gathered)/Projects/2016/20161015 - GPS Auditor' +
                    '/surveymuncher/test_data/AFOR-survey-combined-v01-edited.csv')
print('testfile4 - file with full path and multiple slashes')
print('filepath = '+testfile4.filepath)
print('filename = '+testfile4.filename)
print('errorlog = '+str(testfile3.errorlog))
print('-------------------')

print('\n')
print('**************************')
print('tests complete')
print('**************************')
print('\n')