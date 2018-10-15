import userConfig, userData, songData

def main():
    # Creating Config File
    configs = userConfig.userConfig()
    userDataObj = userData.userData()
    # Checking configs, creating if needed.
    if configs.configFileExistsBool is True:
        configs.setPath(configs.getPathFromConfigFile())
        songsDirectoryPath = configs.getPath()
    else:
        songsDirectoryPath = userDataObj.getSongDirectory()
    if configs.createConfigFileBool is True:
        configs.createConfigFile()
        configs.appendToConfigFile('path = ' + songsDirectoryPath)
        configs.setPath(songsDirectoryPath)

    files = userDataObj.getDirectoryListing(configs.getPath())
    while len(files) is not 1:
        files = userDataObj.getDirectoryListing(configs.getPath(), files)
        if len(files) is 1:
            chosenSongPath = files[0]
        elif len(files) is 0:
            print("Could not find a song with that string, please try again.")
        elif files[0] == 'RESTARTPROG':
            files = userDataObj.getDirectoryListing(configs.getPath(), files)

    songDataObj = songData.songData()
    songDataObj.setSongDifficulty(songsDirectoryPath, chosenSongPath)
    songDataObj.parseSongFile(configs.getPath(), files, songDataObj.getSongDifficulty())
    songDataObj.setFinalScore()
    print('Final score for ' + songDataObj.getSongTitle() + ' is: ' + '{:,}'.format(songDataObj.getFinalScore()))

main()