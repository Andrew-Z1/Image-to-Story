# Magical Story Generator

## 📖 Overview
The **Magical Story Generator** is an AI-powered storytelling tool that transforms images into engaging stories. Users can provide an image, select a genre, and optionally name a main character to receive a uniquely generated narrative.

## ✨ Features
- Generates creative and immersive stories based on images
- Supports multiple genres: Adventure, Mystery, and Fairy Tale
- Allows users to personalize stories by naming the main character
- Provides real-time feedback and user-friendly prompts
- Uses **Google's Gemini AI** to generate high-quality text
- Includes colorful console output using **Colorama**

## 🚀 Getting Started

### Prerequisites
Ensure you have the following installed:
- Python 3.8+
- Required dependencies:
  - `google-generativeai`
  - `python-dotenv`
  - `pillow`
  - `colorama`

### Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/magical-story-generator.git
   cd magical-story-generator
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the project directory and add your API key:
   ```env
   API_KEY=your_google_genai_api_key
   ```

## 🛠 Usage
1. Run the script:
   ```sh
   python story_generator.py
   ```
2. Follow the on-screen prompts:
   - Enter the path to an image file (JPEG, PNG, or WebP supported)
   - Choose a story genre (Adventure, Mystery, or Fairy Tale)
   - Optionally, enter a name for the main character
3. The AI will generate and display a unique story based on your inputs.

## 🎨 Example Output
```
==================================================
✨ Magical Story Generator ✨
==================================================

Welcome to the AI Storyteller!
1. Provide an image path
2. Choose story preferences
3. Receive a unique story!

📸 Enter path to your image file: example.jpg

Story Customization Options:
Enter preferred genre (adventure/mystery/fairy tale): adventure
Enter main character name (optional): Alice

🔮 Weaving your story...

✅ Story crafted in 3.5s!

==================================================
📖 Your Magical Story 📖
==================================================
Once upon a time in the Enchanted Forest, Alice stumbled upon a glowing portal...
==================================================
Thank you for using the Magical Story Generator! 🎉
```

## ⚠️ Error Handling
The program handles various errors gracefully, including:
- Invalid image path (FileNotFoundError)
- Unsupported image format (ValueError)
- API errors (genai.Error)
- Unexpected issues with informative error messages

## 📜 License
This project is open-source under the MIT License.

## 💡 Future Improvements
- Support for additional genres
- Integration with text-to-speech for narrated storytelling
- Web-based interface for a more interactive experience

---
🎉 **Enjoy crafting magical stories!**
