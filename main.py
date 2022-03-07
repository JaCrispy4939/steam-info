#Please note this isnt done yet

import requests
from bs4 import BeautifulSoup
import lxml
import lxml.html


def main():
    import lxml.html
    username = input("Enter Username: ")


    page = requests.get("https://steamcommunity.com/id/" + username + "")
    soup=BeautifulSoup(page.content,"html.parser")
    soup_condition=BeautifulSoup(page.content,"html.parser")
    lxml = lxml.html.fromstring(page.content)

    playtime = soup.find(class_="recentgame_quicklinks recentgame_recentplaytime").text
    recentgame = soup.find(class_="game_name").text
    status = soup.find(class_="profile_in_game_header").text
    bio = soup.find(class_="profile_summary noexpand").text

    if bio == None:
        bio = "User has not setup a Bio"

    print(f"Play Time: {playtime}\nRecent Game: {recentgame}\nStatus: {status}\nBio: {bio}")

main()
