# ChatApp

ChatApp is a simple chat playground application that demonstrates connecting a frontend to an LLM-backed chat API. It provides a minimal developer setup to run a local development server, configure API keys, and experiment with chat interactions.

## Features

- Local development server for a chat UI
- Simple configuration via .env.local
- Extensible codebase to add integrations or custom models

## Prerequisites

- Node.js (v16 or later recommended)
- npm (comes with Node.js)

## Setup

1. Clone this repository

   git clone <repo-url>
   cd <repo-directory>

2. Install dependencies

   npm install

3. Create a .env.local file in the project root and add your API keys

   # Example .env.local
   TTC_API_KEY=your_ttc_api_key
   OPENROUTER_API_KEY=your_openrouter_api_key

   Replace the variables above with the API keys or credentials required by your environment. If your project uses different environment variables, update this file accordingly.

4. Run the development server

   npm run dev

5. Open the app in your browser

   http://localhost:3000

## Development

- Start the dev server: npm run dev
- Build for production: npm run build
- Start production server (if configured): npm start

Adjust scripts in package.json as needed for your project.

## Contributing

Contributions are welcome. Please open issues or pull requests for bug fixes, new features, or improvements.

## License

This repository does not include a specific license file by default. Please add a LICENSE file if you wish to set licensing terms for the project.

## Notes

- The README above provides a general setup based on common conventions. If your project requires additional environment variables or build steps, update the .env.local instructions and the scripts section accordingly.
- The app name used throughout this README is "ChatApp" as requested.