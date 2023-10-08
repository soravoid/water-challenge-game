# Placeholder first line

image paso_severino = Image("paso severino satellite.png")

image enso:
  "enso/frame_01.jpg"
  pause 0.2
  "enso/frame_02.jpg"
  pause 0.2
  "enso/frame_03.jpg"
  pause 0.2
  "enso/frame_04.jpg"
  pause 0.2
  "enso/frame_05.jpg"
  pause 0.2
  "enso/frame_06.jpg"
  pause 0.2
  "enso/frame_07.jpg"
  pause 0.2
  "enso/frame_08.jpg"
  pause 0.2
  "enso/frame_09.jpg"
  pause 0.2
  "enso/frame_10.jpg"
  pause 0.2
  "enso/frame_11.jpg"
  pause 0.2
  "enso/frame_12.jpg"
  pause 0.2
  "enso/frame_13.jpg"
  pause 0.2
  "enso/frame_14.jpg"
  pause 0.2
  "enso/frame_15.jpg"
  pause 0.2
  "enso/frame_16.jpg"
  pause 0.2
  "enso/frame_17.jpg"
  pause 0.2
  "enso/frame_18.jpg"
  pause 0.2
  "enso/frame_19.jpg"
  repeat

define sil = Character("Silvia", image="silvia")
define sam = Character("Samuel", image="samuel")
define hec = Character("Héctor", image="hector")
define rad = Character("Radio")
define exp = Character("Expert")
define co1 = Character("Coworker 1")
define co2 = Character("Coworker 2")

label uruguay_main:
  scene uruguay house outside  

  "Silvia is a journalist for a local news station in Uruguay, a country in South America. She lives with her husband, Héctor, and her 6-year-old son, Samuel."

  scene uruguay house kitchen

  # TODO Show Héctor is sitting at the dinner table reading a newspaper. Silvia begins preparing coffee

  "Silvia usually starts her day with a cup of coffee, but something was off today." 

  sil normal "Héctor, my coffee is way too salty! Did we change the beans or something recently?"

  hec normal "No my dear, I haven’t touched anything"

  # TODO Silvia pours her coffee down the drain with a frown on her face. Her son, samuel, enters the room with a frown on his face.

  sam normal "{size=+40} BLEH!!!" with vpunch

  sam "The water tasted terrible today!"

  sam "Brushing my teeth was like drinking pool water!"

  sil normal "Don't overexaggerate, honey."
  sil "Come on now, you’re going to make both of us late this morning."
  sil "Bye, sweetie!"

  # TODO Silvia drives off with samuel while Héctor waves them goodbye. Silvia turns on the radio to fill the silence.
  scene car driving 1
  
  rad "…three years of drought have plagued Uruguay."
  rad "Experts worry that the country may soon face a water crisis if the current situation continues as is."

  sil normal "A water crisis? That sounds serious."

  sam normal "Mommy? What's a water crisis?"

  sil normal "It's when there isn't enough water to go around."

  sam normal "Like running out of juice?"

  sil normal "Kind of. But water is even more important than juice."
  sil "We need it to drink, to cook, to bathe, to clean. Everything!"

  scene car driving 2

  sam normal "But we have lots of water in the ocean. Why can't we just drink that?"

  sil normal "Because ocean water is salty, and it's not safe to drink. You said you didn't like salty water this morning, didn't you?"

  sam normal "Ew...gross."

  sil normal "That's why it's important to conserve water, even when we have plenty of it. We need to make sure that we don't waste it."

  sam normal "I won't waste water, Mommy."

  sil normal "I know you won't, honey."

  scene uruguay school outside

  sil normal "We're here, sweetheart! Have a good day at school!"

  sam normal "Bye, Mommy!"

  scene car driving 1

  # TODO something here?
  
  scene uruguay office

  co1 "Silvia! Thank goodness you're here. We're in the middle of a big story."

  co2 "Yeah, the Paso Severino resevoir reservoir is drying up."
  co2 "The government is about to start adding water from the Plata River to the water supply, but it's salty."

  sil normal "It's already happened! My coffee was way too salty this morning."
  
  co1 "That's why everyone is panicking. People are worried about getting sick from drinking the water."

  sil normal "We need to get this story out there. People need to know what's going on."

  "Silvia and her coworkers start working on a news report about the water crisis."
  "They interview experts and residents to get a better understanding of the situation."
  "Before long, the work day had ended with less work done than she had wanted."

  scene uruguay market

  "Silvia stops by the market to buy bottled water for her family at home, but..."
  "She found that the price had gone up several times!"

  sil normal "I don’t think I can keep buying bottled water for very long."
  sil "I hope that this water crisis can be resolved soon."

  scene uruguay outside school

  "It was time to pick up samuel, but something was terribly wrong…"

  sil normal "He should be here by now. What’s taking him so long?"

  # TODO samuel gets in Silvia’s car, face pale
  
  sil normal "Samuel, sweetie, you don't look well. What happened at school today?"

  sam normal "Mommy, I don't feel so good. My throat hurts, and I'm really thirsty."

  sil normal "It's going to be okay, sweetheart. Let's get you home, and I'll make sure you're better soon."

  scene car driving 1

  scene uruguay house couch

  # TODO Silvia takes samuel home from school. Samuel is laying on the couch with a towel on his head.

  sil normal "Are you feeling any better, honey?"

  sam normal "No, Mommy. My head hurts and my mouth is so dry."
  
  sil normal "I'm going to get you some water."
  
  sam normal "{size=+10}No!"

  sam normal "I don't want to drink any water. It tastes funny."

  sil normal "No, honey, this is bottled water. It's safe to drink."

  sam normal "Okay, Mommy..."

  # TODO Silvia goes to the kitchen to get samuel the bottled water she had bought earlier. Silvia sits down on the couch next to Samuel and puts her arm around him.

  sil normal "We're going to get through this, honey. I promise."

  scene uruguay house outside with fade

  "The next day..."

  scene uruguay house kitchen

  sil normal "Honey, are you going to be okay with samuel?"

  hec normal "Yes, sweetheart, don't worry about me!"

  scene car driving 1

  # TODO? Silvia gets in her car and heads to work.

  scene uruguay office

  "At work that day, Silvia is interviewing an environmental scientist to explore potential solutions to the ongoing water crisis."

  scene uruguay interview

  sil normal "Thank you for agreeing to this interview today."

  exp "The pleasure's mine!"

  sil normal "Let's get started! What do you think caused these past three years of drought?"

  exp "That is a very difficult question, as the climate and weather patterns are very chaotic systems."

  exp "However, several factors can contribute to prolonged droughts. Climate change, which affects weather patterns, has been a significant factor."

  exp "In fact, look at these satellite images of the Paso Severino resevoir!"

  show paso_severino

  exp "The left image is from June 2022 and the right is from June 2023 recorded by the NASA OLI telescope."

  exp "The Paso Severino resevoir has dried up considerably over the past year, which contributes to the current water crisis."

  hide paso_severino

  exp "Being aware and proactive about observing these patterns will allow us to prevent future situations like we are in now."
  
  sil normal "Wow! These pictures are super shocking to me! More attention should be brought to data like this!"

  exp "Presenting scientific data to the public is a difficult task,"

  exp "and with an effective presentation, hopefully more people are inspired to take action."

  call question_menu


  return

