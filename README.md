- Asteroids Game (Pygame)

This project is a simple *Asteroids-style game* developed in Python using the Pygame library. Its purpose is to demonstrate object-oriented programming, event handling, collision detection, and a basic game loop.


- Requirements

Python 3.0 or higher
Operating system: Windows, macOS, or Linux

- Project Structure


.
├── main.py
├── player.py
├── asteroid.py
├── asteroidfield.py
├── shot.py
├── constants.py
├── README.md
└── venv/                 Virtual environment (not committed to the repository)
```


- Virtual Environment Setup

Follow the steps below to create a **virtual environment** and install the required dependencies.

- 1. Clone the repository or download the project

Navigate to the project directory using your terminal:
bash
cd path/to/your/project




- 2. Create the virtual environment

#### Windows

```bash
python -m venv venv
```

#### macOS / Linux

```bash
python3 -m venv venv
```

This will create a folder named `venv` containing the virtual environment.



3. Activate the virtual environment

  - Windows (CMD or PowerShell)

bash
venv\Scripts\activate
```

  - macOS / Linux

bash
source venv/bin/activate


When the environment is active, `(venv)` will appear at the beginning of your terminal prompt.



4. Install dependencies

With the virtual environment activated, install **Pygame**:

  bash
pip install pygame



5. Run the game

From the project directory and with the environment activated:

bash
python main.py


or, if required by your system:

```bash
python3 main.py
```

---

## Basic Controls

* Movement and shooting: WASD(Navigation arrows also work) / SPACE
