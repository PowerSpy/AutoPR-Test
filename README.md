# ChatApp

ChatApp is a lightweight chat playground for experimenting with chat integrations and LLM-based assistants. It demonstrates how to wire up API keys and run a local development instance so you can prototype chat experiences quickly.

## Features
- Local development server for rapid iteration
- Easily configured via environment variables
- Simple chat UI for testing assistant responses

## Setup
1. Clone this repository:

   git clone <repository-url>
   cd <repository-directory>

2. Install dependencies:

   npm install

3. Create a `.env.local` file in the project root with your API keys. Example:

   TTC_API_KEY=your_ttc_api_key
   OPENROUTER_API_KEY=your_openrouter_api_key

4. Run the development server:

   npm run dev

5. Open the app in your browser:

   http://localhost:3000

## Usage
- Use the chat UI to send messages and see assistant responses.
- Update configuration and API keys in `.env.local` as needed.

## Contributing
Contributions are welcome. Please open issues or pull requests with suggested improvements or fixes.

## License
This project is provided as-is. Add a license file if you intend to distribute the project.
