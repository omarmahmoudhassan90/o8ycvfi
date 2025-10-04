# Race Game — Buildable Android Project

This archive contains a Kivy-based Android project (main.py) and a `buildozer.spec` file.
I inserted your Firebase Realtime Database URL into the code:
`https://alrowad-school-ea01c-default-rtdb.firebaseio.com`

## What I prepared for you
- `main.py` — the Kivy app (the original `omar.py`, renamed to `main.py`).
- `buildozer.spec` — a minimal spec configured for building an Android debug APK.
- `build.sh` — helper script to build using Docker (recommended).
- `README.md` — this file.

---

## Option A — Build locally on Ubuntu / WSL (recommended)

1. Install required packages on Ubuntu (WSL or native):
```bash
sudo apt update
sudo apt install -y python3-pip git zip unzip openjdk-11-jdk
pip install --user buildozer cython
# optionally add pip --user bin to PATH: export PATH=$PATH:~/.local/bin
```

2. From the project directory:
```bash
# ensure main.py and buildozer.spec are here
buildozer -v android debug
```

3. APK will appear in `bin/` as `*.apk` (e.g. `bin/racegame-0.1-debug.apk`).

---

## Option B — Build inside Docker (easy, reproducible)

This project works well with the official `kivy/buildozer` Docker image.

From the project directory run:
```bash
docker pull kivy/buildozer
docker run --rm -v "$(pwd)":/home/user/hostcwd -w /home/user/hostcwd kivy/buildozer buildozer -v android debug
```

This will create the APK inside the `bin/` folder.

---

## Notes & Troubleshooting

- The build process downloads Android SDK/NDK and other large tools on first run — it may take a long time (several GB).
- If you want a release-signed APK, you'll need to create a keystore and update `buildozer.spec` with the keystore settings.
- If you want to change the app name, icon, or permissions, edit `buildozer.spec` before building.
- If Firebase multiplayer fails, verify your Realtime Database rules and that the URL matches your project.

If you want, I can also:
- Add a GitHub Actions workflow file or Dockerfile to automate CI builds.
- Produce a signed release APK (requires a keystore from you).