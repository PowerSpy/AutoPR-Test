# ChatApp

ChatApp is a simple playground for experimenting with chat integrations and conversational AI. This repository provides a minimal developer setup to run the app locally and connect to required APIs via environment variables.

## Features

- Basic chat UI for testing conversational flows
- Uses TTC and OpenRouter keys for backend integrations
- Simple dev-focused setup for quick iteration

## Setup

1. Clone this repository

   git clone <repo-url>
   cd <repo-directory>

2. Install dependencies

   npm install

3. Create a `.env.local` file in the project root with your API keys:

   TTC_API_KEY=your_ttc_api_key
   OPENROUTER_API_KEY=your_openrouter_api_key

4. Run the development server

   npm run dev

5. Open the app in your browser

   http://localhost:3000

## Usage

- Open the app in your browser and interact with the ChatApp UI.
- Ensure your API keys are correctly provided in `.env.local` so the app can reach external services.

## Contributing

Contributions are welcome. If you plan to make changes, please open an issue first to discuss the proposed changes. For bug fixes and features, please submit a pull request with a clear description of the change.

## License

This project does not include a license file by default. If you wish to include one, add a LICENSE file to the repository.
