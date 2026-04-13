# ChatApp

ChatApp is a simple chat playground application demonstrating integration with TTC and OpenRouter (or other LLM providers). This README explains how to set up and run the project locally, configure API keys, and build for production.

## Features

- Real-time chat UI for interacting with language model APIs
- Configurable via environment variables
- Local development server and production build

## Requirements

- Node.js (v16 or later recommended)
- npm (or yarn)

## Setup

1. Clone this repository

   git clone <repo-url>
   cd <repo-directory>

2. Install dependencies

   npm install

3. Create a `.env.local` file in the project root containing your API keys. Example:

   ```
   TTC_API_KEY=your_ttc_api_key
   OPENROUTER_API_KEY=your_openrouter_api_key
   ```

   Replace the values with your actual API keys. The app expects these environment variables at runtime.

4. Run the development server

   npm run dev

5. Open your browser at:

   http://localhost:3000

## Scripts

- `npm run dev` - Start the development server (hot reload)
- `npm run build` - Build the production bundle
- `npm run start` - Start the production server after building

## Environment Variables

The following variables are commonly used by the project. Add them to `.env.local` (do not commit secrets to source control):

- TTC_API_KEY - API key for TTC provider
- OPENROUTER_API_KEY - API key for OpenRouter provider

If your deployment environment uses a different configuration system, set equivalent environment variables there.

## Building & Running in Production

1. Build the app:

   npm run build

2. Start the production server:

   npm run start

## Contributing

Contributions are welcome. Please open issues for bugs or feature requests and submit pull requests for proposed changes.

When contributing:
- Keep changes small and focused
- Update or add documentation when behavior or configuration changes

## Troubleshooting

- If the app fails to start, ensure Node.js and npm are installed and that you ran `npm install`.
- If you see authentication or API errors, verify that the keys in `.env.local` are correct and that the provider services are reachable.

## License

This project is provided under whatever license the repository owner has chosen. Check the repository root for a LICENSE file.

---

If you have questions or need help configuring ChatApp, open an issue in this repository with relevant details (error messages, logs, steps to reproduce).