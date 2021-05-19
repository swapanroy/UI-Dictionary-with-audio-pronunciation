import json
import requests
from tkinter import *
from playsound import playsound

# Constants 
app_id  = "XXXXXXX"
app_key  = "ABCD"
endpoint = "entries"
headers = {'app_id': app_id, 'app_key': app_key}
language_code = "en" # Specify the language code




# Create an empty Tkinter window
window = Tk()
window.title("Dictionary Widget using Oxford Dictionary")
window.geometry("500x140")

# Addimg my custom logo :) 
img=PhotoImage(file='C:\Swapan\Research\PlaywithPython\Tinker Section\SwapanRoy-logo.gif')
img = img.zoom(3, 3) 
window.iconphoto(True, img)


# define dictonary function 

def from_dictionary(lookupWord):
    getword = lookupWord
    #  Get the word
    url = "https://od-api.oxforddictionaries.com/api/v2/entries/" + language_code + "/" + getword.lower()
    r_status= requests.get(url, headers=headers)
    print(url)

    # Additional varibles for readability
    r_mean = r_status
    r_audio = r_mean

    if r_status:
        
        mean_json = r_mean.json()
        mean_list = []

        # Logic to pull relavant data
        for result in mean_json['results'][0]['lexicalEntries'][0]['entries']:
            for sense in result['senses']:
                mean_list.append(sense['definitions'][0])


        for i in mean_list:
            return (i)
    else:
        return("No matches found.. \n Please try again with different word")




# define functional to accept the user input, share a message and clear text 

def beautify_word(beautyword):
    if type(beautyword) == list:
        for i in beautyword:
            return i
        else: 
            return "Word Doesn't Exist, Please double check"

def get_word():
    # Get user value from input box and search for that word in the dictionary 
    word = from_dictionary(e1_value.get()) 
    #word = beautify_word(word)
    

    # Empty the Text boxes if they had text from the previous use and fill them again
    t1.delete("1.0", END)  # Deletes the content of the Text box from start to END
    t1.insert(END,word)  # Fill in the text box with the value of gram variable
   
def get_audio():
    url = "https://od-api.oxforddictionaries.com/api/v2/entries/" + language_code + "/" + e1_value.get()
    print(url)
    r_status = requests.get(url, headers=headers)

    r_mean = r_status
    r_audio = r_mean
    if r_audio:
        audio_json = r_audio.json()
        audio_list = []

        for result in audio_json['results'][0]['lexicalEntries'][0]['entries']:
            for pronunciations in result['pronunciations']:
                audio_list.append(pronunciations)
    else:
        return("No matches found.. \n Please try again with different word")

    #Audio_Output = audio_list[1]['audioFile']
    #print("Audio list",Audio_Output )

    #pip install playsound

    playsound(audio_list[0]['audioFile'])

def delete():
    # Deletes content from t1 Text box
    t1.delete("1.0", END)

    # Deletes content from e2 Entry 
    e1.delete(0, END)

# Add label 

# Create a Label widget with "Word" as label
l0 =Label(window,text="Word")
l0.place(relx = 0.1, rely = 0.17, anchor = 'sw')
#l0.grid(row=0,column=0) # The Label is placed in position 0, 0 in the window

l1 = Label(window,text="Meaning")
l1.place(relx = 0.315, rely = 0.4, anchor = 'sw')
#l1.grid(row=1,column=1) # The Label is placed in position 1, 0 in the window

# Entry point for the users 
e1_value=StringVar()  # Create a special StringVar object
e1 = Entry(window, textvariable = e1_value)  # Create an Entry box for users to enter the value

#e1 = Text(window, height = 3, width = 20, bg = "light yellow")
e1.grid(row=0,column=1) 


# Create a button widget
# The get_word() 
b1 = Button(window,text="Get Meaning",command=get_word)
b1.grid(row=0,column=2)

# The delete function is called when the button is pushed
b2 = Button(window,text="Clear",command=delete)
b2.grid(row=1,column=2)

# The get_audio function is called when the button is pushed
b3 = Button(window,text="Pronunciations",command=get_audio)
b3.grid(row=4,column=1)

# Create four empty text boxes t1

t1 = Text(window,height=2,width=45,font = ("Times New Roman",12) )
t1.grid(row=3,column=1, pady = 5, padx = 10)
t1.config(wrap=WORD)


# Keeps connection window open
window.mainloop()

