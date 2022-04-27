import subprocess
import pyttsx3
import speech_recognition as sr
import tkinter
import json
import random
import operator
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import pyjokes
import smtplib
import ctypes
import time
import requests, json
import shutil
import win32com.client as wincl


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
	engine.say(audio)
	engine.runAndWait()

def wishMe():
	hour = int(datetime.datetime.now().hour)
	if hour>= 0 and hour<12:
		speak("Good Morning Sir !")

	elif hour>= 12 and hour<18:
		speak("Good Afternoon Sir !")

	else:
		speak("Good Evening Sir !")

	assname =("Jarvis 1 point o")
	speak("I am your Assistant")
	speak(assname)
	

def username():
	speak("What should i call you sir")
	uname = takeCommand()
	speak("Welcome Mister")
	speak(uname)
	columns = shutil.get_terminal_size().columns
	

	print("Welcome Mr.", uname.center(columns))

	
	speak("How can i Help you, Sir")

def takeCommand():
	
	r = sr.Recognizer()
	
	with sr.Microphone() as source:
		
		print("Listening...")
		r.pause_threshold = 1
		audio = r.listen(source)

	try:
		print("Recognizing...")
		query = r.recognize_google(audio, language ='en-in')
		print(f"User said: {query}\n")

	except Exception as e:
		print(e)
		print("Unable to Recognize your voice.")
		return "None"
	
	return query


if __name__ == '__main__':
	clear = lambda: os.system('cls')
	clear()
	wishMe()
	username()
wishMe()
chance = 3
while(chance != 0):
    speak("please authenticate")
    password =(input('Enter the password:'))
    cpass= '12345'
    if password == cpass:
        print("correct")
        speak("i am EDITH. how may i help you?")	

if 'wikipedia' in query:
			speak('Searching Wikipedia...')
			query = query.replace("wikipedia", "")
			results = wikipedia.summary(query, sentences = 3)
			speak("According to Wikipedia")
			print(results)
			speak(results)

elif 'open youtube' in query:
			speak("Here you go to Youtube\n")
			webbrowser.open("youtube.com")

elif 'open google' in query:
			speak("What do you want to search on google, sir?\n")
			webbrowser.open("google.com")

elif 'open stackoverflow' in query:
			speak("Here you go to Stack Over flow.Happy coding")
			webbrowser.open("stackoverflow.com")

elif 'play music' in query or "play song" in query:
			speak("Here you go with music")
		
			music_dir = "C:\\Users\\\\Music"
			songs = os.listdir(music_dir)
			print(songs)
			random = os.startfile(os.path.join(music_dir, songs[1]))

elif 'the time' in query:
			strTime = datetime.datetime.now().strftime("% H:% M:% S")
			speak(f"Sir, the time is {strTime}")


elif 'how are you' in query:
			speak("I am fine, Thank you")
			speak("How are you, Sir")

elif 'fine' in query or "good" in query:
			speak("It's good to know that your fine")

elif "change my name to" in query:
			query = query.replace("change my name to", "")
			assname = query

elif "change name" in query:
			speak("What would you like to call me, Sir ")
			assname = takeCommand()
			speak("Thanks for naming me")

elif "what's your name" in query or "What is your name" in query:
			speak("My friends call me")
			speak(assname)
			print("My friends call me", assname)

elif 'exit' in query:
			speak("Thanks for giving me your time")
			exit()

			
elif 'joke' in query:
			speak(pyjokes.get_joke())
			
elif "calculate" in query:
			
			app_id = "Wolframalpha api id"
			client = wolframalpha.Client(app_id)
			indx = query.lower().split().index('calculate')
			query = query.split()[indx + 1:]
			res = client.query(' '.join(query))
			answer = next(res.results).text
			print("The answer is " + answer)
			speak("The answer is " + answer)

elif 'search' in query or 'play' in query:
			
			query = query.replace("search", "")
			query = query.replace("play", "")		
			webbrowser.open(query)

elif "who i am" in query:
			speak("If you talk then definitely your human.")

elif "why you came to world" in query:
			speak("Thanks  further It's a secret")

elif 'power point presentation' in query:
			speak("opening Power Point presentation")
			power = ""
			os.startfile(power)


elif "who are you" in query:
			speak("I am your virtual assistant")

		
elif 'lock window' in query:
				speak("locking the device")
				ctypes.windll.user32.LockWorkStation()

elif 'shutdown system' in query:
				speak("Hold On a Sec ! Your system is on its way to shut down")
				subprocess.call('shutdown / p /f')
				
elif 'empty recycle bin' in query:
			winshell.recycle_bin().empty(confirm = False, show_progress = False, sound = True)
			speak("Recycle Bin Recycled")

elif "don't listen" in query or "stop listening" in query:
			speak("for how much time you want to stop jarvis from listening commands")
			a = int(takeCommand())
			time.sleep(a)
			print(a)

elif "camera" in query or "take a photo" in query:
			ec.capture(0, "Jarvis Camera ", "img.jpg")

elif "restart" in query:
			subprocess.call(["shutdown", "/r"])
			
elif "hibernate" in query or "sleep" in query:
			speak("Hibernating")
			subprocess.call("shutdown / h")

elif "log off" in query or "sign out" in query:
			speak("Make sure all the application are closed before sign-out")
			time.sleep(5)
			subprocess.call(["shutdown", "/l"])

elif "write a note" in query:
			speak("What should i write, sir")
			note = takeCommand()
			file = open('jatxt', 'w')
			speak("Sir, Should i include date and time")
			snfm = takeCommand()
			if 'yes' in snfm or 'sure' in snfm:
				strTime = datetime.datetime.now().strftime("% H:% M:% S")
				file.write(strTime)
				file.write(" :- ")
				file.write(note)
			else:
				file.write(note)
		
elif "show note" in query:
			speak("Showing Notes")
			file = open("jarvis.txt", "r")
			print(file.read())
			speak(file.read(6))

elif "weather" in query:
			r
			api_key = ""
			base_url = "http://api.openweathermap.org / data / 2.5 / weather?"
			speak(" City name ")
			print("City name : ")
			city_name = takeCommand()
			complete_url = base_url + "appid =" + api_key + "&q =" + city_name
			response = requests.get(complete_url)
			x = response.json()
			
			if x["cod"] != "404":
				y = x["main"]
				current_temperature = y["temp"]
				current_pressure = y["pressure"]
				current_humidiy = y["humidity"]
				z = x["weather"]
				weather_description = z[0]["description"]
				print(" Temperature (in kelvin unit) = " +str(current_temperature)+"\n atmospheric pressure (in hPa unit) ="+str(current_pressure) +"\n humidity (in percentage) = " +str(current_humidiy) +"\n description = " +str(weather_description))
			
			else:
				speak(" City Not Found ")

elif "wikipedia" in query:
	 webbrowser.open("wikipedia.com")
elif "Good Morning" in query:
			speak("A warm" +query)
			speak("How are you Mister")
			speak(assname)



elif "how are you" in query:
			speak("I'm fine, glad you me that")


elif "what is" in query or "who is" in query:
			

			client = wolframalpha.Client("")
			res = client.query(query)
			
			try:
				print (next(res.results).text)
				speak (next(res.results).text)
			except StopIteration:
				print ("No results")


       