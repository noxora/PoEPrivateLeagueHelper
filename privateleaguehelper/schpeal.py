current_league = "Ultimatum gauntlet practice"
league_link = "https://www.pathofexile.com/private-leagues/league/LiamsSufferingGames"
schpeal_intro = f"""
Hello! I'm Private league helper here to help you get into a private league.
The current league is set to: {current_league}
The link to the current league is: {league_link}
The current donation required to skip the line is a minimum of 10 points, but more than 10 is always appreciated if you're able

If you would like to **get in line** for entry, please **follow the link** to the league and **apply at the top** of the page

If you would like to **skip the line** which **requires a crowdfund donation of 10 points**, reply with ```!crowdfund```
If you have a **quick question**, reply with ```!faq```
If you need help, or still have questions, reply with ```!help``` so that I can ask a mod to message you on discord. You must be in the racing discord for a mod to find you!
"""
schpeal_unknown = "Hello! I didn't see a command in your message, if you would like instructions, please respond with ```!intro```"
schpeal_crowdfund = """If you are able to **at least contribute 10 points** to the crowdfund, please follow these steps to skip the line

**1.** Please apply to the league at the link above

**2.** When you are ready, send me a message with your PoE account name, like this
```!register <my-account-name>```**Please include the angled brackets!**
I'll then take your name and send it to our list of moderators, they'll add you as soon as they can
Once you've been added, a fund button will appear at the top of the league and you'll be able to crowdfund. 

**3.** Please **take two screenshots, one before and after crowdfunding**. Please show both your account's points and the current crowdfund level in each picture! 
When you send them to me, please include the text ```!proof <my-account-name>```in any message which has a picture of proof

If you would like an **example proof image**, please reply with ```!example```
"""
schpeal_faq = """**Why are there still spots available in the league? Why not fill the league up all of the way?** 
By holding about 12 spots, we are able to guarantee that crowdfunders are let in when they crowdfund. This leads to more crowdfunding and more people overall getting in

**Why 10 points and not 6 or 12?**
6 or 12 points would be to pay for the crowdfunder's spot or their spot + 1
We wanted to make it more than 6 points so that crowdfunders are paying for at least a little more than their own spot
We decided to go with 10 points because it allows people to buy the minimum 50 points, and gain entry to 5 leagues cleanly.
"""

error_no_username = "Sorry, I'll need an account name for that. Please make sure your account name is between < and > "
error_no_image = "I don't see an image in that message, please try again"
error_not_image = (
    "I see that you've sent files, but they don't appear to be images, please try again"
)
error_typo = "I don't recognize that command, please double-check your spelling"
confirmation_registered = "I've forwarded your request for entry, I'll let you know when a moderator tells me you've been added!"
confirmation_admitted = "A Moderator has indicated that they've added you to the league!\nGood luck and have fun!\nPlease remember to submit proof as soon as you can"
confirmation_help = "I've forwarded your request for help, a mod will reach out to you as soon as they can!"
confirmation_proof = "Your proof has been successfully submitted, thank you!"

example_proof = "This is an example before image, an example after image should be the same but with the crowdfund bar increased by at least 10 points and your account's points decreased by 10 points"
