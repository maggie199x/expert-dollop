#!python3
import sys, traceback

def tester():
	print("tester successful")

def player(command):
	pass

reactionMap = {}
reactionMap["player"] = tester
reactionMap["first_room"] = tester
reactionMap["second_room"] = tester


class GameObject(object):
	def __init__(self, tag, lDesc, sDesc, inv):
		self._tag = tag
		self._lDesc = lDesc
		self._sDesc = sDesc
		self._inv = inv

	
	def give_item(self, tag):
		self._inv.append(tag)

	def take_item(self, tag):
		self._inv.remove(tag)
	
	#react = None
	_tag = None
	_sDesc = None
	_lDesc = None
	_inv = []
	_alias = []
