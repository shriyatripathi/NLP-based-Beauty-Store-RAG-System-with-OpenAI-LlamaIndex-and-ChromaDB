from dotenv import load_dotenv
import os
from src.flask_api_rag_setup import app, initialize_rag_system

# Load environment variables
load_dotenv()

# Disable Chroma telemetry
os.environ['ANONYMIZED_TELEMETRY'] = 'False'

def main():
    print("Starting Beauty Store RAG System")
    
    print("Initializing RAG system...")
    initialize_rag_system()

    print("RAG system initialized. Starting Flask server...")
    app.run(debug=False, host='0.0.0.0', port=5000)

if __name__ == "__main__":
    main()