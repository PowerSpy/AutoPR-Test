# ChatApp

ChatApp is a simple chat playground application for experimenting with conversational AI backends and integrations. This repository provides a straightforward local development setup so you can run and test the app on your machine.

## Features

- Minimal chat UI for testing conversational flows
- Easy local development workflow
- Simple environment-based API key configuration

## Prerequisites

- Node.js (v16+ recommended)
- npm (or yarn)

## Setup

1. Clone this repository:

   git clone <repository-url>
   cd <repository-directory>

2. Install dependencies:

   npm install

3. Create a `.env.local` file in the project root with required API keys. Example:

   # .env.local
   TTC_API_KEY=your_ttc_api_key
   OPENROUTER_API_KEY=your_openrouter_api_key

   Replace the values above with your actual keys. If your deployment or development needs other variables, add them here.

4. Run the development server:

   npm run dev

5. Open the app in your browser:

   http://localhost:3000

## Scripts

- npm run dev — start the development server
- npm run build — build the production bundle (if applicable)
- npm run start — start the production server (if applicable)

(Adjust available scripts to match your project's package.json.)

## Contributing

Contributions are welcome. Please open an issue or submit a pull request with clear descriptions of changes.

## Troubleshooting

- If the app doesn't start, ensure Node.js and npm are installed and that dependencies installed without errors.
- Verify the keys in `.env.local` are set correctly and that any external services you use are available.

## License

This repository does not currently specify a license. Add a LICENSE file if you wish to make the terms explicit.

--

If you'd like the README to include a project-specific diagram, screenshots, or more detailed deployment instructions (Vercel, Netlify, Docker, etc.), tell me what to include and I will update it.
