#!/usr/bin/env python2.7
# -*- coding: utf-8

import codecs
import re
import random

def shuffleStr(s):
	l = list(s)
	random.shuffle(l)
	return ''.join(l)

def main():

	words = set()

	with codecs.open('original.txt', 'r', 'utf-8') as f:
		text = f.read()
		text = text.lower()
		regex = re.compile(ur'[^a-zA-Zа-яА-Я0-9ё]', re.UNICODE)
		text = regex.sub(' ', text)

	newText = []
	for w in text.split():
		words.add(w)
		newText.append(shuffleStr(w))

	with codecs.open('shuffled.txt', 'w', 'utf-8') as f:
		f.write(''.join(newText))

	with codecs.open('dict.txt', 'w', 'utf-8') as f:
		f.write('\n'.join(words))

if __name__ == '__main__':
	main()
