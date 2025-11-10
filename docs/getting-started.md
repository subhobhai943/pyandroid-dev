# Getting Started with PyAndroid

Welcome to PyAndroid! This guide will help you create your first Android application using Python.

## Installation

### Basic Installation

```bash
pip install pyandroid-dev
```

### With GUI Support (Recommended)

```bash
pip install "pyandroid-dev[gui]"
```

This installs Kivy for graphical user interface support.

## Your First App

Let's create a simple "Hello World" app:

```python
from pyandroid import AndroidApp, Activity
from pyandroid.ui import LinearLayout, TextView

class MainActivity(Activity):
    def __init__(self):
        super().__init__("MainActivity")
    
    def on_start(self):
        # Create layout
        layout = LinearLayout("main_layout", orientation="vertical")
        
        # Create text view
        text = TextView("hello", "Hello, PyAndroid!")
        text.set_text_size(24)
        text.set_text_color("#2196F3")
        
        # Add text to layout
        layout.add_view(text)
        
        # Add layout to activity
        self.add_view("main_layout", layout)

# Create and run app
app = AndroidApp("Hello World", "com.example.helloworld")
app.register_activity("main", MainActivity)
app.start_activity("main")
app.run()
```

Save this as `hello_world.py` and run:

```bash
python hello_world.py
```

A window will open with your app! 🎉

## Understanding the Code

### AndroidApp

The main application class:

```python
app = AndroidApp(
    "Hello World",           # App name
    "com.example.helloworld" # Package name (reverse domain)
)
```

### Activity

A screen in your app:

```python
class MainActivity(Activity):
    def on_start(self):
        # Called when activity starts
        # Setup UI here
        pass
```

### Layouts

Containers for organizing views:

```python
layout = LinearLayout("id", orientation="vertical")  # Stack vertically
layout = LinearLayout("id", orientation="horizontal") # Stack horizontally
```

### Views

UI components:

```python
text = TextView("id", "Text content")
button = Button("id", "Click Me")
input_field = EditText("id", hint="Enter text")
```

## Adding Interactivity

Let's add a button that responds to clicks:

```python
from pyandroid import AndroidApp, Activity
from pyandroid.ui import LinearLayout, TextView, Button

class MainActivity(Activity):
    def __init__(self):
        super().__init__("MainActivity")
        self.click_count = 0
    
    def on_start(self):
        layout = LinearLayout("main", orientation="vertical")
        
        # Counter display
        self.counter_text = TextView("counter", "Clicks: 0")
        self.counter_text.set_text_size(28)
        layout.add_view(self.counter_text)
        
        # Button
        button = Button("click_btn", "Click Me!")
        button.set_background_color("#4CAF50")
        button.set_on_click_listener(self.on_button_click)
        layout.add_view(button)
        
        self.add_view("main", layout)
    
    def on_button_click(self, view):
        self.click_count += 1
        self.counter_text.set_text(f"Clicks: {self.click_count}")

app = AndroidApp("Click Counter", "com.example.counter")
app.register_activity("main", MainActivity)
app.start_activity("main")
app.run()
```

## Next Steps

- [UI Components Guide](ui-components.md) - Learn about all available widgets
- [Layouts Guide](layouts.md) - Master different layout types
- [Building APK](building-apk.md) - Deploy to Android devices
- [Examples](../examples/) - See complete example apps

## Need Help?

- [GitHub Issues](https://github.com/subhobhai943/pyandroid-dev/issues)
- [Discussions](https://github.com/subhobhai943/pyandroid-dev/discussions)
- [API Reference](api-reference.md)
