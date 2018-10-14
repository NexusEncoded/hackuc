import time
import random
import os
import os

print("Welcome to YouMusic!, the MUSIC FOR YOU! (Music as of 10/13/2018")

time.sleep(.5)

class Music:

    def __init__(self, song, songt, songth, sixth, sixthl, sixth65):
        self.song = song
        self.songt = songt
        self.songth = songth
        self.sixth = sixth
        self.sixthl = sixthl
        self.sixth65 = sixth65
    def songnames(self):
        return '{} {}'.format(self.song, self.songt, self.songth, self.sixth, self.sixthl, self.sixth65)
        #return self.song,self.songt,self.songth,self.sixth,self.sixthl.self.sixth65

name = input("Whats your name?\n")

time.sleep(.5)

print ("Hello",name)
time.sleep(.5)
print("We will custommize a playlist from a wide variety of songs which are updated daily.\n They are personalized to a mood or genre.")

playlist = input("How are you feeling today or what generes do you have in mind? (Hype, Sad , Spanish Music, Pop)\n You can just say the genre or mood listed. You will be given two songs to start of with but there are more in the que.")

playlist = playlist.lower()

beastModeRap = {1:"Lil Baby & Drake - Yes Indeed", 2:"Mo Bamba - Sheck Wes", 3:"Lil Wayne - 6 Foot 7 Foot", 4:"Kendrick Lamar - Humble", 5:"Famous Dex - JAPAN", 6:"31 Days - Future"}
breakUpMusic = {1:"Sam Smith - Like I Can:", 2:"Sam Smith - I'm Not The Only One", 3:"REM - Everybody Hurts", 4:"Adele - Hello", 5:"XXXTentacion - SAD", 6:"Juice WRLD - Lucid Dreams"}
popLive = {1:"Sia & LSD - Thunderclouds", 2:"Jon Bellion - All Time Low", 3:"Troye Sivan - YOUTH", 4:"Neil Diamond - Sweet Caroline", 5:"Twenty One Pilots - My Blood"}
beastModeHispanic = {1:"DJ Snake - Taki Taki",2:"Nicky Jam - X-remix", 3:"Daddy Yankee - Dura Remix", 4:"Cardi B - I Like It", 5:"Wolfine - Bella Remix", 6:"Cardi B- Bodak Yellow"}
#dictest = {1:"lol", 2:"pop", 3:"kool", 4:"lalas"}

if playlist == "hype":
    print("We will now randomize songs for your listening from the hype section. ")
    playlista = Music(beastModeRap[1], beastModeRap[2], beastModeRap[3], beastModeRap[4], beastModeRap[5], beastModeRap[6])
    print("You are recommeneded too listen to" , playlista.songnames())
    time.sleep(.5)
    os.startfile('C:\\Music\\LilBaby.mp3')
    

if playlist == "sad":
    print("We will now randomize songs for your listening from the sad section.")
    playlista = Music(breakUpMusic[1], breakUpMusic[2], breakUpMusic[3], breakUpMusic[4], breakUpMusic[5], breakUpMusic[6])
    print("You are recommened to listen to but not limited too", playlista.songnames())
    time.sleep(1)

if playlist == "pop":
    print("We will now randomize songs for your listening from the pop section.")
    playlista = Music(popLive[1], popLive[2], popLive[3], popLive[4], popLive[4], popLive[5])
    print("You are recommened to to listen to but not limited too ", playlista.songnames())

if playlist == "spanish":
    print("We will now randomize songs for your listening from the Spanish section.")
    playlista = Music(beastModeHispanic[1], beastModeHispanic[2], beastModeHispanic[3], beastModeHispanic[4], beastModeHispanic[5], beastModeHispanic[6])
    print("You are recommened to to listen to but not limited too", playlista.songnames())

print("Thank you for using YouMusic!, The personalized playlist maker.")



