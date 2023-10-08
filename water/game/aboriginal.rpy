# Placeholder first line
image a = Image("Aboriginal drought 2002")
image b = Image("Aboriginal drought 2003")
define j = Character("Jonathan", image="jonathan")
define a = Character("Miss Anderson", image="ms_anderson")
define one = Character("Volunteer 1", image="volunteer")
define two = Character ("Volunteer 2", image="volunteer")
define m = Character ("Mayor", image="mayor")

label aboriginal_main:
  scene aboriginal school bus  
  "Jonathan is a highschool student from Sydney, Australia who has come to Walgett to help with an elementary school's renovations"
  "After they arrive at the school, Jonathan and the other volunteers notice that the classroom is mostly empty...""

  scene aboriginal school outside
  j normal "The classroom looks a little bit empty today, doesn't it?"

  one normal "It really does... today is a weekday, so the kids should be here"

  j normal "Hmm that's odd, I'll go ask the classroom teacher to see if anything is going on"

  j normal "Miss Anderson, I noticed that there aren't very many kids in the classroom today. Is there something going on?"

  show a
  show b

  hide a 
  hide b

  a normal "Yes Jonathan, Walgett has been having some water issues lately. After experiencing droughts, we've had to drill into the ground to get our water instead of using the river. Here are some satellite images of the drought from NASA."

  a normal"This underground bore water is less sanitary and some of our kids have gotten sick from drinking it."

  j normal "That’s awful! We can’t just renovate a school without addressing such a crucial issue! How can we help with this?"

  one normal "One idea is to raise awareness with the local organizations and authorities to see if there is anything we could do to help"

  two normal "What if we changed our original renovation plans to renovate the school in a way that increases water efficiency"

  a normal "Those sound like great ideas!"

  menu: 
	"Speak to local leaders about the issue":
		jump left_path
	"Help renovate the school to make it more water efficient":
		jump right_path


  
label left_path:
  scene aboriginal town hall

  j normal "Hello Mayor! We are at town hall today to see if there is anything we can do to combat Walgett's ongoing water crisis."

  m normal "Hello Jonathan! We are currently trying to bring more awareness about our water issue to more people. Would you like to help?"

  j normal "We would love to! I can start reaching out to the locals and even people in Sydney to let them know about what's going on!"


label right_path:
	scene aboriginal school outside
	j normal "Miss Anderson, what are some renovations we can help with at the school to make it more water efficient?"

	a normal "Some things that we can start working on include: landscaping at the school that are resistant to droughts, sensor-activated faucets, and so much more!"
	
	j normal "Awesome! My classmates and I are more than ready to get started!"


