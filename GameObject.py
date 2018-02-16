#!python3
import sys, traceback

def tester():
	print("tester successful")
	return

def player(command):
	return

reactionMap = {}
reactionMap["player"] = tester
reactionMap["first_room"] = tester
reactionMap["second_room"] = tester


class GameObject(object):
	def __init__(self, tag, lDesc, sDesc):
		self._tag = tag
		self._lDesc = lDesc
		self._sDesc = sDesc
		return

	@property
	def tag():
	    doc = "The tag property."
	    def fget(self):
	        return self._tag
	    def fset(self, value):
	        self._tag = valuse
	    def fdel(self):
	        del self._tag
	    return locals()

	def give_item(self, tag):
		return

	def take_item(self, tag):
		return
	
	#react = None
	_tag = None
	_sDesc = None
	_lDesc = None
	_inv = {}
	_alias = []
