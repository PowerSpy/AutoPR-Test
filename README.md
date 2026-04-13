# ChatApp

ChatApp is a small chat playground application that demonstrates integration with TTC and OpenRouter APIs. It provides a local development setup so you can experiment with chat interactions and API-backed responses.

## Features
- Simple chat UI for testing conversational flows
- Connects to TTC and OpenRouter APIs via environment variables
- Quick local development setup with npm

## Setup
1. Clone this repository

   git clone <repository-url>
   cd <repository-directory>

2. Install dependencies

   npm install

3. Create a `.env.local` file in the project root with your API keys. Example:

```
TTC_API_KEY=your_ttc_api_key
OPENROUTER_API_KEY=your_openrouter_api_key
```

4. Run the development server

   npm run dev

5. Open the app in your browser:

   http://localhost:3000

## Environment Variables
- TTC_API_KEY — Your TTC API key used by ChatApp to interact with TTC services.
- OPENROUTER_API_KEY — Your OpenRouter API key used by ChatApp for routing requests.

Ensure you do not commit `.env.local` or your API keys to source control.

## Contributing
Contributions are welcome. Please open issues for bugs or feature requests, and submit pull requests for fixes or improvements.

## License
This project does not include a specific license file. Add a LICENSE file if you want to specify license terms.
