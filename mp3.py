from pytube import YouTube, Playlist
from art import tprint

def get_urls(playlist: object) -> list:
    print("Getting urls from your desired playlist...")
    return [url for url in playlist.video_urls]

def download(urls: list) -> None:
    for url in urls:
        
        try:
            video = YouTube(url)
            stream = video.streams.filter(only_audio=True).first()
            stream.download(filename=f"{"".join([c for c in video.title if c.isalpha() or c.isdigit() or c.isspace()]).rstrip()}.mp3")
            print(f"{video.title} is downloaded in MP3")
            
        except KeyError:
            print("Unable to fetch video information. Please check the video URL or your network connection.")
            return None
        
    print("Successfully downloaded your video(s).")
    return None
            
def run() -> None:
    def quit():
        try:
            quitting = int(input('Are you sure you want to quit? (0 = No, 1 = Yes)'))
            
            if quitting == 1:
                print("Quitting application...")
                return True
            
            else:
                return False
            
        except Exception:
            print("Quitting application...")
            return True
    
    tprint("mp3.py")
    print("------------------------------------------")
    running: bool = True
    
    while running:
        try:
            download_type: int = int(input('What sort of download are you wishing for? \n(1 = Video, 2 = Playlist): '))
            
            if download_type == 1:
                video_urls: list = input("Input your video url here: ").split(" ")
                
            elif download_type == 2:
                playlist_url: str = input("Input your playlist url here: ")
                video_urls: list = get_urls(Playlist(playlist_url))
                
            else:
                if quit():
                    break
        
            print("Successfully fetched url(s), now downloading your video(s)...")
            download(video_urls)
            
            return None
        
        except Exception:
            print("Invalid response.")
            if quit():
                break
        
run()