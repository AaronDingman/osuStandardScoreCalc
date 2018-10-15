import os

class songData:
    def __init__(self):
        self.difficulty = ''
        # [General]
        # Mode
        # Standard = 3, Taiko = 1, Catch The Beat = 2, Mania = 3
        self.gameMode = -1
        # [Metadata]
        # Title
        self.title = ''
        # [Difficulty]
        # Song File Data #
        # HPDrainRate
        self.hpDrain = 0
        # Mania and Taiko only
        # CircleSize
        self.keys = 0
        # OverallDifficulty
        self.overallDifficulty = 0
        # ApproachRate
        self.ApproachRate = 0
        # SliderMultiplier
        self.SliderMultiplier = 0
        # [HitObjects]
        # Count of lines in this section
        self.notes = 0

        self.finalScore = 0

    def getSongGameMode(self):
        return self.gameMode

    def setSongDifficulty(self, songsPath, chosenSongPath):
        difficulties = []
        fullPath = songsPath + chosenSongPath
        songDirectoryContents = os.listdir(fullPath)
        for fname in songDirectoryContents:
            if fname.endswith(".osu"):
                difficulties.append(fname)
        # Only exit when returned, no reason to leave without good user input
        while True:
            for i in range(0, (len(difficulties) - 1)):
                print(str(i) + ': ' + difficulties[i])
            print('Please enter the number to the left of the song name to select a song difficulty.')
            userInput = input('Waiting for a response\n')
            if userInput.isnumeric():
                if len(difficulties) > int(userInput) and int(userInput) >= 0:
                    self.difficulty = difficulties[int(userInput)-1]
                    break
                else:
                    print('Invalid selection, please try again.')
            else:
                print("You did not enter a number. Please try again.")

    def getSongDifficulty(self):
        return self.difficulty

    def parseSongFile(self, songsPath, chosenSongPath, chosenSongFile):
        countingNotes = False
        fullFilePath = (songsPath + chosenSongPath[0] + '\\' + chosenSongFile)
        with open(fullFilePath) as file:
            line = file.readline().replace(" ", "")
            while line:
                if 'Mode:' in line:
                    self.gameMode = line.split("Mode:", 1)[1].replace('\n', "")
                elif 'Title:' in line:
                    self.title = line.split("Title:", 1)[1].replace('\n', "")
                elif 'HPDrainRate:' in line:
                    self.hpDrain = line.split("HPDrainRate:", 1)[1].replace('\n', "")
                elif 'CircleSize:' in line:
                    self.keys = line.split("CircleSize:", 1)[1].replace('\n', "")
                elif 'OverallDifficulty:' in line:
                    self.overallDifficulty = line.split("OverallDifficulty:", 1)[1].replace('\n', "")
                elif 'ApproachRate:' in line:
                    self.ApproachRate = line.split("ApproachRate:", 1)[1].replace('\n', "")
                elif 'SliderMultiplier:' in line:
                    self.SliderMultiplier = line.split("SliderMultiplier:", 1)[1].replace('\n', "")
                elif '[HitObjects]' in line:
                    countingNotes = True
                elif countingNotes:
                    self.notes += 1
                line = file.readline().replace(" ", "")

    def setFinalScore(self, baseScore=100):
        tempScore = 0
        for i in range(0, self.notes):
            tempScore += baseScore * i
        self.finalScore = tempScore

    def getFinalScore(self):
        return self.finalScore

    def getSongTitle(self):
        return self.title