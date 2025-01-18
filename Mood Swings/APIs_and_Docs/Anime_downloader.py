import requests
from bs4 import BeautifulSoup
import yt_dlp

def scrape_anime_episodes(base_url):
    # Step 1: Send a request to the anime page
    response = requests.get(base_url)
    response.raise_for_status()
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Step 2: Find episode links (adjust selector based on site structure)
    episodes = []
    for link in soup.select('a.episode-link'):  # Update selector to match the site
        episodes.append(link['href'])
    return episodes

def download_anime_episode(video_url):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',
        'merge_output_format': 'mp4',
        'noplaylist': True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([video_url])

if __name__ == '__main__':
    base_url = input('Enter the URL of the anime page: ')
    episodes = scrape_anime_episodes(base_url)
    
    for i, episode_url in enumerate(episodes, start=1):
        print(f'Downloading Episode {i}: {episode_url}')
        try:
            download_anime_episode(episode_url)
        except Exception as e:
            print(f'Failed to download {episode_url}: {e}')
