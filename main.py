from youtube_transcript_api import YouTubeTranscriptApi
from deep_translator import GoogleTranslator
import requests
from bs4 import BeautifulSoup
import re 

def getTitle(yt_url):
    try:
        page = requests.get(yt_url)
        soup = BeautifulSoup(page.content, "html.parser")
        title = soup.text.split(" - YouTubeAboutPressCopyrightContact")[0]
        return title
    except Exception as e:
        return 'No Title'

def getTranscript():
    try:
        transcript = YouTubeTranscriptApi.get_transcript("dLPio7v1gew", languages=['de'])
        lines = ''
        for t in transcript:
            start = round(t['start'], 1)
            end  = round(start + t["duration"], 1)
            lines += t['text']

            if len(lines.split(' ')) >= 15:
                with open('out.txt', 'a', encoding='utf8') as file:
                    file.write(GoogleTranslator(source='de', target='en').translate(lines))
                    file.write('\n')
                lines = ''

    except Exception as e:
        print(e)

getTitle("https://www.youtube.com/watch?v=NIu71an-ks8")



