---
updated: 2026-10-04 --- 20:41:21
---
```text
MojiTerm
├── CHANGELOG.md
├── data
├── docs
│  ├── architecture.md
│  ├── Database Models.md
│  └── LICENSE
├── logs
├── poetry.lock
├── pyproject.toml
├── README.md
├── src
│  └── mojiterm
│     ├── __init__.py
│     ├── backend      # server, logic & persistence
│     │  ├── __init__.py
│     │  ├── database
│     │  │  ├── __init__.py
│     │  │  ├── models
│     │  │  │  ├── __init__.py
│     │  │  │  ├── kana.py
│     │  │  │  ├── kanji.py
│     │  │  │  ├── progress.py
│     │  │  │  └── user.py
│     │  │  └── session.py
│     │  ├── main.py
│     │  ├── schemas
│     │  │  ├── __init__.py
│     │  │  ├── kana_schemas.py
│     │  │  ├── kanjis_schemas.py
│     │  │  └── user_schemas.py
│     │  └── services
│     │     ├── __init__.py
│     │     ├── algorithm.py
│     │     └── lifecycle.py
│     ├── client       # terminal user interface (TUI)
│     │  ├── __init__.py
│     │  ├── api
│     │  │  ├── __init__.py
│     │  │  └── request.py
│     │  ├── app.py
│     │  ├── styles
│     │  │  ├── basic_styles.tcss
│     │  │  ├── library_styles.tcss
│     │  │  ├── quiz_styles.tcss
│     │  │  └── strokes_styles.tcss
│     │  └── views
│     │     ├── __init__.py
│     │     ├── base_views.py
│     │     ├── character_views.py
│     │     └── quiz_views.py
│     └── shared       # common utilities & configurations
│        ├── __init__.py
│        ├── config.py
│        └── logger.py
└── tests              # unit tests
   ├── __init__.py
   ├── backend
   └── client
```
## Principal Modules
- `src/mojiterm/backend/`: Implements server logic and data management.
	- `database/`: Defines the database connection and persistence models (`kana`, `kanji`, `progress`, `user`).
    - `schemas/`: Data validation and serialization schemas (Pydantic).
    - `services/`: Pure business logic, such as the spaced repetition/study algorithm (`algorithm.py`) and server lifecycle events (`lifecycle.py`).
    - `main.py`: Backend service entry point and route/endpoint definitions.
- `src/mojiterm/client/`: Terminal client layer (TUI/Textual).
    - `api/`: HTTP client (`request.py`) responsible for consuming the backend API.
    - `views/`: Visual components and screens (base views, character dictionary, and quizzes).
    - `styles/`: TCSS stylesheets for the interface (quiz, strokes, library, and general styles).
    - `app.py`: Main instance and lifecycle for the terminal application.
- `src/mojiterm/shared/`: Agnostic code used by both the client and the backend.
    - `config.py`: Environment variable loading and global configurations.
    - `logger.py`: Unified configuration for event logging and debugging.
- `data/` & `logs/`: Local storage for SQLite databases / static files and runtime system logs.
