# surveymuncher.py
# this module contains the building blocks required to process survey data into useful geometry and other data
# current version is 0.1
# github.com/digzilla/surveymuncher
# comments welcome!


# ReadCsv reads a .csv file, validates it and outputs the data as a list of tuples, and also a line count and errors
# todo: work out how to best feed in paths - just expects a file in the same folder for now or with forward slashes
class ReadCsv:
    def __init__(self, csvfile):

        # set variables
        self.csvfile = csvfile
        self.filepath = ''
        self.filename = ''
        self.errorlog = []
        self.linecounter = 0
        self.readtext = []

        # validate csvfile and continue if OK
        if self.validate_input() == True:
            if self.validate_file() == True:
                self.linecounter = 1
                self.read_line()
                self.file.close()

    def validate_input(self):
        # check if there is a / for splitting
        # todo - check that these split variables are getting used - if not, remove this section
        if self.csvfile.find('/') != -1:
            # split filename by searching for / and taking what's after it
            self.filename = self.csvfile.rsplit('/', 1)[1]
            # split filepath by splitting with filename
            self.filepath = self.csvfile.split(self.filename, 1)[0]
            return True
        else:
            if self.csvfile == '':
                self.errorlog.append('The input \'csvfile\' is empty')
                return False
            else:
                # todo - is this an important message? could just be a file in the sme folder as this
                self.errorlog.append('The input \'csvfile\' does not seem to contain a path (no \'/\' found)')
                self.filename = self.csvfile
                return True

    def validate_file(self):
        # attempt to open file
        try:
            self.file = open(self.csvfile)
            return True
        except IOError:
            self.errorlog.append('The file \'' + self.csvfile + '\' does not exist')
            return False

    def read_line(self):
        line = self.file.readline()
        while line != '':
            if line.count(',') == -1:
                self.errorlog.append('Line number ' + str(self.linecounter) + ' contains no commas - ignored')
            elif line.count(',') < 4:
                self.errorlog.append('Line number ' + str(self.linecounter) + ' contains fewer than five values')
            elif line.count(',') > 4:
                self.errorlog.append('Line number ' + str(self.linecounter) + ' contains more than five values')
            else:
                splitline = line.split(',')
                if self.is_number(splitline[1]) != True:
                    self.errorlog.append('Line number ' + str(self.linecounter) + ' has an invalid X coordinate')
                else:
                    if self.is_number(splitline[2]) != True:
                        self.errorlog.append('Line number ' + str(self.linecounter) + ' has an invalid Y coordinate')
                    else:
                        if self.is_number(splitline[3]) != True:
                            self.errorlog.append(
                                'Line number ' + str(self.linecounter) + ' has an invalid Z coordinate')
                        else:
                            # remove trailing line breaks
                            splitline[4] = splitline[4].replace('\n', '')
                            self.readtext.append(splitline)
                            self.linecounter += 1
            line = self.file.readline()

    def is_number(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False


# class ReadCsv - test suite
def test_suite_readcsv(us1):
    print('\n')
    print('**************************')
    print('test suite - class ReadCsv')
    print('**************************')
    print('\n')

    if us1 == True:
        print('US1 - Accept the path and name of the `.csv` file and validate that it is actually a path and name')
        print('(also tests aspects of US2, US3 and US11)')
        print('\n')

        # file with relative path and one slash
        testfile1 = ReadCsv('test_data/AFOR-survey-combined-v01-edited.csv')
        print('testfile1 - file with relative path and two slashes')
        print('filepath = ' + testfile1.filepath)
        print('filename = ' + testfile1.filename)
        print('errorlog = ' + str(testfile1.errorlog))
        print('readtext = ' + str(testfile1.readtext))
        print('linecounter = ' + str(testfile1.linecounter))
        print('-------------------')

        # file with no path and no slashes
        testfile2 = ReadCsv('AFOR-survey-combined-v01-edited.csv')
        print('testfile2 - file with no path and no slashes')
        print('filepath = ' + testfile2.filepath)
        print('filename = ' + testfile2.filename)
        print('errorlog = ' + str(testfile2.errorlog))
        print('readtext = ' + str(testfile2.readtext))
        print('linecounter = ' + str(testfile2.linecounter))
        print('-------------------')

        # file with no path and one slash
        testfile3 = ReadCsv('/AFOR-survey-combined-v01-edited.csv')
        print('testfile3 - file with no path and one slash')
        print('filepath = ' + testfile3.filepath)
        print('filename = ' + testfile3.filename)
        print('errorlog = ' + str(testfile3.errorlog))
        print('readtext = ' + str(testfile3.readtext))
        print('linecounter = ' + str(testfile3.linecounter))
        print('-------------------')

        # file with full path and multiple slashes
        testfile4 = ReadCsv(
            'S:/Allway/The Vault/Archive - Stage 1 (roughly gathered)/Projects/2016/20161015 - GPS Auditor' +
            '/surveymuncher/test_data/AFOR-survey-combined-v01-edited.csv')
        print('testfile4 - file with full path and multiple slashes')
        print('filepath = ' + testfile4.filepath)
        print('filename = ' + testfile4.filename)
        print('errorlog = ' + str(testfile4.errorlog))
        print('readtext = ' + str(testfile4.readtext))
        print('linecounter = ' + str(testfile4.linecounter))
        print('-------------------')

        # empty input
        testfile5 = ReadCsv('')
        print('testfile5 - empty input')
        print('filepath = ' + testfile5.filepath)
        print('filename = ' + testfile5.filename)
        print('errorlog = ' + str(testfile5.errorlog))
        print('readtext = ' + str(testfile5.readtext))
        print('linecounter = ' + str(testfile5.linecounter))
        print('-------------------')

        print('\n')
        print('**************************')
        print('tests complete')
        print('**************************')
        print('\n')


test_suite_readcsv(True)
