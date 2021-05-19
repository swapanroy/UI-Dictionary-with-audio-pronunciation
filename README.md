# UI Dictionary with Audio Pronunciation 


**Dictionary** is defined by *Merriam-Webster* as *“a reference book listing alphabetically the words of one language and showing their meanings or translations in another language”*. Using python I’m creating a real-time dictionary with pronunciation. 

*Below is the concept*: 
1.	User API calls to pull the data. (I’m using Oxford Dictionaries - [here](https://developer.oxforddictionaries.com/)) in this example.
2.	Understand the data that has been pulled in – <class type> , list or dict.
3.	Understand the type of data we need and extract it. 
4.	Create a UI screen with buttons like “Get Meaning”, to fetch the meaning of the word, “Pronunciation” , to play sound and “Clear”, to erase the content and make room to request for new


*Dependencies*: 
1.	Using Python 3.9 (Latest version) -download [here](https://www.python.org/downloads/)
2.	Use Tkinter for GUI (pip install tkinter)
3.	Use requests for pull data via API call (pip install requests
4.	Use JSON for parsing, slicing and dicing api data in JSON format ( pip install JSON)
5.	User playsound for playing sound (.mp3 in our case) (pip install playsound)


#Final Output 

![When application loads](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/560abe6ng8h468flbb80.GIF)

Showing the meaning of the word

![With Meaning](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/azj1yrpa55mq57afc25s.GIF)

![Sunny side up](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/8ai3hmt8p45dm8la2bq7.GIF)

Output in Spanish (language_code = "es")

![Spanish](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/y2cpr0m0qqp8wea9w0gy.GIF)
Output in French (language_code = "fr")

![French](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ohnpqw82t2nd8hqfqnl4.GIF)

List of Languages Supported -[here](https://developer.oxforddictionaries.com/documentation/language)

Updated UI 

![Updated UI](https://dev-to-uploads.s3.amazonaws.com/uploads/articles/ipweaglgderl8hwyhbs7.GIF)

	#Code Snippet 
       # Constants 
       appid  = "Your AppID"
       appkey  = "Your Key"
       headers = {'app_id': app_id, 'app_key': app_key}
       language_code = "en-us" # Change language if you want to use 
    a different once

     # Pull data via URL
     url = "https://od- 
     api.oxforddictionaries.com/api/v2/entries/" 
     + language_code + "/" + getword.lower()

    r_status = requests.get(url, headers=headers)
    
    # This checks if the api is live or not <Response [200]>
      print(r_status)

    # Additional varibles for readability
    r_mean = r_status
    r_audio = r_mean

           
Buttons

	# Create a button widget
        # The get_word() 
        b1 = Button(window,text="Get Meaning",command=get_word)
        b1.grid(row=0,column=2)

       # The delete function is called when the button is pushed
       b2 = Button(window,text="Clear",command=delete)
       b2.grid(row=1,column=2)

       # The get_audio function is called when the button is 
       pushed
       b3 =Button(window,text="Pronunciations",command=get_audio)
       b3.grid(row=4,column=1)

      # Create four empty text boxes t1

      t1 = Text(window,height=2,width=45,font = ("Times New Roman",12) )
      t1.grid(row=3,column=1, pady = 5, padx = 2.5)
      t1.config(wrap=WORD)


Functions 
	     
    # Logic to pull meaning of the word 
            def get_word(): 
            #Multiple for loops increases the running time.
             
             for result in mean_json['results'][0]['lexicalEntries'][0]['entries']:
        for sense in result['senses']:
            mean_list.append(sense['definitions'][0])

       for i in mean_list:
            return (i)




     # Logic to pull audio file
        def get_audio():
        for result in audio_json['results'][0]['lexicalEntries'][0]['entries']:
            for pronunciations in result['pronunciations']:
                audio_list.append(pronunciations)














 



