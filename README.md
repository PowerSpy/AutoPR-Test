# cursor-supermemory

A lightweight integration layer for "supermemory" functionality used by Cursor-based tooling. This repository contains utilities for configuring and authenticating an agent-backed memory system for developer workflows.

This project includes code for storing credentials and configuration for both user-global and per-project settings, plus a small "memory-init" skill for exploring and indexing codebases.

Key files and behavior

- src/auth.ts
  - Manages credentials stored at: ~/.supermemory-cursor/credentials.json
  - Exposes helpers to load, save and clear credentials.

- src/config.ts
  - Project config path: .cursor/.supermemory/config.json (per-project)
  - Global config path: ~/.config/cursor/supermemory.json
  - Provides utilities to read and write configuration and default values.

- skills/memory-init/SKILL.md
  - Describes a "memory-init" skill for deep codebase exploration and indexing.

Quick start

1. Prerequisites

- Node.js (16+ recommended)
- npm or yarn

2. Install

Clone the repo and install dependencies:


  git clone https://github.com/supermemoryai/cursor-supermemory.git
  cd cursor-supermemory
  npm install


3. Build (if TypeScript build step is used)

  npm run build

(There may be a build script depending on the project setup. If none exists, running scripts directly with ts-node or node may be appropriate.)

Configuration

- Global configuration is stored at: ~/.config/cursor/supermemory.json
- Project configuration is stored under the project at: .cursor/.supermemory/config.json

Use the config helpers to write settings programmatically. The configuration includes values such as similarityThreshold, maxMemories, injectProfile, and optional container tags.

Authentication

Credentials are saved at: ~/.supermemory-cursor/credentials.json. Use the provided auth helpers in src/auth.ts to save and load an apiKey. Files are created with restrictive permissions (mode 0o600 for the credentials file and 0o700 for the credentials directory).

Contributing

Contributions are welcome. Suggested workflow:

1. Fork the repository
2. Create a feature branch
3. Add tests for new code paths
4. Open a pull request

When adding features that change behavior (especially around config and auth), please include unit tests for the new behavior.

Project conventions

- Config and credentials are stored in OS-appropriate locations (home directory for global secrets and standard config location for global settings).
- Project-specific config is discovered by walking up the filesystem to find a .cursor/.supermemory/config.json file.

License

This repository does not yet include a license file. Please add a LICENSE to indicate the desired license for this project.

Notes

This README is intentionally general to serve as a starting point. If you prefer more detailed setup instructions, environment variables, or examples of how this library is consumed (CLI, editor extension, or other), please open an issue or a PR with suggested documentation improvements.
