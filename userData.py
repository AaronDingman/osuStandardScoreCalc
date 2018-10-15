import os, re

# Empty dicts as parameters are dangerous, using None instead.
class userData:
    def __init__(self):
        self.path = ''
        self.osLoginName = os.getlogin()

    def getDirectoryListing(self, path, files=None):
        if files is None or len(files) is 0:
            return os.listdir(path)
        else:
            filesToReturn = []
            if len(files) >= 10:
                for i in range(0, 10):
                    print(files[i])
            else:
                for name in files:
                    print(name)
            print('... More than 1 file found, please narrow search.')
            print('\nEnter a song name or part of the name that you would like to find')
            songString = input('Waiting for a response\n')
            songStringPattern = '^.*' + songString + '.*$'
            for name in files:
                if re.match(songStringPattern, name):
                    filesToReturn.append(name)
            if len(filesToReturn) is 0:
                print('There were no songs found with this string, if you would like to try again with the same list enter \'y\'')
                print('If you would like to start over with all songs enter anything else for no.')
                userInput = input('Waiting for a response\n')
                if userInput == 'y' or userInput == 'Y':
                    return list
                else:
                    # TODO Figure out better way to handle this?
                    filesToReturn[0] = 'RESTARTPROG'
                    return filesToReturn
            return filesToReturn

    def getSongDirectory(self):
        # Only exit when returned, no reason to leave without good user input
        while True:
            # https://stackoverflow.com/questions/1325581/how-do-i-check-if-im-running-on-windows-in-python
            if os.name == 'nt':
                print('Is your osu! songs directory the default installation directory? eg. C:\\Users\\' + self.osLoginName + '\\AppData\\Local\\osu!\\Songs\\')
                print('Enter \'y\' for yes, enter anything else for no.')
                userInput = input('Waiting for a response\n')
                if userInput == 'y' or userInput == 'Y':
                    path = 'C:\\Users\\' + self.osLoginName + '\\AppData\\Local\\osu!\\Songs\\'
                else:
                    print('Please enter your osu! song directory path. eg C:\\Users\\' + self.osLoginName + '\\AppData\\Local\\osu!\\Songs\\')
                    path = input('Waiting for a response\n')
            else:
                print("Could not recognize a Windows Operating System, please provide the path to your osu! songs directory.")
                path = input('Waiting for a response\n')
            if os.path.exists(path):
                return path
            else:
                print('ERROR: Could not resolve the osu! installation path.')
                print('Please check your path and try again.\n\n')
