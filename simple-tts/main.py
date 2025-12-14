import asyncio
import edge_tts
import pygame
import os

# Voice options for Vietnamese:
# "vi-VN-HoaiMyNeural" (Female)
# "vi-VN-NamMinhNeural" (Male)
VOICE = "vi-VN-HoaiMyNeural"
OUTPUT_FILE = "output.mp3"

async def generate_audio(text):
    print(f"Generating audio for: '{text}'...")
    communicate = edge_tts.Communicate(text, VOICE)
    await communicate.save(OUTPUT_FILE)
    print(f"Saved to {OUTPUT_FILE}")

def play_audio():
    print("Playing audio...")
    pygame.mixer.init()
    pygame.mixer.music.load(OUTPUT_FILE)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.quit()
    # Clean up file afterwards if desired, but keeping it for now
    # os.remove(OUTPUT_FILE) 

if __name__ == "__main__":
    text = input("Enter Vietnamese text to speak: ")
    if not text:
        text = "Xin chào, đây là ví dụ về chuyển đổi văn bản thành giọng nói tiếng Việt."
    
    try:
        asyncio.run(generate_audio(text))
        play_audio()
    except Exception as e:
        print(f"Error: {e}")
