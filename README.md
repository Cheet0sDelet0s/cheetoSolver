# cheetoSolver
cheetoSolver - an AI macro to help you with sparx maths

i hate sparx maths, and you probably do too. i was bored and decided to make a little macro which takes a screenshot of the screen, sends it to bing AI and gets you your answer.

now, because of limitations with bing/chatgpt, quite a few types of questions cannot seemed to be handled, usually ones where there are many steps to working the question out, and where it has to read lots of charts and graphs, stuff like that. it is pretty good at word equations and stuff that can be worked out with formulas. 

this is only the first version, so its janky and needs to be set up correctly, but once it works its pretty cool.

-- setup and use:
- download python
- open cheetoSolver folder in terminal and run:
  ```pycon
  pip install -r requirements.txt
  ```
- open two chrome windows, one with sparx maths, one with bing AI
- maximise sparx maths and minimize bing AI (if you have multiple monitors, make sure both are on your primary one
- make sure there are no other windows visible on screen except sparx and cheetoSolver
- click solve and dont touch your mouse or keyboard until its sent the request

this is mostly designed for kids, so i put a how to use file in here which makes it super easy to use lmao
