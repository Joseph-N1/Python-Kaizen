import yt_dlp

def download_yt_video(url):
    ydl_opts = {
        'format': 'bestvideo+bestaudio/best',  # Download best video and audio and merge them
        'merge_output_format': 'mp4',         # Merge into an MP4 file
        'noplaylist': True,                   # Only download the specified video
        'ffmpeg_location': r'C:\Users\Joseph N Nimyel\OneDrive\Desktop\ffmpeg-master-latest-win64-gpl\ffmpeg-master-latest-win64-gpl\bin\ffmpeg.exe',  # Path to FFmpeg executable
        'postprocessors': [
            {  # Use FFmpeg to merge video and audio
                'key': 'FFmpegMerger',
            },
        ],
        'verbose': True,  # Enable verbose logging for debugging
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except yt_dlp.utils.DownloadError as e:
        print(f"Download error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == '__main__':
    while True:
        video_url = input('Enter YouTube video URL (or "exit" to quit): ').strip()
        if video_url.lower() == "exit":
            print("Exiting the program.")
            break
        if not video_url:
            print("Error: No URL entered. Please try again.")
            continue
        if not video_url.startswith("https://www.youtube.com/"):
            print("Error: Invalid URL. Please enter a valid YouTube video URL.")
            continue

        # Download video
        download_yt_video(video_url)
