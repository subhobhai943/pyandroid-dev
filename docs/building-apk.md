# Building Android APK

Learn how to convert your PyAndroid app into an Android APK file that can be installed on devices.

## Prerequisites

- Your PyAndroid app working on desktop
- Linux or WSL (Windows Subsystem for Linux)
- Python 3.7+
- At least 8GB free disk space

## Method 1: Using Buildozer (Recommended)

### Step 1: Install Buildozer

```bash
# Install system dependencies (Ubuntu/Debian)
sudo apt update
sudo apt install -y git zip unzip openjdk-17-jdk python3-pip \
    autoconf libtool pkg-config zlib1g-dev libncurses5-dev \
    libncursesw5-dev libtinfo5 cmake libffi-dev libssl-dev

# Install Buildozer
pip3 install --user buildozer

# Install Cython
pip3 install --user Cython==0.29.33
```

### Step 2: Initialize Buildozer

In your project directory:

```bash
buildozer init
```

This creates `buildozer.spec` configuration file.

### Step 3: Configure buildozer.spec

Edit the file:

```ini
[app]
# App name shown on device
title = My PyAndroid App

# Package name (reverse domain)
package.name = myapp
package.domain = com.example

# Your main Python file
source.dir = .
source.include_exts = py,png,jpg,kv,atlas

# Version
version = 0.1

# Required packages
requirements = python3,kivy,pyandroid-dev

# Permissions (if needed)
android.permissions = INTERNET

# Orientation
orientation = portrait

# Icon (optional)
# icon.filename = %(source.dir)s/icon.png
```

### Step 4: Build APK

```bash
# Build debug APK (first time takes 30-60 minutes)
buildozer -v android debug

# APK will be in: bin/myapp-0.1-debug.apk
```

### Step 5: Install on Device

#### Via USB:

```bash
# Enable USB Debugging on your Android device
# Settings > Developer Options > USB Debugging

# Connect device
adb devices

# Install APK
buildozer android debug deploy run
```

#### Via File Transfer:

1. Copy `bin/myapp-0.1-debug.apk` to your phone
2. Open file manager on phone
3. Tap the APK file
4. Allow installation from unknown sources
5. Install

## Method 2: Using python-for-android

### Install

```bash
pip install python-for-android
```

### Build APK

```bash
p4a apk --private . \
    --package=com.example.myapp \
    --name "My App" \
    --version 0.1 \
    --bootstrap=sdl2 \
    --requirements=python3,kivy,pyandroid-dev \
    --permission INTERNET \
    --arch=arm64-v8a \
    --arch=armeabi-v7a
```

## Complete Project Structure

```
my-app/
├── main.py              # Your PyAndroid app
├── buildozer.spec       # Buildozer config
├── requirements.txt     # Python dependencies
├── icon.png            # App icon (optional)
└── assets/             # Images, files (optional)
    └── logo.png
```

### main.py Example

```python
from pyandroid import AndroidApp, Activity
from pyandroid.ui import LinearLayout, TextView, Button

class MainActivity(Activity):
    def __init__(self):
        super().__init__("MainActivity")
    
    def on_start(self):
        layout = LinearLayout("main", orientation="vertical")
        
        text = TextView("title", "Hello Android!")
        text.set_text_size(24)
        layout.add_view(text)
        
        button = Button("btn", "Click Me")
        button.set_on_click_listener(
            lambda v: print("Button clicked!")
        )
        layout.add_view(button)
        
        self.add_view("main", layout)

if __name__ == "__main__":
    app = AndroidApp("My App", "com.example.myapp")
    app.register_activity("main", MainActivity)
    app.start_activity("main")
    app.run()
```

### requirements.txt

```txt
pyandroid-dev[gui]
kivy>=2.0.0
```

## Building Release APK

For Google Play Store:

### 1. Create Keystore

```bash
keytool -genkey -v -keystore my-release-key.keystore \
    -alias my-key-alias -keyalg RSA -keysize 2048 \
    -validity 10000
```

### 2. Configure buildozer.spec

```ini
[app]
# ... other settings ...

android.release_artifact = aab  # For Play Store

# Signing
android.keystore = my-release-key.keystore
android.keystore_alias = my-key-alias
```

### 3. Build Release

```bash
buildozer android release
```

## Troubleshooting

### Build Fails

```bash
# Clean build
buildozer android clean

# Retry
buildozer -v android debug
```

### APK Crashes on Launch

1. Check logs:
```bash
adb logcat | grep python
```

2. Common issues:
   - Missing permissions in buildozer.spec
   - Wrong Python version in requirements
   - Missing dependencies

### App Too Large

```ini
# In buildozer.spec, remove unused architectures
android.archs = arm64-v8a  # Only 64-bit
```

## Best Practices

### 1. Test on Desktop First

Always test your app on desktop before building APK:

```bash
python main.py
```

### 2. Use Version Control

```bash
git add .
git commit -m "Version 1.0 ready for APK build"
```

### 3. Optimize Resources

- Compress images
- Remove unused files
- Keep dependencies minimal

### 4. Test on Multiple Devices

Test your APK on:
- Different Android versions
- Different screen sizes
- Different device manufacturers

## Publishing to Play Store

1. Build release AAB:
```bash
buildozer android release
```

2. Create Play Console account
3. Upload AAB file
4. Fill in store listing
5. Set pricing and distribution
6. Submit for review

## Resources

- [Buildozer Documentation](https://buildozer.readthedocs.io/)
- [python-for-android](https://python-for-android.readthedocs.io/)
- [Kivy Documentation](https://kivy.org/doc/stable/)
- [Android Developer Guide](https://developer.android.com/)

## Next Steps

- [Distribution Guide](distribution.md)
- [App Store Guidelines](play-store.md)
- [Performance Optimization](optimization.md)
