from pytube import YouTube, Playlist
from art import tprint

def setup() -> None:  # The setup that runs only once before the loop.
    
    tprint("mp3.py")  # Leveraging the art module to make an ASCII logo.
    print("------------------------------------------")
    return None

def loop() -> None:  # The main code loop and functions related to said loop.
    
    def get_urls(playlist: Playlist) -> list[str]:  # Converts a playlist url into list of urls.
        
        print("Getting urls from your desired playlist...")
        return [url for url in playlist.video_urls]

    def download(urls: list[str]) -> None:  # Reusable download function for videos and playlists.
        
        def convert_title(title: str) -> str: # Converts the video title into someting downloadable.
            
            converted_title: list[str] = [c for c in title if c.isalpha() or c.isdigit() or c.isspace()]
            return ''.join(converted_title).rstrip()
        
        print("Successfully fetched url(s), now downloading your video(s)...")
        
        for url in urls:  # Iterating through each url in the playlist/video.
            
            try:
                video: YouTube = YouTube(url)
                stream = video.streams.filter(only_audio=True).first()
                stream.download(filename=f"{convert_title(video.title)}.mp3")
                print(f"{video.title} is downloaded in MP3")
                
            except KeyError:
                print("Unable to fetch video information.")
                return None
            
        print("Successfully downloaded your video(s).")
        return None
    
    def quit() -> bool:  # Defining reusable quit screen before breaking the code loop.
        
        try:
            quitting: int = int(input('Are you sure you want to quit? (0 = No, 1 = Yes): '))
            
            if quitting == 1:
                print("Quitting program...")
                print("------------------------------------------")
                return True
            
            else:
                return False
            
        except Exception:
            print("Quitting program...")
            print("------------------------------------------")
            return True
    
    running: bool = True
    while running:  # The main code loop.
        
        try:    
            video_urls: list = []
            print('What sort of download are you wishing for?')
            download_type: int = int(input('(1 = Video, 2 = Playlist, other = quit): '))
            
            if download_type == 1:  # A Video
                video_urls = input("Input your video url here: ").split(" ")
                
            elif download_type == 2:  # A Playlist
                playlist_url: str = input("Input your playlist url here: ")
                video_urls = get_urls(Playlist(playlist_url))
                print(video_urls)
                
            else: # Quitting
                if quit():
                    return None
                else:
                    continue
        
            download(video_urls)
        
        except Exception: # Quitting
            print("Invalid response.")
            if quit():
                return None

setup()
loop()
