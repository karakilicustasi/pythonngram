# -*- coding: utf-8 -*-
import unicodedata
from os import listdir
from os.path import isfile, join
from io import open
import re
import string
from collections import Counter

def get_file_names():
	mypath = "books"
	onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
	return onlyfiles
	
def open_file(file_name):
	result_string = ""
	with open("books/"+file_name, 'rt',encoding = "ISO-8859-9") as file:
  		data = file.read().replace('\n', '')
	
	return data

def combine_files():
	content = ""
	file_name_list = get_file_names()	
	
	for file_name in file_name_list:
		content = content + open_file(file_name)
	
	return content

def process_combined_text(text):##https://www.techcoil.com/blog/how-to-generate-n-grams-in-python-without-using-any-external-libraries/
	text = text.lower()
	text = text.replace(',', ' ')
	text = text.replace('/', ' ')
	text = text.replace('(', ' ')
	text = text.replace(')', ' ')
	text = text.replace('.', ' ')
	text = text.replace('"', ' ')
	text = text.replace('!', ' ')
	text = text.replace('?', ' ')
	text = text.replace(';', ' ')
	return text.split()

def generate_ngrams(words_list, n):
	ngrams_list = [] 
	for num in range(0, len(words_list)):
		ngram = ' '.join(words_list[num:num + n])
		ngrams_list.append(ngram)
	return ngrams_list

def count_frequencies(words_list):
	count = 1
	frequencies = {}
	for word in words_list:
		if word in frequencies:
			frequencies[word] +=1
		else:
			frequencies[word] = 1
	sorted_frequencies = sorted(frequencies.items(), key=lambda x: x[1], reverse=True)
	for item in sorted_frequencies:
		if count <= 100:
			print("%d -> %s : %d" %(count,item[0],item[1]))
			count += 1
		else:
			break

def print_first_entries(words_list):
	dict(sorted(words_list.items(), key=lambda item: item[1]))
	print(words_list)
	
def menu():
	
	
	
	content = combine_files()
	words_list = process_combined_text(content)
	choice = ''
	while choice != "e":
		print(" 1 - 1gram \n 2 - 2gram \n 3 - 3gram \n 4 - exit")
		choice = input(' -> ')
		if choice !=1 and choice !=2 and choice !=3 and choice != 4:
			print("Wrong Input")
		elif choice != 4:
			count_frequencies(generate_ngrams(words_list,choice))
		if choice == 4:
			print("exit")
			break;
	

#content = combine_files()

#words_list = process_combined_text(content)

#count_frequencies(generate_ngrams(words_list,3))
menu()


