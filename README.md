# ChatApp

ChatApp is a lightweight chat playground application for experimenting with chat interfaces and LLM integrations. It provides a starter UI and wiring to connect to language model APIs and demo features like streaming responses, conversation history, and simple tool integrations.

Features
- Simple chat UI for user <-> assistant conversations
- Streaming/real-time assistant responses (where supported by the provider)
- Conversation history (in-memory/session)
- Easy configuration via environment variables

Quickstart
Prerequisites
- Node.js (v14+ recommended)
- npm or yarn

Install and run
1. Clone the repository

   git clone <repo-url>
   cd <repo-directory>

2. Install dependencies

   npm install
   # or
   yarn install

3. Create an environment file

Create a file named .env.local in the project root and add any required API keys. Example:

   TTC_API_KEY=your_ttc_api_key
   OPENROUTER_API_KEY=your_openrouter_api_key

The repository may use different environment variable names depending on which provider you choose. Check source code for exact env names if you encounter errors.

4. Run the development server

   npm run dev
   # or
   yarn dev

5. Open the app

   Visit http://localhost:3000 in your browser.

Build and production

Build the application for production:

   npm run build
   npm start

Project structure (typical)
- src/ or pages/ — application source code and pages
- public/ — static assets
- .env.local — local environment variables (not checked into source control)
- placeholder.txt — placeholder file included in the repository

Environment variables
- TTC_API_KEY: (optional) API key for TTC provider if used
- OPENROUTER_API_KEY: (optional) API key for OpenRouter provider if used

Adjust variables as needed depending on the specific providers you integrate with.

Contributing
Contributions are welcome. Please open issues for bugs or feature requests and submit pull requests for fixes.

License
This project is provided as-is. Add an appropriate license file if you wish to reuse or distribute the code.

Acknowledgements
This README is a simple starting point to help developers get up and running with ChatApp. Update and expand it to match the repository's specific architecture and setup as the project evolves.
