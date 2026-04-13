# ChatApp

ChatApp is a small chat playground application for experimenting with conversational APIs and local development. This repository provides a minimal setup to run ChatApp locally, configure API keys, and begin development.

## Features

- Local development server
- Simple chat UI for testing conversational flows
- Environment-based API key configuration

## Prerequisites

- Node.js (16+ recommended)
- npm (or yarn)

## Setup

1. Clone this repository

   git clone <repo-url>
   cd <repo-directory>

2. Install dependencies

   npm install

3. Create a .env.local file in the project root and add any required API keys. Example:

   TTC_API_KEY=your_ttc_api_key
   OPENROUTER_API_KEY=your_openrouter_api_key

   Replace the keys above with the appropriate keys for the services you intend to use. If your project uses different environment variable names, adapt accordingly.

4. Run the development server

   npm run dev

5. Open your browser

   http://localhost:3000

## Scripts

- npm run dev: Start the development server
- npm run build: Build the production bundle
- npm start: Start the production server (after build)

(If your project uses different scripts, consult package.json.)

## Contributing

Contributions are welcome. Please open issues or pull requests for bug fixes, feature requests, or documentation improvements.

Guidelines:
- Create a branch for your change: git checkout -b feat/some-feature
- Keep changes focused and well-documented
- Add tests where appropriate

## License

Add the appropriate license for your project. If none is provided, consult the project owner/maintainers.

## Contact

For questions about ChatApp, open an issue in this repository or contact the maintainers.
