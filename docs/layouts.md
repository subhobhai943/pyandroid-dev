# Layouts Guide

Layouts organize and arrange UI components in your PyAndroid app.

## LinearLayout

Arranges children in a single direction (vertical or horizontal).

### Vertical Layout

```python
from pyandroid.ui import LinearLayout, Button

layout = LinearLayout("main", orientation="vertical")

# Add buttons - they stack vertically
layout.add_view(Button("btn1", "Button 1"))
layout.add_view(Button("btn2", "Button 2"))
layout.add_view(Button("btn3", "Button 3"))

# Result:
# [Button 1]
# [Button 2]
# [Button 3]
```

### Horizontal Layout

```python
layout = LinearLayout("main", orientation="horizontal")

# Add buttons - they stack horizontally
layout.add_view(Button("btn1", "Btn 1"))
layout.add_view(Button("btn2", "Btn 2"))
layout.add_view(Button("btn3", "Btn 3"))

# Result:
# [Btn 1] [Btn 2] [Btn 3]
```

## Nested Layouts

Create complex UIs by nesting layouts:

```python
from pyandroid.ui import LinearLayout, TextView, Button

# Main vertical layout
main_layout = LinearLayout("main", orientation="vertical")

# Title
title = TextView("title", "My App")
main_layout.add_view(title)

# Horizontal row of buttons
button_row = LinearLayout("button_row", orientation="horizontal")
button_row.add_view(Button("btn1", "Save"))
button_row.add_view(Button("btn2", "Cancel"))

# Add button row to main layout
main_layout.add_view(button_row)

# Result:
# My App
# [Save] [Cancel]
```

## Layout Properties

### Padding

Add space inside the layout:

```python
layout = LinearLayout("main", orientation="vertical")
layout.set_padding(
    left=10,
    top=20,
    right=10,
    bottom=20
)
```

### Finding Views

Find child views by ID:

```python
layout = LinearLayout("main", orientation="vertical")
button = Button("my_button", "Click")
layout.add_view(button)

# Find it later
found_button = layout.find_view_by_id("my_button")
```

### Removing Views

```python
layout.remove_view(button)
```

## Complete Layout Example

```python
from pyandroid import AndroidApp, Activity
from pyandroid.ui import LinearLayout, TextView, Button, EditText

class CalculatorActivity(Activity):
    def __init__(self):
        super().__init__("CalculatorActivity")
    
    def on_start(self):
        # Main vertical layout
        main = LinearLayout("main", orientation="vertical")
        main.set_padding(10, 10, 10, 10)
        
        # Display area
        self.display = TextView("display", "0")
        self.display.set_text_size(32)
        self.display.set_background_color("#212121")
        self.display.set_text_color("#FFFFFF")
        main.add_view(self.display)
        
        # Button rows
        for row_buttons in [["7", "8", "9"], ["4", "5", "6"], ["1", "2", "3"]]:
            row = LinearLayout(f"row_{row_buttons[0]}", orientation="horizontal")
            
            for btn_text in row_buttons:
                btn = Button(f"btn_{btn_text}", btn_text)
                btn.set_size(80, 80)
                btn.set_on_click_listener(
                    lambda v, t=btn_text: self.on_number_click(t)
                )
                row.add_view(btn)
            
            main.add_view(row)
        
        self.add_view("main", main)
    
    def on_number_click(self, number):
        current = self.display.text
        if current == "0":
            self.display.set_text(number)
        else:
            self.display.set_text(current + number)

app = AndroidApp("Calculator", "com.example.calc")
app.register_activity("main", CalculatorActivity)
app.start_activity("main")
app.run()
```

## RelativeLayout

Position views relative to parent or siblings.

```python
from pyandroid.ui import RelativeLayout, Button

layout = RelativeLayout("main")

# Manually position views
button = Button("btn", "Click")
button.set_position(x=50, y=100)
layout.add_view(button)
```

## Best Practices

### 1. Use Meaningful IDs

```python
# Good
layout = LinearLayout("user_profile_layout", orientation="vertical")
name_text = TextView("user_name_label", "John Doe")

# Bad
layout = LinearLayout("l1", orientation="vertical")
name_text = TextView("tv1", "John Doe")
```

### 2. Keep Nesting Simple

Avoid too many nested layouts (max 3-4 levels):

```python
# Good
main_layout
  ├─ header_row
  │   ├─ title
  │   └─ button
  └─ content_area

# Too complex (avoid)
main_layout
  └─ outer_wrapper
      └─ inner_wrapper
          └─ container
              └─ holder
                  └─ actual_content  # Too deep!
```

### 3. Reuse Layouts

Create helper methods for repeated patterns:

```python
def create_button_row(button_labels):
    row = LinearLayout("row", orientation="horizontal")
    for label in button_labels:
        btn = Button(f"btn_{label}", label)
        row.add_view(btn)
    return row

# Use it
layout.add_view(create_button_row(["Save", "Cancel", "Delete"]))
```

## Next Steps

- [Event Handling](events.md) - Handle user interactions
- [Styling Guide](styling.md) - Customize appearance
- [Examples](../examples/) - See complete apps
