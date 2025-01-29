import google.generativeai as genai
import os
import time
from dotenv import load_dotenv
from PIL import Image
from colorama import Fore, Style, init

# Initialize colorama for colored text
init(autoreset=True)

# Load environment variables from .env file
load_dotenv()

# Configure the API with your key
genai.configure(api_key=os.getenv('API_KEY'))

# Initialize the model
model = genai.GenerativeModel("gemini-1.5-flash")

def display_welcome():
    """Display welcome message and instructions"""
    print(Fore.CYAN + "\n" + "="*50)
    print(Fore.YELLOW + "✨ Magical Story Generator ✨")
    print(Fore.CYAN + "="*50)
    print(Fore.GREEN + "\nWelcome to the AI Storyteller!")
    print("1. Provide an image path")
    print("2. Choose story preferences")
    print("3. Receive a unique story!\n")  # Removed the 4th option

def get_story_preferences():
    """Get user preferences for story generation"""
    print(Fore.MAGENTA + "\nStory Customization Options:")
    genre = input(Fore.WHITE + "Enter preferred genre (adventure/mystery/fairy tale): ").lower()
    character = input(Fore.WHITE + "Enter main character name (optional): ")
    return genre, character

def validate_image(image_path):
    """Validate the image file format and existence"""
    if not os.path.exists(image_path):
        raise FileNotFoundError
    if Image.open(image_path).format.lower() not in ['jpeg', 'png', 'webp']:
        raise ValueError("Unsupported image format")

def image_to_story():
    try:
        display_welcome()
        
        # Get image path from user
        image_path = input(Fore.WHITE + "\n📸 Enter path to your image file: ")
        validate_image(image_path)
        
        # Get story preferences
        genre, character = get_story_preferences()
        
        # Create dynamic prompt
        prompt = f"""Create a {genre} story based on this image. 
        Main character: {character if character else 'create original character'}.
        Include vivid descriptions, dialogue, and plot twists.
        Writing style: Engaging and imaginative with emojis where appropriate.
        Target audience: All ages."""
        
        # Generate content with loading animation
        print(Fore.YELLOW + "\n🔮 Weaving your story...", end='', flush=True)
        start_time = time.time()
        response = model.generate_content([prompt, Image.open(image_path)])
        
        # Validate response
        if not response.text:
            raise ValueError("Empty response from API")
            
        # Display generation time
        print(Fore.GREEN + f"\n\n✅ Story crafted in {time.time()-start_time:.1f}s!")
        
        # Display the generated story
        print(Fore.CYAN + "\n" + "="*50)
        print(Fore.YELLOW + "📖 Your Magical Story 📖")
        print(Fore.CYAN + "="*50)
        print(Fore.WHITE + response.text)
        print(Fore.CYAN + "="*50)
            
    except FileNotFoundError:
        print(Fore.RED + f"\nError: File not found at {image_path}")
    except Exception as e:
        print(Fore.RED + f"\n⚠️ Error: {str(e)}")
    finally:
        print(Fore.MAGENTA + "\nThank you for using the Magical Story Generator! 🎉\n")

if __name__ == "__main__":
    image_to_story()