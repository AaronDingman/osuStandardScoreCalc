import os, re

class userConfig:
    def __init__(self):
        self.configFileExistsBool = False
        self.createConfigFileBool = False
        self.userConfigFile = ".\\userConfig.ini"
        self.path = ''
        if os.path.exists(self.userConfigFile):
            print("A Config File has been found, would you like to use this file?")
            print('Enter \'y\' for yes, enter anything else for no.')
            userInput = input('Waiting for a response\n')
            if userInput == 'y' or userInput == 'Y':
                self.configFileExistsBool = True
            else:
                print('Would you like to create a new config file? This can make things easier when run multiple times!')
                print('Enter \'y\' for yes, enter anything else for no.')
                userInput = input('Waiting for a response\n')
                if userInput == 'y' or userInput == 'Y':
                    self.createConfigFileBool = True
        else:
            print('Config File Not found, would you like to create a config file? This can make things easier when run multiple times!')
            print('Enter \'y\' for yes, enter anything else for no.')
            userInput = input('Waiting for a response\n')
            if userInput == 'y' or userInput == 'Y':
                self.createConfigFileBool = True

    def setPath(self, path):
        self.path = path

    def getPath(self):
        return self.path

    def createConfigFile(self):
        # Remove the config file if it exists
        try:
            os.remove(self.userConfigFile)
        except OSError:
            pass
        f = open("userConfig.ini", "w+")
        f.close()

    def appendToConfigFile(self, text):
        f = open("userConfig.ini", "a")
        f.write(text)
        f.close()

    def getPathFromConfigFile(self):
        f = open('userConfig.ini', 'r')
        for line in f:
            matcher = re.search('^path = (.*)', line)
            if matcher:
                return matcher.group(1)
        f.close()