# Placeholder first line

define d = Character('Durga', image="dugra")
define k = Character('Kabir', image="kabir")
define l = Character('Lakshmi', image="lakshmi")
define s = Character('Sharma' image ="sharma")

label india_main:
  scene bg market
  "Now how does climate change affect water in India?"
  "70\% of India’s economy depends on the annual monsoons, which means that India depends on natural external causes for multiple facets of life."
  "Here we have Lakshmi, and her friend Durga who will unknowingly find out how much water really has control over their lives."
  l normal"I can’t believe we were able to get out of school two hours early! Typically it feels like we have to stay after."
  d normal "Yeah, but don’t you think our teacher seemed a little weird about it? He seemed a little startled when he told us."
  l normal"I’m sure it’s just temporary, probably something happened with the power breaker. "
  d normal "I just have a bad feeling about this… "

  "Durga kicks a piece of paper as they walk through the town. She picks it up and it reads."
  "Meteorologists predict that the monsoons will come later this year, causing lack of hydroelectricity for the city and irrigation for plants."

  d normal "I told you! This has to be the reason that school let us out early. 
  d normal "Who knows how long we will be out of school if it depends on the monsoon."
  l normal " I doubt it Durga! My parents said those meteorologists are phonies who get paid to say nothing in every word possible. 
  l normal "Let’s just get some kulfi for you to feel better, I bet Kabir will let us get some gajar ka halwa for free again too! "

  scene kulfi stand
  "As the two approach Kabir’s stand, they see him flip the sign to close."
  "Lakshmi looks at her watch and sees that it is only 4 PM. The two look at each other in confusion, but continue heading towards him. "
  l normal "Kabir! Don’t tell me you ran out of Kulfi already! Was business really that good today?"
  k normal "Hello ladies… Unfortunately, I did not run out of kulfi, but rather I must find an alternate way to store my desserts before they spoil.
  k normal "The electricity outage means that if I do not go to the next town fast enough, the kulfi will melt and be wasted."
  d normal "Oh no! How long will that take you?"
  k normal "I don’t know, but it will be expensive to go as quickly as I can."
  "Lakshmi and Dulga look at each other solemnly before Lakshmi perks up with an idea."
  l normal "We can get everyone in town to buy your desserts so you can make the money to go, and no food would have to go to waste!
  l normal "I have 200 rupees with me, I can buy 4 Besan Ladoo now."
  k normal "My prices for every dessert have gone up now, due to how expensive flour is"
  k normal "There is no water to support wheat production, now one bag is four times the price of what it used to be. "
  d normal "Four times!?!"
  k normal "I know, that’s why I must act quickly. "
  k normal " I have no idea whether prices will keep increasing or whether these supplies will run out."
  k normal "If I don’t act now, how will I support my family? "
  d normal "We better let you go then, and we hope things will get better for you Kabir."
  l normal "We can’t imagine what our city would be like without your desserts."
  k normal "Thank you girls"
  "Dulga and Lakshmi leave Kabir as he puts his head in his hands."

  scene bg market 
  "Dulga looks at Lakshmi with a knowing look. "
  d normal "I told you the meteorologist was right."
  d normal "It’s because people don’t believe in science that innocent people like Kabir have to be roped into this."
  l normal "I know and I’m sorry."
  l normal "I want to help him so badly, but I don’t know what we could do as students."
  d normal "Maybe we could raise money for Kabir so he can depend on another energy source."
  d normal "I read an article about solar panels the other day and how they can be a more efficient method of getting energy."

  l normal "Oh yeah! Ms. Sharma was telling us about that in class the other day."
  d normal "We could also start an eco club to inform others and bring awareness to this topic as well"
  d normal "That way we can get others to support us as well! "
  l normal "I love that idea! "
  l normal "We could also go to the local university and see what the environmental professors have to say on the topic as well. "

  menu:
  "What should the girls do?"

  "Start a club to raise awareness"	
	 "Great idea! The girls will go to Ms. Sharma to get some more information prior to starting their club"
	 jump club
  "Raise money for Kabir"
	"Great idea! The girls will go to Ms. Sharma to get some more information prior to raising money for Kabir"
	jump money
  "Go find local environmental experts to get their opintions on it"
	"Great idea! The girls will go to Ms. Sharma to see if she knows anyone and also to get more information."
	jump experts

club
scene school
l "Hi Ms. Sharma, thank you so much for meeting with us"
d "We just have some questions about the environment that we don't really understand yet"

menu:
"How do monsoons work?"
	s "During summer months when the Asian landmass heats up, warm, moist air flows northward from the Indian Ocean towards the Himalayas
	s "This brings abundant showers and thundershowers to India."

"Why is India so dependent on monsoons?"
	s "Monsoon rains provide important reservoirs of water that sustain human activities like agriculture and supports the natural environment through replenishment of aquifers."

"Skip"

l normal "Thank you so much for your insight Ms. Sharma"
d normal "We were just wondering if you would be open to sponsoring our club as well. We want to raise awareness among all students"
s normal "That's a great idea, by getting students involved there will be a greater effort to inform others."
"And so the club began, and Lakshmi and Durga got all their friends and family to support their movement. Their community has now overcome an unexpected force through unity"

money
scene school
l "Hi Ms. Sharma, thank you so much for meeting with us"
d "We just have some questions about the environment that we don't really understand yet"

menu:
"How do monsoons work?"
	s "During summer months when the Asian landmass heats up, warm, moist air flows northward from the Indian Ocean towards the Himalayas
	s "This brings abundant showers and thundershowers to India."

"Why is India so dependent on monsoons?"
	s "Monsoon rains provide important reservoirs of water that sustain human activities like agriculture and supports the natural environment through replenishment of aquifers."

"Skip"

l normal "Thank you so much for your insight Ms. Sharma"
d normal "We were wondering if you knew ways we could fundraise for Kabir as well."
s normal "A great idea would be to recycle resources you already have. 
s normal "I have spare beads, maybe we can all make bracelets to sell around town and give the funds to Kabir"
"And so the three made bracelets and made money for Kabir. Their community has now overcome an unexpected force through unity"

experts
scene school
l "Hi Ms. Sharma, thank you so much for meeting with us"
d "We just have some questions about the environment that we don't really understand yet"

menu:
"How do monsoons work?"
	s "During summer months when the Asian landmass heats up, warm, moist air flows northward from the Indian Ocean towards the Himalayas
	s "This brings abundant showers and thundershowers to India."

"Why is India so dependent on monsoons?"
	s "Monsoon rains provide important reservoirs of water that sustain human activities like agriculture and supports the natural environment through replenishment of aquifers."

"Skip"

l normal "Thank you so much for your insight Ms. Sharma"
d normal "We were just wondering if you would possibly know anyone who is a professional in regards to climate change as well."
s normal "Of course. It is such a great idea to reach out to local professionals to get to know more. I'm sure they are dying to show you their research!"
"And so the girls went on to talk to professionals. By reaching out to members of the commmunity, they have now overcome an unexpected force through unity"