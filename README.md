---
updated: 2026-10-10 --- 13:05:05
---
# MojiTerm
**MojiTerm** consists of a TUI application focused on learning Japanese kana and kanji using a game-like setup with quizzes consisting in cards with the Japanese character where you'll have to write the [romaji](https://www.google.com/search?channel=fs&q=romaji) (in kana quizzes) or the meanings (in kanji quizzes) and using a SRS system to track when to repeat any character. Counts with an integrated library to search and see each kanji or kana individually, each one organized by their level (JLPT level in kanji) or character type (such as Dakuon, Handakuon, etc.) in kana.
## Table of Contents
- [[#MojiTerm]]
	- [[#Table of Contents]]
	- [[#Requirements]]
	- [[#Installation]]
	- [[#Usage]]
	- [[#API Reference]]
	- [[#Structure]]
	- [[#Credits]]
	- [[#Contributing]]
	- [[#Tech Stack]]
		- [[#Core]]
		- [[#Development]]
- [[#License]]
---
## Requirements
- Python: `>3.12`
- Pipx: `>1.4.3`
- Poetry: `>2.3.4`
## Installation
### Using Pipx
```bash
pipx install mojiterm
```
### Installing from source
```bash
git clone https://github.com/JD1705/mojiterm.git
cd mojiterm
pipx install .
```
---
## Usage
```bash
mojiterm
```
### Keybindings

| Key | Action |
| --- | ------ |
|     |        |

---
## API Reference

| Method | Endpoint Name                              | Description                                                           |
| ------ | ------------------------------------------ | --------------------------------------------------------------------- |
| GET    | `/health`                                  | Healthcheck verification endpoint to check resources status           |
| GET    | `/progress`                                | Request the user progress data from the database                      |
| GET    | `/quiz/due?type={character_type}&limit=15` | Request a list with the characters to be studied in this quiz session |

see [[docs/API Specification.md|API]] for the full documentation.

---
## Structure
```text
MojiTerm
├── src
│  └── mojiterm
│     ├── backend      # server, logic & persistence
│     ├── client       # terminal user interface (TUI)
│     └── shared       # common utilities & configurations
└── tests              # unit tests
   ├── __init__.py
   ├── backend
   └── client
```
see [[docs/architecture.md|architecture]] for the full specification.

---
## Credits
This project uses the [JMdict/EDICT](https://www.edrdg.org/wiki/index.php/JMdict-EDICT_Dictionary_Project) and [KANJIDIC](https://www.edrdg.org/wiki/index.php/KANJIDIC_Project) dictionary files. These files are the property of the [Electronic Dictionary Research and Development Group](https://www.edrdg.org/), and are used in conformance with the Group's [licence](https://www.edrdg.org/edrdg/licence.html).

Special thanks to the authors of:
- [kanjidicparser](https://github.com/nramkissoon/Kanjidicparser) for providing the parser used in this project.
- [Good-CONTRIBUTING.md-template](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for providing the contribution guidelines used in this project.


---
## Contributing
See the [[docs/Contributing.md|contributing]] file for a full comprehension on how to contribute in this project.

---
## Tech Stack
### Core
- **Language**: Python 3.12+
- **Framework**: FastAPI
- **TUI Client**: Textual
- **ORM**: Tortoise ORM
- **Database**: SQLite (`aiosqlite`)
### Development & Tooling
- **Dependency Management**: Poetry
- **Testing**: Pytest
- **Client Transport**: `httpx` 
- **Logging**: Loguru

---
## License
[[docs/LICENSE|MIT]]
