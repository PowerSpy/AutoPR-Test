# cursor-supermemory

A small TypeScript utility that integrates with the Cursor tooling and Supermemory services to manage project and global configuration and credentials. This repository contains code for reading/writing configuration, storing credentials locally, and initial "memory-init" skill definitions for exploring a codebase.

This README gives an overview of the repo, how to build and run it, and where to look for relevant configuration and authentication code.

Features
- Read and write project and global configuration (see src/config.ts)
- Store and manage local credentials securely (see src/auth.ts)
- Skill definitions for initializing project memory and indexing the codebase (skills/)

Quickstart
1. Install dependencies

   npm install

2. Build (if you're using TypeScript tooling)

   npm run build

3. Run or use the code

   This repository exposes helper modules under src/. Import them into your application or run tooling that depends on them.

Key files
- src/config.ts
  - GLOBAL_CONFIG_PATH: default global config (~/.config/cursor/supermemory.json)
  - getProjectConfigPath(cwd): returns the project config path (.cursor/.supermemory/config.json)
  - writeConfig(updates, scope, cwd): writes updates to the chosen scope (project or global)
  - DEFAULTS: default configuration values
  - Helper functions: readJson, findProjectConfig

- src/auth.ts
  - Manages local credentials in the user's home directory (~/.supermemory-cursor/credentials.json)
  - loadCredentials(): returns stored apiKey and createdAt if present
  - saveCredentials(apiKey): saves the api key with secure file modes
  - clearCredentials(): removes stored credentials

- skills/memory-init/SKILL.md
  - A skill document describing how to initialize project memory by exploring the codebase

Configuration
- Global configuration file: ~/.config/cursor/supermemory.json
- Project configuration file: <repo-root>/.cursor/.supermemory/config.json

Secrets and credentials
- Credentials are stored under ~/.supermemory-cursor/credentials.json by default. The auth helper attempts to use secure file permissions when creating this file.

Contributing
- Contributions are welcome. Please open an issue or a PR describing the change you want to make.
- Follow existing code style and add tests for any logic changes.

License
- Add a LICENSE file as appropriate for your project. This repository currently does not include a license file.

Notes
- This README is intentionally brief. For implementation details, read the code under src/ and the skill docs under skills/.
- If you plan to publish a package or add a CLI, include package.json, scripts, and usage examples in this README.