label question_menu:
  menu:
    sil "What other questions should I ask the expert??"

    "What are some ways we can make water less salty?":
      jump expert_first_question

    "How can we save more water to reduce our waste?":
      jump expert_second_question

    "What are El Niño and La Niña?":
      jump expert_nino_nina

    "I am done.":
      return

label expert_first_question:

  exp "What an excellent question! This is the first solution many people have researched."

  exp "The method to do so is called \"desalination,\" and there are two main ways to carry out this process."

  exp "The first is to evaporate the water so it leaves all the salt behind. We can collect the water vapor and condense it, giving us not-salty water."

  exp "We can also desalinate the water by using a filter that only lets water molecules through and not salt molecules."

  exp "Both of these methods are incredibly expensive and energy intensive, so we are still looking for more affordable ways to provide clean water."

  jump question_menu

  return

label expert_second_question:

  exp "Household leaks, from pipes, taps, or other areas, tend to be a surprising source of water waste."

  exp "Taking the time to fix these problems can be a great first step!"

  exp "Taking care of your gardens could also be a source of water waste."

  exp "Try watering during the cooler parts of the day to reduce water loss due to evaporation."

  exp "By incorporating these simple changes into our daily lives, we can contribute to water conservation in Uruguay to ensure everyone can have access to clean water."

  jump question_menu

  return

label expert_nino_nina:

  exp "El Niño is a phenomenon that affects weather all over the world! It consists of unusual warming of surface waters in the eastern tropical Pacific Ocean." 

  exp "It is part of a larger phenomenon called the El Niño-Southern Oscillation (ENSO), which also describes La Niña, the cold version of El Niño."

  exp "These phenomena has a significant impact on ocean temperatures, currents, fisheries, and weather patterns around the world"
  
  show enso at top

  exp "In fact, here's a short animation that shows temperature changes due to El Niño and La Niña from NASA!"

  hide enso

  jump question_menu

  return
