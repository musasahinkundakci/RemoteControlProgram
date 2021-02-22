import time as t
import random as r
import os
class remoteControl():
  
  def __init__(self,openor_not="Open",volumeof_voice=0,channel_list=["Trt","Star","Tv-8","Beyaz-Tv","Trt Spor","BBC"],current_channel="Trt",favourite_channels=[]):
    self.openor_not=openor_not
    self.volume=volumeof_voice
    self.channel_list=channel_list
    self.current_channel=current_channel
    self.favourite_channels=favourite_channels
    print("Creating a remote control is processing...")
    for i in range(1,4):
      print("{} saniye".format(i))
      t.sleep(1)
    print("Remote Cotrol is occured...")
  def addFavoriteChannel(self):
    print("Your channels are {}".format(self.channel_list))
    a=input("Which one do you wanna add: ")
    print("Adding channell is processing...")
    t.sleep(1)
    self.favourite_channels.append(a)
    print("Channel is added...")
  def deleteChannel(self):
    print("Your channels are {}".format(self.channel_list))
    a=input("Which one do you wanna delete: ")
    t.sleep(1)
    print("Deleting channel is processing...")
    self.channel_list.remove(a)
    print("The channel is deleted...")
  def deleteFavoriteChannel(self):
    print("Your favourite channels are {}".format(self.favourite_channels))
    a=input("Which one do you wanna delete: ")
    t.sleep(1)
    print("Deleting favourite channel is processing...")
    self.favourite_channels.remove(a)
    print("The favourite channel is deleted...")      
  def volume_upordown(self):
    while(True):
      up_or_down=input("Eksiltmek için '<',Arttırmak için '>' a basınız\nÇıkmak için 'q' ya basınız...")
      if(up_or_down=="<"):
        self.volume+=1
        print("The new volume is {}.".format(self.volume))
      elif(up_or_down==">"):
        self.volume-=1
        print("The new volume is {}.".format(self.volume))
      elif(up_or_down=="q"):
        print("Programdan çıkılıyor...")
        t.sleep(1)
        break
  def power_button(self):
    if(self.openor_not=="Open"):
      self.openor_not="Off"
      print("Tv is shut_down...")
    elif(self.openor_not=="Off"):
      print("Tv is opened...")
      self.openor_not="Open"
  def __str__(self):
    return "Tv situation={}\nVolume Level={}\nChannel List={}\nCurren Channel={}".format(self.openor_not,self.volume,self.channel_list,self.current_channel)
  def __len__(self):
    return "{} channels exist...".format(len(self.channel_list))
  def random_channel(self):
    a=r.randint(0,len(self.channel_list)-1)
    self.current_channel=self.channel_list[a]
    print("The new channel is {}".format(self.current_channel))
  def add_channel(self,channel_name):
    print("Adding channel is processing...")
    self.channel_list.append(channel_name)
    t.sleep(1)
    print("{} channel is added...".format(channel_name))
  def seefavouritechannels(self):
    return "{}".format(self.favourite_channels)
  
remote=remoteControl()
while(True):
  print("""
  ***********************
  Remote control program:
  1.Power Button

  2.Tv's situation

  3.Find out how many channel exists

  4.Add new channel

  5.Pick random channel

  6.Volume up or down

  7.Add favourite channel

  8.Delete favourite channel

  9.Delete channel
  
  10.See favourite channels

  11.Break
  """)
  operation=int(input("Pick a command like '1' or '5'"))
  if(operation==1):
    remote.power_button()
  elif(operation==2):
    print(remote.__str__())
  elif(operation==3):
    print(remote.__len__())
  elif(operation==4):
    channel=input("The channel you wanna ad is ")
    remote.add_channel(channel)
  elif(operation==5):
    remote.random_channel()
  elif(operation==6):
    remote.volume_upordown()
  elif(operation==7):
    remote.addFavoriteChannel()
  elif(operation==8):
    remote.deleteFavoriteChannel()
  elif(operation==9):
    remote.deleteChannel()
  elif(operation==10):
    print(remote.seefavouritechannels())
  elif(operation==11):
    print("Program is shutting down...")
    break
  c=input("Do you wanna clear the screen(y/N):")
  if(c.lower()=="y"):
    t.sleep(3)
    os.system("clear")
  



    
