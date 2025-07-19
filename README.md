**AI or Not**

A simple web app that checks whether a piece of text was written by AI or a human. It uses the Hugging Face model `roberta-base-openai-detector`, built with FastAPI and styled with Tailwind CSS.

**Features**

- Analyze pasted text for AI/human probability
- Clean, minimal interface
- No data stored or saved


**Running Locally**

1. Clone the repository:
   git clone https://github.com/HashimmNYC/ai-or-not.git

2. Navigate into the folder:
   cd ai-or-not

3. Install dependencies:
   pip install -r requirements.txt

4. Start the app:
   uvicorn main:app --reload

Then open your browser and go to http://127.0.0.1:8000

**Tech Used**

- FastAPI
- Hugging Face Transformers
- Tailwind CSS
- Render (hosting)


