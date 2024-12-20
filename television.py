class Television:
  MIN_VOLUME = 0
  MAX_VOLUME = 2
  MIN_CHANNEL = 0
  MAX_CHANNEL = 3

def __init__(self):
  self.__status = False
  self.__mute = False
  self.__volume = Television.MIN_VOLUME
  self.__channel = self.MIN_CHANNEL
  self.prev = 0

def power(self):
  if self.__status == False:
    self.__status = True
  else:
    self.__status = False 
def mute(self):
  if self.__status == True:
    self.__previous_volume = self.__volume
    self.__volume = self.MIN_VOLUME
    self.__muted = True
def channel_up(self):
  if self.__status == True:
    if self.__channel < self.Max_CHANNEL:
      self.__channel += 1
    else:
      self.__channel = self.MIN_CHANNEL
def channel_down(self):
  if self.__status:
    if self.__channel > Television.MIN_CHANNEL:
      self.__channel -= 1
    else:
      self.__channel = Television.MAX_CHANNEL
def volume_up(self):
  if self.__status:
    self.__muted = False
    if self.__volume < Television.MAX_VOLUME:
      self.__volume += 1
def volume_down(self):
  if self.__status:
    self.__muted = False
    if self.__volume > Television.MIN_VOLUME:
      self.__volume -= 1
def __str__(self):
  if self.__muted:
    return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}'
  else:
    return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
