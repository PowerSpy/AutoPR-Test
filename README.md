# TTC Chat Playground

A small demo playground for the TTC ChatApp — a simple chat application that demonstrates integration with TTC and OpenRouter APIs.

This repository contains the ChatApp frontend and any related tooling to run a local development instance for experimentation and development.

Quick start

1. Clone this repository

   git clone https://github.com/TheTokenCompany/ttc-chat-playground.git
   cd ttc-chat-playground

2. Install dependencies

   npm install

3. Create a .env.local file with your API keys:

   TTC_API_KEY=your_ttc_api_key
   OPENROUTER_API_KEY=your_openrouter_api_key

4. Run the development server

   npm run dev

5. Open the ChatApp in your browser

   Visit http://localhost:3000 to access the ChatApp UI. The ChatApp is the primary demo in this repository — start a conversation and experiment with the integration.

What is the ChatApp?

The ChatApp is a simple chat interface that sends user messages to the configured backend/model provider (TTC / OpenRouter) and displays assistant responses. It's intended as a playground for testing integrations, prompts, and streaming responses.

Key notes

- Ensure your API keys are set correctly in .env.local prior to running the app.
- If you encounter CORS or local network issues in development, check browser network settings or any proxy configuration.

Contributing

Contributions and improvements are welcome. If you'd like to add features or fix bugs, please open a pull request describing your changes.

License

See LICENSE or the repository root for license details.
