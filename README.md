# ChatApp

ChatApp is a simple chat playground application that demonstrates integration with TTC and OpenRouter APIs. This repository provides a minimal local development setup so you can run and extend the chat experience.

## Features
- Local development server
- Integration points for TTC and OpenRouter API keys
- Simple chat UI to experiment with model responses

## Prerequisites
- Node.js (v16+ recommended)
- npm

## Setup
1. Clone this repository

   git clone <repository-url>
   cd <repository-directory>

2. Install dependencies

   npm install

3. Create a `.env.local` file in the project root and add your API keys:

   ```env
   TTC_API_KEY=your_ttc_api_key
   OPENROUTER_API_KEY=your_openrouter_api_key
   ```

4. Run the development server

   npm run dev

5. Open the app in your browser

   http://localhost:3000

## Production
To build and run a production build locally:

```bash
npm run build
npm run start
```

## Contributing
Contributions are welcome. Please open issues or pull requests for bug fixes and improvements.

## License
This repository does not specify a license by default. Add a LICENSE file if you intend to open source the project.
