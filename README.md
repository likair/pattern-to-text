# Pattern to Text

![Github Workflow](https://github.com/likair/hansen-cloud-engineer-task/actions/workflows/main.yml/badge.svg)

Initially, I thought the programming task was at easy level, but it took me roughly a day for the project considering no time constraint.

While I could easily achieve a basic solution that works, refining it to be clean, modular, fully-tested, and well-documented definitely presented a challenge.

Overall, it was an excellent opportunity to sharpen must-have Python skills.

## Instructions

### Pre-requisites

- Python (>3.9.1)
- Docker (optional)

### Quickstart

A single `make` command will install all required dependencies and execute the unit tests.

```
make
```

### Running Locally

- `./src/pattern_to_text PATTERN INTEGERS`: run the program with the given arguments
- `make test`: run unit tests
- `make run`: run the program with default arguments
- `make clean`: remove temporary files

### Running as a Docker Container (Optional)

```
make build_image
docker run pattern-to-text SST 5 2
```
