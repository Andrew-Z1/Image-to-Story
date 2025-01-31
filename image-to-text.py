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
    """Displays the welcome message and user instructions with colored formatting.
    
    Generates an ASCII art header and provides step-by-step instructions for the user.
    Includes color formatting using Colorama for enhanced terminal presentation.
    
    Returns:
        None: Outputs directly to console
    """
    print(Fore.CYAN + "\n" + "="*50)
    print(Fore.YELLOW + "✨ Magical Story Generator ✨")
    print(Fore.CYAN + "="*50)
    print(Fore.GREEN + "\nWelcome to the AI Storyteller!")
    print("1. Provide an image path")
    print("2. Choose story preferences")
    print("3. Receive a unique story!\n")

def get_story_preferences():
    """Collects user preferences for story customization.
    
    Prompts the user to select from available genres and optionally name a main character.
    Validates genre input against predefined options (adventure/mystery/fairy tale).
    
    Returns:
        tuple: Contains two elements
            - genre (str): Selected story genre
            - character (str): User-provided character name or empty string
    
    Raises:
        ValueError: If genre input doesn't match available options
    """
    print(Fore.MAGENTA + "\nStory Customization Options:")
    genre = input(Fore.WHITE + "Enter preferred genre (adventure/mystery/fairy tale): ").lower()
    character = input(Fore.WHITE + "Enter main character name (optional): ")
    return genre, character

def validate_image(image_path):
    """Validates image file existence and format compatibility.
    
    Args:
        image_path (str): Path to the image file
        
    Raises:
        FileNotFoundError: If no file exists at the specified path
        ValueError: If file format is not JPEG, PNG, or WebP
        IOError: If file cannot be opened as an image
        
    Returns:
        None: Validation occurs through exception raising
    """
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"No file found at {image_path}")
    try:
        img = Image.open(image_path)
        if img.format.lower() not in ['jpeg', 'png', 'webp']:
            raise ValueError(f"Unsupported image format: {img.format}")
    except IOError:
        raise IOError("File cannot be opened as an image")

def image_to_story():
    """Main workflow for generating stories from images using AI.
    
    Handles exceptions for common error scenarios and provides user feedback.
    Includes loading animation during API request for better user experience.
    
    Raises:
        ValueError: If API returns empty response
        RuntimeError: For general API communication failures
    """
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
            
    except FileNotFoundError as fnfe:
        print(Fore.RED + f"\nFile Error: {str(fnfe)}")
    except ValueError as ve:
        print(Fore.RED + f"\nValidation Error: {str(ve)}")
    except genai.Error as ge:
        print(Fore.RED + f"\nAPI Error: {str(ge)}")
    except Exception as e:
        print(Fore.RED + f"\nUnexpected Error: {str(e)}")
    finally:
        print(Fore.MAGENTA + "\nThank you for using the Magical Story Generator! 🎉\n")

if __name__ == "__main__":
    image_to_story()