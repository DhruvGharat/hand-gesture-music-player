# Hand Gesture Music Player

Simple project to control music playback using hand gestures from a webcam (OpenCV + MediaPipe). The player uses `pygame` for audio playback.

**Project structure**
- `main.py` — entry point: captures webcam frames, runs MediaPipe hand detection, maps gestures to the `MusicPlayer`.
- `gesture_controller.py` — logic for counting fingers and detecting simple left/right swipes.
- `music_player.py` — loads and plays `.mp3` files from the `music/` folder using `pygame`.
- `music/` — place your `.mp3` music files here.

**Python version**
This repo includes a `.venv` created with Python 3.14 (see `.venv/pyvenv.cfg`). The project should work with Python 3.9+ but the existing environment was made with Python 3.14.

## Setup (Windows PowerShell)

1. Create a virtual environment (optional if `.venv` already exists):

```powershell
python -m venv .venv
```

2. Activate the virtual environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

3. Upgrade `pip` and install dependencies:

```powershell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

4. Add some `.mp3` files to the `music/` folder.

5. Run the app:

```powershell
python main.py
```

Press `q` in the video window to quit.

## Notes and tips
- If PowerShell blocks activation, temporarily allow the script for the process:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

- If your audio files are large, consider tracking them with Git LFS or excluding them from the repo and providing a download link instead.

- If you prefer a different Python version, create the venv with that interpreter and re-install dependencies.

## Prepare and push to GitHub

Run these commands from the project root to initialize a git repo and push (replace `<your-repo-url>`):

```powershell
git init
git add .
git commit -m "Initial commit: hand-gesture-music-player"
git branch -M main
git remote add origin <your-repo-url>
git push -u origin main
```

If you need, I can initialize the repo locally and help you connect it to a GitHub repository (I will not push without your confirmation and credentials).
