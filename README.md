# Manawatu Chinese Community Trust Website

[manawatu chinese](https://manawatuchinese.org.nz/)

# Test Users

| Role    | Username | Notes |
| ------- | -------- | ----- |
| Staff   | -        | -     |
| Mentor  | -        | -     |
| Student | -        | -     |

# Code Standards

- Use `4 spaces`
- NO `tab`s
- Use `snake_case` for names
- Use double quotes
- `2 empty lines` between functions

# Ways of Working

- `branch`es should be deleted after merging
- `comments` need to be solved by the "owner/creator"
- A short message should be given in the title of a PR

# Tools

| Type      | Link                                                                                                                                                    |
| --------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| UI Design | [Figma](<https://www.figma.com/file/NeJ6tWqclp6bhAtrPIN6Eg/Bootstrap-UI-Kit-(Community)?type=design&node-id=3989-959&mode=design&t=CKzmRBpFzOm67ezp-0>) |

# Project Setup (Development)

1. Clone the repo to local

1. Add `.env`

   ```bash
   DB_USER="root"
   DB_PASS="J23df3FIO"
   DB_HOST="150.230.9.92"
   DB_PORT="3306"
   DB_NAME="PlacementSystem"
   ENV="DEVELOPMENT"
   SALT="w3rjq,fl2.f"
   PROJECT_DIR="mcct"
   ```

1. Install dependencies

   - by pip3, `pip3 install -r requirements.txt`, or
   - by [poetry](https://python-poetry.org/docs/), `poetry install`

1. Run the project
   - `flask --debug run`
