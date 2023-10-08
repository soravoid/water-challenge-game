# The script of the game goes in this file.

# The game starts here.

label start:

    scene watercycle

    "Everything starts with water. But how do we use water, and how does it move around from place to place?"

    scene evap

    "Beginning with evaporation, the sun heats up bodies of water and turns them into little water droplets that stay in the air and rise into the sky."

    scene condense

    "The temperature in the sky is cooler than on Earth, so the water droplets condense into clouds that we can see in the sky."

    scene precip

    "When the clouds get too heavy, the water is released through rain or snow which is also known as precipitations."

    scene watercycle

    "The water then goes back to the bodies of water and the cycle begins again."

    "This cycle has gone on for millions of years on Earth. It is essential for maintaining the planet's environment, ensuring that all forms of life have access to fresh water, and regulating our climate."

    scene watercross

    "While water is essential for our hydration, it is also essential to our food, our power, and our health. Water is what makes life possible, yet it does so differently in different communities."

    "Let take a look at how water can affect those living in India!"

    call india_main

    # TODO change this transition
    # TODO NEED SCENE HERE?
    "Let's look at Uruguay"

    call uruguay_main

    # TODO change this transition
    # TODO NEED SCENE HERE?
    "Let's look at the Aboriginals, an indigenous community in Australia"

    call aboriginal_main
    
    # TODO Implement ending of the game
    scene
    "Ending placeholder"

    # This ends the game.

    return
