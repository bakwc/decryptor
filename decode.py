#!/usr/bin/env python2.7
# -*- coding: utf-8

import codecs

MAX_LEN = 25

def getAllMatchingWords(text, posFrom, swords):
	results = []
	for i in xrange(1, MAX_LEN):
		wordToCheck = ''.join(sorted(text[posFrom:posFrom + i]))
		if wordToCheck in swords:
			results.append(wordToCheck)
	return results

class State(object):
	def __init__(self):
		self.prevWords = []
		self.position = 0

def main():
	with codecs.open('shuffled.txt', 'r', 'utf-8') as f:
		text = f.read()

	with codecs.open('dict.txt', 'r', 'utf-8') as f:
		words = f.read().split()

	swords = set()
	stow = {}
	for w in words:
		sw = ''.join(sorted(w))
		swords.add(sw)
		stow[sw] = w

	states = [State()]

	for i in xrange(0, 5000):
		newStates = []
		maxStatePos = 0
		for state in states:
			results = getAllMatchingWords(text, state.position, swords)
			for result in results:
				newState = State()
				newState.prevWords = state.prevWords + [result]
				newState.position = state.position + len(result)
				maxStatePos = max(maxStatePos, newState.position)
				newStates.append(newState)

		currPositions = set()
		states = []
		#todo: implement context-base resolving
		for state in newStates:
			if state.position < maxStatePos - MAX_LEN:
				continue
			if state.position not in currPositions:
				states.append(state)
				currPositions.add(state.position)

	print ' === total states:', len(states)
	for state in states[:1]:
		print ' '.join([stow[w] for w in state.prevWords])

if __name__ == '__main__':
	main()
