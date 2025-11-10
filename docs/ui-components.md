# UI Components Guide

PyAndroid provides a complete set of UI components for building your app interface.

## TextView

Display text to users.

### Basic Usage

```python
from pyandroid.ui import TextView

text = TextView("my_text", "Hello World")
```

### Styling

```python
# Set text properties
text.set_text("New text")
text.set_text_color("#FF5722")  # Hex color
text.set_text_size(20)          # Font size in px

# Set background
text.set_background_color("#FFFFFF")

# Set size
text.set_size(width=300, height=50)
```

### Example

```python
title = TextView("title", "Welcome!")
title.set_text_color("#2196F3")
title.set_text_size(32)
title.set_background_color("#F5F5F5")
```

## Button

Interactive button for user actions.

### Basic Usage

```python
from pyandroid.ui import Button

def on_click(view):
    print("Button clicked!")

button = Button("my_button", "Click Me")
button.set_on_click_listener(on_click)
```

### Styling

```python
# Colors
button.set_background_color("#4CAF50")
button.set_text_color("#FFFFFF")

# Size
button.set_size(width=200, height=60)

# Text
button.set_text("Submit")
button.set_text_size(18)
```

### Full Example

```python
submit_button = Button("submit", "Submit Form")
submit_button.set_background_color("#2196F3")
submit_button.set_text_color("#FFFFFF")
submit_button.set_text_size(16)
submit_button.set_size(250, 50)
submit_button.set_on_click_listener(lambda v: handle_submit())
```

## EditText

Text input field for user input.

### Basic Usage

```python
from pyandroid.ui import EditText

input_field = EditText("username", hint="Enter username")
```

### Getting/Setting Text

```python
# Set text
input_field.set_text("John")

# Get text
username = input_field.get_text()
print(f"Username: {username}")
```

### Full Example

```python
email_input = EditText("email", hint="Enter your email")
email_input.set_size(300, 40)
email_input.set_background_color("#FFFFFF")

# Later, get the value
def on_submit(view):
    email = email_input.get_text()
    print(f"Email: {email}")
```

## Widget Helper

Create widgets quickly with the Widget class.

```python
from pyandroid.ui import Widget

# Create TextView
text = Widget.create_text_view("id", "Text", width=200, height=50)

# Create Button
button = Widget.create_button(
    "id", 
    "Click",
    on_click=lambda v: print("Clicked!"),
    width=150,
    height=60
)

# Create EditText
input_field = Widget.create_edit_text("id", hint="Enter text")
```

## View Properties

All views inherit these properties:

### Position

```python
view.set_position(x=10, y=20)
```

### Size

```python
view.set_size(width=300, height=100)
```

### Visibility

```python
view.set_visibility(True)   # Show
view.set_visibility(False)  # Hide
```

### Enable/Disable

```python
view.set_enabled(True)   # Enabled
view.set_enabled(False)  # Disabled (grayed out)
```

### Background Color

```python
view.set_background_color("#FF5722")
```

## Color Format

All colors use hex format:

```python
"#FF0000"  # Red
"#00FF00"  # Green
"#0000FF"  # Blue
"#FFFFFF"  # White
"#000000"  # Black
"#2196F3"  # Material Blue
```

## Complete Form Example

```python
from pyandroid import AndroidApp, Activity
from pyandroid.ui import LinearLayout, TextView, EditText, Button

class FormActivity(Activity):
    def __init__(self):
        super().__init__("FormActivity")
    
    def on_start(self):
        layout = LinearLayout("form", orientation="vertical")
        
        # Title
        title = TextView("title", "Sign Up")
        title.set_text_size(28)
        title.set_text_color("#2196F3")
        layout.add_view(title)
        
        # Name input
        self.name_input = EditText("name", hint="Full Name")
        layout.add_view(self.name_input)
        
        # Email input
        self.email_input = EditText("email", hint="Email Address")
        layout.add_view(self.email_input)
        
        # Submit button
        submit_btn = Button("submit", "Sign Up")
        submit_btn.set_background_color("#4CAF50")
        submit_btn.set_on_click_listener(self.on_submit)
        layout.add_view(submit_btn)
        
        self.add_view("form", layout)
    
    def on_submit(self, view):
        name = self.name_input.get_text()
        email = self.email_input.get_text()
        print(f"Name: {name}, Email: {email}")

app = AndroidApp("Form Demo", "com.example.form")
app.register_activity("main", FormActivity)
app.start_activity("main")
app.run()
```

## Next Steps

- [Layouts Guide](layouts.md) - Organize your UI
- [Event Handling](events.md) - Handle user interactions
- [Styling Guide](styling.md) - Make your app beautiful
