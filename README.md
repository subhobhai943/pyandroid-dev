# PyAndroid - Python Library for Android Development

A comprehensive Python library for Android application development with cross-platform capabilities. PyAndroid provides a Pythonic interface for building Android applications using familiar Python patterns and paradigms.

## Features

- **Core Android Components**: Activities, Intents, and Application lifecycle management
- **UI Framework**: Complete UI system with Views, Layouts, and Widgets
- **Utility Classes**: Built-in logging, file management, and networking capabilities
- **Cross-Platform**: Write once, deploy across multiple Android versions
- **Pythonic API**: Familiar Python syntax and patterns
- **Extensible**: Easy to extend with custom components and functionality

## Installation

```bash
pip install pyandroid-dev
```

## Quick Start

### Basic Application

```python
from pyandroid import AndroidApp, Activity
from pyandroid.ui import LinearLayout, Widget

class MainActivity(Activity):
    def __init__(self):
        super().__init__("MainActivity")
        
    def on_start(self):
        # Create UI layout
        layout = LinearLayout("main_layout", orientation="vertical")
        
        # Add text view
        text_view = Widget.create_text_view(
            "welcome_text", 
            "Welcome to PyAndroid!",
            width=300, 
            height=50
        )
        
        # Add button with click handler
        def on_button_click(view):
            print("Button clicked!")
            
        button = Widget.create_button(
            "click_button", 
            "Click Me",
            on_click=on_button_click,
            width=200,
            height=60
        )
        
        layout.add_view(text_view)
        layout.add_view(button)
        
        # Add layout to activity
        self.add_view("main_layout", layout)

# Create and run application
app = AndroidApp("MyApp", "com.example.myapp")
app.register_activity("main", MainActivity)
app.start_activity("main")
app.run()
```

### UI Components

```python
from pyandroid.ui import TextView, Button, EditText, LinearLayout

# Create text view
text_view = TextView("title", "Hello Android!")
text_view.set_text_color("#FF0000")
text_view.set_text_size(18)

# Create button
button = Button("submit_btn", "Submit")
button.set_background_color("#2196F3")
button.set_on_click_listener(lambda v: print("Submitted!"))

# Create input field
edit_text = EditText("user_input", hint="Enter your name")

# Create layout and add views
layout = LinearLayout("form_layout")
layout.add_view(text_view)
layout.add_view(edit_text)
layout.add_view(button)
```

### File Management

```python
from pyandroid.utils import FileManager

file_manager = FileManager("MyApp")

# Save data
data = {"user": "John", "score": 100}
file_manager.save_json("game_data.json", data)

# Load data
loaded_data = file_manager.load_json("game_data.json")
print(loaded_data)  # {'user': 'John', 'score': 100}

# Write text file
file_manager.write_file("log.txt", "Application started\n")
```

### Networking

```python
from pyandroid.utils import NetworkManager

network = NetworkManager("MyApp")

# Check connectivity
if network.is_connected():
    # Make GET request
    response = network.get("https://api.example.com/data")
    
    # Make POST request with JSON
    data = {"name": "John", "age": 30}
    result = network.post_json("https://api.example.com/users", data)
    print(result)
```

## Architecture

PyAndroid follows Android's architecture patterns:

- **AndroidApp**: Main application class managing lifecycle
- **Activity**: Individual screens/views in your application
- **Intent**: Communication between components
- **Views**: UI components (TextView, Button, EditText, etc.)
- **Layouts**: Container for organizing views (LinearLayout, RelativeLayout)
- **Utils**: Helper classes for common tasks

## API Reference

### Core Classes

#### AndroidApp
- `register_activity(name, activity_class)`: Register an activity
- `start_activity(name, **kwargs)`: Start an activity
- `run()`: Run the application

#### Activity
- `on_start()`: Override for activity start logic
- `on_resume()`: Override for activity resume logic
- `on_pause()`: Override for activity pause logic
- `add_view(id, view)`: Add view to activity
- `get_view(id)`: Get view by ID

#### Intent
- `put_extra(key, value)`: Add data to intent
- `get_extra(key, default)`: Get data from intent

### UI Classes

#### View (Base Class)
- `set_position(x, y)`: Set view position
- `set_size(width, height)`: Set view dimensions
- `set_visibility(visible)`: Show/hide view
- `set_background_color(color)`: Set background color
- `set_on_click_listener(callback)`: Set click handler

#### TextView
- `set_text(text)`: Set text content
- `set_text_color(color)`: Set text color
- `set_text_size(size)`: Set font size

#### Button (extends TextView)
- All TextView methods plus button-specific styling

#### EditText
- `set_text(text)`: Set input text
- `get_text()`: Get current text

#### Layouts
- `add_view(view)`: Add child view
- `remove_view(view)`: Remove child view
- `find_view_by_id(id)`: Find child by ID

### Utility Classes

#### Logger
- `debug(message, **kwargs)`: Log debug message
- `info(message, **kwargs)`: Log info message
- `warning(message, **kwargs)`: Log warning
- `error(message, **kwargs)`: Log error

#### FileManager
- `write_file(filename, content)`: Write text file
- `read_file(filename)`: Read text file
- `save_json(filename, data)`: Save JSON data
- `load_json(filename)`: Load JSON data
- `list_files()`: List files in directory

#### NetworkManager
- `get(url, headers)`: HTTP GET request
- `post(url, data, headers)`: HTTP POST request
- `post_json(url, data, headers)`: POST with JSON
- `is_connected()`: Check connectivity

## Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Roadmap

- [ ] WebView component
- [ ] Database integration (SQLite)
- [ ] Push notification support
- [ ] Camera and media access
- [ ] Sensor integration
- [ ] Background service support
- [ ] Testing framework
- [ ] Documentation improvements

## Support

If you have questions or need help:

- Open an [Issue](https://github.com/subhobhai943/pyandroid-dev/issues)
- Check the [Wiki](https://github.com/subhobhai943/pyandroid-dev/wiki)
- Join our community discussions

## Changelog

### v1.0.0 (2024-10-24)
- Initial release
- Core Android components (App, Activity, Intent)
- Complete UI framework (Views, Layouts, Widgets)
- Utility classes (Logger, FileManager, NetworkManager)
- Comprehensive documentation and examples
