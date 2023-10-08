# Placeholder first line

image ab = Image("aboriginal drought.png")

define j = Character("Jonathan", image="jonathan")
define a = Character("Miss Anderson", image="ms_anderson")
define one = Character("Student 1", image="volunteer")
define two = Character ("Student 2", image="volunteer")
define m = Character ("Mayor", image="mayor")

label aboriginal_main:
  scene aboriginal school bus  
  "Jonathan is a highschool student from Sydney, Australia who has come to Walgett to help with an elementary school's renovations."
  "After they arrive at the school, Jonathan and the other volunteers notice that the classroom is mostly empty..."

  scene aboriginal school outside
  j normal "The classroom looks a little bit empty today, doesn't it?"

  one normal "It really does... today is a weekday, so the kids should be here."

  j normal "Hmm that's odd, I'll go ask the classroom teacher to see if anything is going on."

  j normal "Miss Anderson, I noticed that there aren't very many kids in the classroom today. Is there something going on?"

  a normal "Yes Jonathan, Walgett has been having some water issues lately."

  a "After experiencing droughts, we've had to drill into the ground to get our water instead of using the river."

  a "This  groundwater here is less sanitary and some of our kids have gotten sick from drinking it."

  j normal "That's awful!"

  one normal "It's true! Look at these satellite images from NASA that popped up after a quick search!"

  show ab

  one normal "The left image shows a previous satellite view of Walgett, and the right image is just one year later!"

  hide ab

  j normal "We can’t just renovate a school without addressing such a crucial issue! How can we help with this?"

  one normal "We could raise awareness with the local organizations and authorities to see if there is anything we could do to help."

  two normal "What if we changed our original renovation plans to renovate the school in a way that increases water efficiency?"

  a normal "You all are too kind! Those are amazing ideas!"

  menu:
    j normal "What will we do?"

    "Speak to local leaders about the issue":
      jump left_path
    "Help renovate the school to make it more water efficient":
      jump right_path

  return
  
label left_path:
  scene aboriginal town hall

  j normal "Hello Mayor!"

  j "We heard about the ongoing water crisis happening in Walgett."

  j "Is anything we can do to help the situation?"

  m normal "Jonathan, we are incredibly appreciative of your enthusiasm!"
  m "We're trying to raise awareness about our water issue to more people."
  m "We hope to get word out to big cities like Sydney and Melborne."

  j normal "We would love to help out! Since I go to high school in Sydney, I can start reaching out to the people there to let them know about what's going on!"

  return


label right_path:
  scene aboriginal school outside
  j normal "Miss Anderson, what are some renovations we can help with at the school to make it more water efficient?"

  a normal "We can start by planting native flora that are accustomed to the drought conditions."
 
  j normal "Awesome! My classmates and I are more than ready to get started!"

  return
