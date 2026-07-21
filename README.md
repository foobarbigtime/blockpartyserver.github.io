# Block Party Server

A family-friendly, block-inspired website for a private Minecraft Realm. The site gives players a central place to enter the Block World, play browser mini-games, launch classic text adventures, download keyboard files, review server rules, and request an invite safely.

> This is a fan-made project and is not affiliated with Minecraft, Mojang, or Microsoft.

## Features

- Live multiplayer Block World
- Browser-based mining mini-game
- Classic text adventure links
- Downloadable keyboard files
- Realm join instructions
- Family-friendly server rules
- Privacy guidance for younger players
- Responsive layout for phones, tablets, and desktops
- Keyboard-accessible controls and status messages

## Project structure

```text
.
├── index.html                 # Main landing page and mining game
├── world.html                 # Multiplayer Block World
└── scripts/
    └── keyboard/
        └── keyboard.html      # Keyboard file downloads
```

The current project is intentionally lightweight and uses plain HTML, CSS, and JavaScript with no build system or external framework.

## Run locally

1. Clone or download the repository.
2. Open `index.html` in a modern web browser.
3. For the best results, serve the folder through a small local web server.

Using Python:

```bash
python -m http.server 8000
```

Then open `http://localhost:8000`.

## Safety and privacy

Block Party Realm is intended for invited family and friends. Players are instructed to use nicknames only and avoid sharing personal information such as their full name, age, school, address, or phone number.

Parents or guardians should approve invite requests for younger players.

## Technologies

- HTML5
- CSS3
- Vanilla JavaScript
- GitHub Pages

## Planned improvements

- Separate the embedded CSS and JavaScript into dedicated asset files
- Add screenshots and a project banner
- Add automated link and HTML validation
- Improve the invite-request workflow to reduce email-address scraping
- Add clearer deployment instructions

## Contributing

This is a personal family project, but suggestions and bug reports are welcome through GitHub Issues.

## License

No open-source license has been assigned yet. All rights are reserved unless a license is added later.
