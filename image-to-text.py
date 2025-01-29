import google.generativeai as genai
import os
from dotenv import load_dotenv
from PIL import Image

# Load environment variables from .env file
load_dotenv()

# Configure the API with your key
genai.configure(api_key=os.getenv('API_KEY'))

# Initialize the model
model = genai.GenerativeModel("gemini-1.5-flash")

def image_to_story():
    # Get image path from user
    image_path = input("Enter the path to your image file: ")
    
    try:
        # Load the image file
        img = Image.open(image_path)
        
        # Create the prompt
        prompt = """Create a creative story based on this image. 
        The story should be engaging and suitable for all ages. 
        Include descriptive elements from the image in the narrative."""
        
        # Generate content with both image and text prompt
        response = model.generate_content([prompt, img])
        
        # Display the generated story
        print("\n" + "="*50)
        print("Generated Story:")
        print("="*50)
        print(response.text)
        print("="*50 + "\n")
        
    except FileNotFoundError:
        print(f"Error: File not found at {image_path}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    image_to_story()