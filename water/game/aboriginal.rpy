# Placeholder first line

define j = Character("Jonathan")
define a = Character("Miss Anderson")
define one = Character("Volunteer 1")
define two = Character ("Volunteer 2")

label aboriginal_main:
  scene aboriginal school outside 
  "Jonathan is a highschool student from Sydney, Australia who has come to Walgett to help with an elementary school's renovations"
  "After they arrive at the school, Jonathan and the other volunteers notice that the classroom is mostly empty"
  "They ask the teacher about where the kids are..."

  show Jonathan
  j "Miss Anderson, why are there so many kids missing from class today?"
  hide Jonathan

  show Miss Anderson
  a "We are dealing with a water crisis and the kids have gotten sick from drinking the water"

  show Jonathan
  j "That’s awful! We can’t just renovate a school without addressing such a crucial issue! How can we help with this?"

  show Volunteer 1
  one"We could raise awareness with the local organizations and authorities to see if there is anything we could do to help"
  hide Volunteer 1

  show Volunteer 2
  two"What if we changed our original renovation plans to renovate the school in a way that increases water efficiency"

  show Miss Anderson
  a"Those sound like great ideas! Would you all like to come outside so I can show you what is causing all of this?"
  hide Miss Anderson

  show Volunteer 1
  show Jonathan
  j "Sure!"

  scene aboriginal dried river

