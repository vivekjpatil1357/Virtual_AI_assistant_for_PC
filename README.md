
# Personal PC Assistant "Pixel"

## Overview

"Pixel" is an innovative Personal PC Assistant developed to enhance productivity, efficiency, and user experience across various computing tasks. Leveraging advanced AI algorithms and natural language processing capabilities, Pixel interprets user commands seamlessly, enabling intuitive interaction and swift execution of tasks through voice commands or graphical user interfaces.

## Features

- **Coding Assistance:** Integration with Visual Studio Code (VS Code) for coding assistance, including syntax highlighting, code completion, and debugging capabilities.
- **Multimedia Management:** Organize and access audio, video, and image files. Integration with external APIs for real-time information retrieval (e.g., news updates, weather forecasts).
- **Productivity Tools:** A versatile toolkit designed to empower users in navigating their digital ecosystem with ease and proficiency.
- **Voice Command Functionality:** Hands-free interaction and quick access to information.

## Installation

### Prerequisites

- Operating System: Windows, macOS, or Linux
- [Visual Studio Code](https://code.visualstudio.com/)
- [Python](https://www.python.org/)
- [Electron.js](https://www.electronjs.org/)

### Steps

1. Clone the repository:
    ```bash
    git clone https://github.com/vivekjpatil/Virtual_AI_assistant_for_PC.git
    ```
2. Navigate to the project directory:
    ```bash
    cd frontend
    ```
3. Install the required dependencies:
    ```bash
    npm install
    pip install -r requirements.txt
    ```
4. Run the Electron application:
    ```bash
    npx electron main.js
    ```

### Running the Backend (Flask)

We need to create another terminal for the backend to run the Flask server. Follow these steps:

1. Open a new terminal window.
2. Navigate to the backend directory:
    ```bash
    cd backend
    ```
3. Install the required Python dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Run the Flask server:
    ```bash
    py app.py
    ```

## Usage

1. **Launching Pixel:** After installation, run the application using the command `npx electron main.js`. This will open the Pixel interface.
2. **Voice Commands:** Interact with Pixel using voice commands for tasks such as opening applications, searching the web, or retrieving multimedia files.
3. **Coding Assistance:** Use the integrated features within Visual Studio Code for coding assistance, including syntax highlighting and debugging.

