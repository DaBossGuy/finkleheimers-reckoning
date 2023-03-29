# The script of the game goes in this file.

define config.menu_include_disabled = True
    
# Declare characters used by this game. The color argument colorizes the
# name of the character.

define f = Character("Finkleheimer")
define l = Character("Lenny")
define mc = Character("[mcname]",
                        who_color="#00bb00")

# The game starts here.

label start:

    scene bg liveWire

    $ credits = 0

    $ cash = 0
    
    $ mcname = renpy.input("What is your name?")
    
    if mcname == "":
        $ mcname="Leo"

    call screen quest_menu
    
    "Your name is [mcname], the year is 2029 and you live in a place called Xenon City. A city that's in the middle of a crisis."
    "It all starts with Jeffery Finkleheimer. The founder and owner of Jank Incorporated."
    "He has slowy been taking over the city piece by piece. Forcing his employees to live in Jank company housing. And only pays them in Jank Credits, his new form of currency."
    "These Jank Credits are only legal tender in JankTown, the place where all his employees live."
    "But where do you fit in all of this? Well you are a Jank Inc. hater. You despise Jeffery and what he has done, but you are struggling with money and local businesses pay under minimum wage."
    "You fight the choice to work for Jank Inc. but it may be the only choice you have......"

    "GAME START"
    
    "You awake in the Live Wire. A bar created and owned by an IPC (Integrated Positronic Chassis) named Lenny."
    
    "This makes the Live Wire the only IPC owned business in Xenon City."
    
    "You look around and see that you were sleeping on a barstool, with your head on the counter."
    
    "You look down at the counter and see a small puddle of liquid, which you assume is drool."
    
    "You contine looking around, still dazed and tired."
    
    "You see Lenny, cleaning a glass, a few people standing around in the bar, and one person using the data terminal."
    
    "And you can't help but see a familiar yet unkown man talking to these people. As if he were tying to sell them something."

    show lenny
    
    l "Yeah,"

    l "He thought if he got you drunk he could scam ya."

    mc "Who?"

    l "Roger, I knew you were drunk but not THAT drunk."

    l "Do you seriously not remember who he is?"

    mc "I can barely remember my own name, what makes you think I could remember his?"

    l "Good point."

    "Lenny walks away from the counter and starts adjusting the bottles on the shelves."

    "Everything around you gets dark and you feel really tired."

    "And before you know it, you're awake again."

    "You look around, and easily know where you are."

    "You look down at the counter and see the puddle has gotten bigger."

    "Lenny turns around, seemily just noticing you have awoken."

    "He grabs and empty glass from under the counter and fills it up at the sink."

    l "Here you go."

    l "I'm assuming you remember who you are now?"

    mc "Yeah, I'm good. Just a little tired."

    "You look down at your watch, which you realize you don't have."

    l "12:32."

    mc "Really? How long was I out for."

    l "Well, you came in at five."

    l "Passed out at 5:50."

    l "Woke up at eight."

    l "Passed out again."

    l "And you know the rest."

    mc "Seven hours?!"

    mc "Did anything notable happen while I was passed out?"

    l "Nope, 'cept Roger was here, doing the usual."

    mc "Well yeah, that's obvious."

    l "I thought you didn't remember who Roger was? {i}looks smug{/i}"

    mc "{i}rolls eyes{/i}"

    "Lenny laughs"

    "You get up from the seat"

    $ tutorialComplete = True

    $ dataTerminalFirstTime = True
    
label liveWire:

    menu:
        "You are in the Live Wire. What do you do?"

        "Leave":
            jump liveWireAlley

        "Sit at the counter":
            jump liveWireCounter

        "Use the data terminal":
            jump liveWireDataTerminal

label liveWireAlley:

    if tutorialComplete == True:
        "You leave the Live Wire. You know for sure Lenny was telling the truth about the time."
        "It was pitch black. The only thing lighting up the area is the signs of businesses in the alley and the distant skyscrapers."
    
    
    $ tutorialComplete = False

    menu: 
        "You are in the alley. What do you do?"

        "Enter the Live Wire":
            jump liveWire

label liveWireCounter:
    
    menu:
        "You walk up to the counter and take a seat. What do you do?"

        "Get up":
            jump liveWire

        "Order a drink":
            menu:
                l "What'd ya like? And please remember, I only take cash."

                "Nevermind":
                    jump liveWireCounter

                "Beer (25 cr)" if credits >=25:
                    $ credits += -25




                "Screwdriver (1000 cr)" if mcname == "Doug" and credits >=25:
                    $ credits += -1000

                        

        "Talk to Lenny":
            f "PLACEHOLDER"
            jump liveWireCounter

label liveWireDataTerminal:

    if dataTerminalFirstTime == True:
        "You walk up to the data terminal."
        "Data terminals are ATM like machines that allow users to access NNet (New Net), as well as accessing their bank account, and a myriad of other features."
        $ dataTerminalFirstTime = False

    menu:
        "You are infront of the data terminal. There is a 16 pin data connector hanging off the front. What do you do?"

        "Walk away":
            jump liveWire
        
        "Connect your PDA":
            menu:
                "You grab the data connector and, after some fiddling, and flipping the connector upside down, insert it in your PDA's data port. What do you do?"

                "Disconnect":
                    jump liveWireDataTerminal
                
                


            
        
        
        



label end:
    
    "This is the end of the current version. Thanks for playing!"
    
    return
# $ earn = renpy.input("Lets show HIM who's boss. How much you want son?", allow="123456789")

    # $ earn = int(earn)