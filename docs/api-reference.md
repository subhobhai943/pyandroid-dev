# API Reference

Complete API documentation for PyAndroid library.

## Core Module

### AndroidApp

Main application class.

```python
from pyandroid import AndroidApp

app = AndroidApp(app_name: str, package_name: str, use_gui: bool = True)
```

**Parameters:**
- `app_name` (str): Human-readable application name
- `package_name` (str): Reverse domain package name (e.g., "com.example.app")
- `use_gui` (bool): Enable GUI rendering with Kivy (default: True)

**Methods:**

#### register_activity(name, activity_class)
Register an activity with the application.

```python
app.register_activity("main", MainActivity)
```

#### start_activity(name, **kwargs)
Start a registered activity.

```python
app.start_activity("main", user_id=123)
```

#### run()
Start the application.

```python
app.run()
```

### Activity

Base class for application screens.

```python
from pyandroid import Activity

class MyActivity(Activity):
    def __init__(self):
        super().__init__("MyActivity")
```

**Lifecycle Methods:**

```python
def on_start(self):
    """Called when activity starts"""
    pass

def on_resume(self):
    """Called when activity resumes"""
    pass

def on_pause(self):
    """Called when activity pauses"""
    pass

def on_stop(self):
    """Called when activity stops"""
    pass

def on_destroy(self):
    """Called when activity is destroyed"""
    pass
```

**Methods:**

#### add_view(view_id, view)
Add a view to the activity.

```python
self.add_view("main_layout", layout)
```

#### get_view(view_id)
Get a view by ID.

```python
view = self.get_view("main_layout")
```

### Intent

Inter-component communication.

```python
from pyandroid import Intent

intent = Intent(action: str, target: str = None)
```

**Methods:**

```python
intent.put_extra("key", "value")
value = intent.get_extra("key", default="default_value")
```

## UI Module

### View

Base class for all UI components.

**Properties:**
- `view_id` (str): Unique identifier
- `width` (int): Width in pixels
- `height` (int): Height in pixels
- `x` (int): X coordinate
- `y` (int): Y coordinate
- `visible` (bool): Visibility state
- `enabled` (bool): Enabled state
- `background_color` (str): Background color (hex)

**Methods:**

```python
view.set_position(x: int, y: int)
view.set_size(width: int, height: int)
view.set_visibility(visible: bool)
view.set_enabled(enabled: bool)
view.set_background_color(color: str)
view.set_on_click_listener(callback: callable)
```

### TextView

Text display component.

```python
from pyandroid.ui import TextView

text = TextView(view_id: str, text: str = "", **kwargs)
```

**Properties:**
- `text` (str): Text content
- `text_color` (str): Text color (hex)
- `text_size` (int): Font size in pixels
- `font_family` (str): Font family name

**Methods:**

```python
text.set_text(text: str)
text.set_text_color(color: str)
text.set_text_size(size: int)
```

### Button

Interactive button component.

```python
from pyandroid.ui import Button

button = Button(view_id: str, text: str = "Button", **kwargs)
```

Inherits all TextView methods plus button-specific styling.

### EditText

Text input component.

```python
from pyandroid.ui import EditText

input_field = EditText(view_id: str, hint: str = "", **kwargs)
```

**Properties:**
- `text` (str): Current input text
- `hint` (str): Placeholder text
- `text_color` (str): Text color
- `hint_color` (str): Hint color

**Methods:**

```python
input_field.set_text(text: str)
text = input_field.get_text() -> str
```

### LinearLayout

Linear arrangement of children.

```python
from pyandroid.ui import LinearLayout

layout = LinearLayout(layout_id: str, orientation: str = "vertical")
```

**Parameters:**
- `orientation`: "vertical" or "horizontal"

**Methods:**

```python
layout.add_view(view: View)
layout.remove_view(view: View)
view = layout.find_view_by_id(view_id: str) -> View
layout.set_padding(left: int, top: int, right: int, bottom: int)
```

### RelativeLayout

Relative positioning of children.

```python
from pyandroid.ui import RelativeLayout

layout = RelativeLayout(layout_id: str)
```

Same methods as LinearLayout.

### Widget Helper

Factory methods for quick widget creation.

```python
from pyandroid.ui import Widget

# Create TextView
text = Widget.create_text_view(
    view_id: str,
    text: str,
    **kwargs
) -> TextView

# Create Button
button = Widget.create_button(
    view_id: str,
    text: str,
    on_click: callable = None,
    **kwargs
) -> Button

# Create EditText
input_field = Widget.create_edit_text(
    view_id: str,
    hint: str = "",
    **kwargs
) -> EditText
```

## Utils Module

### Logger

Application logging.

```python
from pyandroid.utils import Logger

logger = Logger(app_name: str)
```

**Methods:**

```python
logger.debug(message: str, **kwargs)
logger.info(message: str, **kwargs)
logger.warning(message: str, **kwargs)
logger.error(message: str, **kwargs)
```

### FileManager

File operations.

```python
from pyandroid.utils import FileManager

fm = FileManager(app_name: str)
```

**Methods:**

```python
# Text files
fm.write_file(filename: str, content: str)
content = fm.read_file(filename: str) -> str

# JSON files
fm.save_json(filename: str, data: dict)
data = fm.load_json(filename: str) -> dict

# List files
files = fm.list_files() -> list
```

### NetworkManager

HTTP requests.

```python
from pyandroid.utils import NetworkManager

net = NetworkManager(app_name: str)
```

**Methods:**

```python
# Check connectivity
connected = net.is_connected() -> bool

# HTTP GET
response = net.get(url: str, headers: dict = None)

# HTTP POST
response = net.post(url: str, data: dict, headers: dict = None)

# HTTP POST with JSON
response = net.post_json(url: str, data: dict, headers: dict = None)
```

## Constants

### Colors

Common color constants:

```python
from pyandroid.ui import Colors

Colors.RED = "#FF0000"
Colors.GREEN = "#00FF00"
Colors.BLUE = "#0000FF"
Colors.WHITE = "#FFFFFF"
Colors.BLACK = "#000000"
```

## Examples

### Complete Application

```python
from pyandroid import AndroidApp, Activity
from pyandroid.ui import LinearLayout, TextView, Button, EditText
from pyandroid.utils import Logger

class MainActivity(Activity):
    def __init__(self):
        super().__init__("MainActivity")
        self.logger = Logger("MyApp")
    
    def on_start(self):
        self.logger.info("Activity started")
        
        layout = LinearLayout("main", orientation="vertical")
        
        title = TextView("title", "Welcome")
        title.set_text_size(24)
        layout.add_view(title)
        
        self.input_field = EditText("input", hint="Enter name")
        layout.add_view(self.input_field)
        
        button = Button("submit", "Submit")
        button.set_on_click_listener(self.on_submit)
        layout.add_view(button)
        
        self.add_view("main", layout)
    
    def on_submit(self, view):
        name = self.input_field.get_text()
        self.logger.info(f"Submitted: {name}")

if __name__ == "__main__":
    app = AndroidApp("My App", "com.example.app")
    app.register_activity("main", MainActivity)
    app.start_activity("main")
    app.run()
```

## Version

```python
import pyandroid
print(pyandroid.__version__)  # "1.2.1"
```
