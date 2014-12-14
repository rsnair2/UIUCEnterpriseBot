<h1> University of Illinois @ Urbana Champaign Enterprise WebBot </h1>

Classes in UIUC tend to fill up fairly quickly. However, people do drop courses, though depending on the course it may not happen frequently. The UIUC Enterprise WebBot allows students of UIUC to sign up for a course as soon as its available. This WebBot is used to poll the University of Illinois Enterprise website
for information about whether a class is available or not. Just enter your
username, password, term and the specific classes you want the WebBot to poll
for and the WebBot will automatically signup for that class as soon as it opens up. 

You will need to download and install the
<a href="http://docs.python-requests.org/en/latest/">
Requests </a> library for python.

Some features that I plan on adding are:
<ol>

<li>
Auto-completion features so that when you start typing in a given Major, Course
or CRN it suggests possible completions.
</li>

<li>
Ability to configure a plan of action in the event a class is found to be open. For instance, one should be able to specify which classes you want to add and drop when a class or set of classes that you are monitoring open up and have the webbot automatically do that for you. 
</li>
</ol>

If you have some ideas, or if you want to contribute, feel free to get in touch
with me. :)

<h4> Disclaimer </h4>

<p>
Please note that I cannot provide any warranties on this software.
This bot has not been through thorough testing and while it works most of
the times, there might be some circumstances unaccounted for. Also,
if the UIUC Enterprise website is to change at any point, the WebBot might
break as well. Please use with caution.
</p>

<p>
Also, the bot is rate limited at this stage, please do not modify this behavior.
This is done to prevent the bots from bogging down the University of Illinois
server. Reducing the rate at which you poll should not be a problem.
</p>

***

&#169; Rajiv Nair (rsnair.me)