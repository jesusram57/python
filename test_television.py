import pytest
from television import Television

def test_initial_state():
    tv = Television()
    assert not tv._Television__status
    assert not tv._Television__muted
    assert tv._Television__volume == Television.MIN_VOLUME
    assert tv._Television__channel == Television.MIN_CHANNEL

def test_power():
    tv = Television()
    tv.power()
    assert tv._Television__status
    tv.power()
    assert not tv._Television__status

def test_mute():
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.mute()
    assert tv._Television__muted
    assert tv._Television__volume == Television.MIN_VOLUME
    tv.mute()
    assert not tv._Television__muted
    assert tv._Television__volume == 1 

def test_channel_up():
    tv = Television()
    tv.power()
    tv.channel_up()
    assert tv._Television__channel == 1
    tv.channel_up()
    tv.channel_up()
    tv.channel_up()  
    assert tv._Television__channel == Television.MIN_CHANNEL

def test_channel_down():
    tv = Television()
    tv.power()
    tv.channel_down()
    assert tv._Television__channel == Television.MAX_CHANNEL
    tv.channel_down()
    assert tv._Television__channel == Television.MAX_CHANNEL - 1

def test_volume_up():
    tv = Television()
    tv.power()
    tv.volume_up()
    assert tv._Television__volume == 1
    tv.volume_up()
    tv.volume_up() 
    assert tv._Television__volume == Television.MAX_VOLUME

def test_volume_down():
    tv = Television()
    tv.power()
    tv.volume_up()
    tv.volume_up()
    tv.volume_down()
    assert tv._Television__volume == 1
    tv.volume_down()
    tv.volume_down() 
    assert tv._Television__volume == Television.MIN_VOLUME
