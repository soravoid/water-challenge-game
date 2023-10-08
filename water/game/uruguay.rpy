# Placeholder first line

define sil = Character("Silvia")
define sam = Character("Sam")
define hec = Character("Héctor")
define rad = Character("Radio")
define exp = Character("Expert")
define co1 = Character("Coworker 1")
define co2 = Character("Coworker 2")

label uruguay_main:
  scene silvia house outside  

  "Silvia is a journalist for a local news station in Uruguay, a country in South America. She lives with her husband, Héctor, and her 6-year-old son, Samuel."

  scene silvia house kitchen

  # TODO Show Héctor is sitting at the dinner table reading a newspaper. Silvia begins preparing coffee

  "Silvia usually starts her day with a cup of coffee, but something was off today." 

  sil "Héctor, my coffee is way too salty! Did we change the beans or something recently?"

  hec "No my dear, I haven’t touched anything"

  # TODO Silvia pours her coffee down the drain with a frown on her face. Her son, Samuel, enters the room with a frown on his face.

  sam "{size=+40} BLEH!!!" with vpunch

  sam "The water tasted terrible today!"

  sam "Brushing my teeth was like drinking pool water!"

  sil "Don't overexaggerate, honey."
  sil "Come on now, you’re going to make both of us late this morning."
  sil "Bye, sweetie!"

  # TODO Silvia drives off with Samuel while Héctor waves them goodbye. Silvia turns on the radio to fill the silence.
  scene silvia car
  
  rad "…three years of drought have plagued Uruguay."
  rad "Experts worry that the country may soon face a water crisis if the current situation continues as is."

  sil "A water crisis? That sounds serious."

  sam "Mommy? What's a water crisis?"

  sil "It's when there isn't enough water to go around."

  sam "Like running out of juice?"

  sil "Kind of. But water is even more important than juice."
  sil "We need it to drink, to cook, to bathe, to clean. Everything!"

  scene silvia car sideways

  sam "But we have lots of water in the ocean. Why can't we just drink that?"

  sil "Because ocean water is salty, and it's not safe to drink. You said you didn't like salty water this morning, didn't you?"

  sam "Ew...gross."

  sil "That's why it's important to conserve water, even when we have plenty of it. We need to make sure that we don't waste it."

  sam "I won't waste water, Mommy."

  sil "I know you won't, honey."

  scene uruguay school outside

  sil "We're here, sweetheart! Have a good day at school!"

  sam "Bye, Mommy!"

  scene silvia car

  # TODO something here?
  
  scene silvia office

  co1 "Silvia! Thank goodness you're here. We're in the middle of a big story."

  co2 "Yeah, the Paso Severino reservoir is drying up."
  co2 "The government is about to start adding water from the Plata River to the water supply, but it's salty."

  sil "It's already happened! My coffee was way too salty this morning."
  
  co1 "That's why everyone is panicking. People are worried about getting sick from drinking the water."

  sil "We need to get this story out there. People need to know what's going on."

  "Silvia and her coworkers start working on a news report about the water crisis."
  "They interview experts and residents to get a better understanding of the situation."
  "Before long, the work day had ended with less work done than she had wanted."

  scene uruguay market

  "Silvia stops by the market to buy bottled water for her family at home, but..."
  "She found that the price had gone up several times!"

  sil "I don’t think I can keep buying bottled water for very long."
  sil "I hope that this water crisis can be resolved soon."

  scene uruguay outside school

  "It was time to pick up Samuel, but something was terribly wrong…"

  sil "He should be here by now. What’s taking him so long?"

  # TODO Samuel gets in Silvia’s car, face pale
  
  sil "Samuel, sweetie, you don't look well. What happened at school today?"

  sam "Mommy, I don't feel so good. My throat hurts, and I'm really thirsty."

  sil "It's going to be okay, sweetheart. Let's get you home, and I'll make sure you're better soon."

  scene silvia car

  scene silvia house couch

  # TODO Silvia takes Samuel home from school. Samuel is laying on the couch with a towel on his head.

  sil "Are you feeling any better, honey?"

  sam "No, Mommy. My head hurts and my mouth is so dry."
  
  sil "I'm going to get you some water."
  
  sam "{size=+10}No!"

  sam "I don't want to drink any water. It tastes funny."

  sil "No, honey, this is bottled water. It's safe to drink."

  sam "Okay, Mommy..."

  # TODO Silvia goes to the kitchen to get Samuel the bottled water she had bought earlier. Silvia sits down on the couch next to Samuel and puts her arm around him.

  sil "We're going to get through this, honey. I promise."

  "The next day..."

  sil "Honey, are you going to be okay with Samuel?"

  hec "Yes, sweetheart, don't worry about me!"

  scene silvia car

  # TODO? Silvia gets in her car and heads to work.

  scene silvia office

  "At work that day, Silvia is interviewing an environmental scientist to explore potential solutions to the ongoing water crisis."

  return
