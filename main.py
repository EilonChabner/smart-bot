from config import GOOGLE_API_KEY
import genai_manager

if __name__ == "__main__":
    message = input("Enter your message: ")
    display(generate_response(message))

