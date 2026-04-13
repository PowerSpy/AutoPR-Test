# ChatApp

ChatApp is a simple chat playground that demonstrates how to connect to language model APIs and build a real-time chat interface.

Features
- Real-time chat UI for interacting with a language model
- Easy local development setup
- Configurable API keys via .env.local

Setup
1. Clone this repository:

   git clone <repo-url>
   cd <repo-directory>

2. Install dependencies:

   npm install

3. Create a `.env.local` in the project root with your API keys. Example:

   TTC_API_KEY=your_ttc_api_key
   OPENROUTER_API_KEY=your_openrouter_api_key

4. Run the development server:

   npm run dev

5. Open your browser to:

   http://localhost:3000

Environment Variables
- TTC_API_KEY: API key for TTC (The Token Company) services (if used by the project)
- OPENROUTER_API_KEY: API key for OpenRouter or other routing-based LM providers

Scripts
- npm run dev: Start the development server
- npm run build: Build the app for production
- npm run start: Start the production server (after build)

Development Notes
- The app is referred to as "ChatApp" in documentation and UI copy.
- Check the codebase for components and configuration that reference environment variables; ensure your `.env.local` includes the required keys.

Contributing
- Contributions are welcome. Please open an issue first to discuss major changes.
- For small fixes or docs updates, open a pull request with a short description of the change.

License
This project is provided under the MIT License unless otherwise specified in repository files.

Contact
If you have questions, open an issue in the repository with the "question" or "help wanted" label.
