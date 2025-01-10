import yt_dlp

def download_yt_video(url):
    ydl_opts = {
        'format': 'bestvideo[height<=1080]', # Download best option up to 1080 or adjust for higher or lower quality.
        'noplaylist': True, # Ensures only video you want not entire playlist 
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl: # Using the youtube dl class for yt_dlp
        ydl.download([url])

if __name__ == '__main__':
    video_url = input('Enter the Youtube Video URL: ')
    download_yt_video(video_url)
