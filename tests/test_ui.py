"""Tests for PyAndroid UI components."""

import pytest
from pyandroid.ui import TextView, Button, EditText, LinearLayout, RelativeLayout, Widget


@pytest.fixture
def text_view():
    """Create a test TextView instance."""
    return TextView("test_tv", "Hello World")


@pytest.fixture
def button():
    """Create a test Button instance."""
    return Button("test_btn", "Click Me")


@pytest.fixture
def edit_text():
    """Create a test EditText instance."""
    return EditText("test_et", hint="Enter text")


@pytest.fixture
def linear_layout():
    """Create a test LinearLayout instance."""
    return LinearLayout("test_layout", orientation="vertical")


class TestTextView:
    """Test cases for TextView class."""
    
    def test_textview_creation(self, text_view):
        """Test creating a text view."""
        assert text_view.view_id == "test_tv"
        assert text_view.text == "Hello World"
    
    def test_textview_set_text(self, text_view):
        """Test setting text on TextView."""
        text_view.set_text("New Text")
        assert text_view.text == "New Text"
    
    def test_textview_styling(self, text_view):
        """Test text view styling."""
        text_view.set_text_color("#FF0000")
        text_view.set_text_size(20)
        
        assert text_view.text_color == "#FF0000"
        assert text_view.text_size == 20
    
    def test_textview_render(self, text_view):
        """Test rendering text view."""
        rendered = text_view.render()
        
        assert rendered["type"] == "TextView"
        assert rendered["id"] == "test_tv"
        assert rendered["text"] == "Hello World"
        assert "position" in rendered
        assert "size" in rendered
    
    def test_textview_visibility(self, text_view):
        """Test TextView visibility controls."""
        assert text_view.visible is True
        text_view.set_visibility(False)
        assert text_view.visible is False
    
    def test_textview_position(self, text_view):
        """Test setting TextView position."""
        text_view.set_position(100, 200)
        assert text_view.x == 100
        assert text_view.y == 200
    
    def test_textview_size(self, text_view):
        """Test setting TextView size."""
        text_view.set_size(300, 50)
        assert text_view.width == 300
        assert text_view.height == 50


class TestButton:
    """Test cases for Button class."""
    
    def test_button_creation(self, button):
        """Test creating a button."""
        assert button.view_id == "test_btn"
        assert button.text == "Click Me"
    
    def test_button_default_colors(self, button):
        """Test button has default colors."""
        assert button.background_color == "#2196F3"
        assert button.text_color == "#FFFFFF"
    
    def test_button_click(self):
        """Test button click event."""
        clicked = []
        
        def on_click(view):
            clicked.append(view.view_id)
        
        btn = Button("test_btn", "Click")
        btn.set_on_click_listener(on_click)
        btn.on_click()
        
        assert len(clicked) == 1
        assert clicked[0] == "test_btn"
    
    def test_button_disabled_click(self, button):
        """Test that disabled button doesn't trigger click."""
        clicked = []
        
        def on_click(view):
            clicked.append(True)
        
        button.set_on_click_listener(on_click)
        button.set_enabled(False)
        button.on_click()
        
        assert len(clicked) == 0
    
    def test_button_render(self, button):
        """Test rendering button."""
        rendered = button.render()
        
        assert rendered["type"] == "Button"
        assert rendered["id"] == "test_btn"
        assert rendered["text"] == "Click Me"


class TestEditText:
    """Test cases for EditText class."""
    
    def test_edittext_creation(self, edit_text):
        """Test creating edit text."""
        assert edit_text.view_id == "test_et"
        assert edit_text.hint == "Enter text"
        assert edit_text.text == ""
    
    def test_edittext_text(self, edit_text):
        """Test setting and getting text."""
        edit_text.set_text("Hello")
        assert edit_text.get_text() == "Hello"
    
    def test_edittext_empty(self):
        """Test EditText without hint."""
        et = EditText("test_et")
        assert et.hint == ""
        assert et.text == ""
    
    def test_edittext_render(self, edit_text):
        """Test rendering EditText."""
        edit_text.set_text("Test input")
        rendered = edit_text.render()
        
        assert rendered["type"] == "EditText"
        assert rendered["id"] == "test_et"
        assert rendered["text"] == "Test input"
        assert rendered["hint"] == "Enter text"


class TestLinearLayout:
    """Test cases for LinearLayout class."""
    
    def test_layout_creation(self, linear_layout):
        """Test creating a layout."""
        assert linear_layout.layout_id == "test_layout"
        assert linear_layout.orientation == "vertical"
    
    def test_layout_horizontal(self):
        """Test creating horizontal layout."""
        layout = LinearLayout("test", orientation="horizontal")
        assert layout.orientation == "horizontal"
    
    def test_add_remove_view(self, linear_layout):
        """Test adding and removing views."""
        view = TextView("test_tv", "Test")
        
        linear_layout.add_view(view)
        assert len(linear_layout.children) == 1
        
        linear_layout.remove_view(view)
        assert len(linear_layout.children) == 0
    
    def test_add_multiple_views(self, linear_layout):
        """Test adding multiple views."""
        view1 = TextView("tv1", "Text 1")
        view2 = Button("btn1", "Button 1")
        view3 = EditText("et1", "Hint")
        
        linear_layout.add_view(view1)
        linear_layout.add_view(view2)
        linear_layout.add_view(view3)
        
        assert len(linear_layout.children) == 3
    
    def test_find_view_by_id(self, linear_layout):
        """Test finding view by ID."""
        view = TextView("test_tv", "Test")
        linear_layout.add_view(view)
        
        found = linear_layout.find_view_by_id("test_tv")
        assert found == view
    
    def test_find_nonexistent_view(self, linear_layout):
        """Test finding view that doesn't exist."""
        found = linear_layout.find_view_by_id("nonexistent")
        assert found is None
    
    def test_set_padding(self, linear_layout):
        """Test setting layout padding."""
        linear_layout.set_padding(10, 20, 30, 40)
        
        assert linear_layout.padding["left"] == 10
        assert linear_layout.padding["top"] == 20
        assert linear_layout.padding["right"] == 30
        assert linear_layout.padding["bottom"] == 40
    
    def test_layout_render(self, linear_layout):
        """Test rendering layout with children."""
        view1 = TextView("tv1", "Text 1")
        view2 = Button("btn1", "Button 1")
        
        linear_layout.add_view(view1)
        linear_layout.add_view(view2)
        
        rendered = linear_layout.render()
        
        assert rendered["type"] == "LinearLayout"
        assert rendered["id"] == "test_layout"
        assert len(rendered["children"]) == 2
        assert rendered["children"][0]["type"] == "TextView"
        assert rendered["children"][1]["type"] == "Button"
    
    def test_vertical_arrangement(self, linear_layout):
        """Test that vertical layout arranges children vertically."""
        view1 = TextView("tv1", "Text 1")
        view2 = TextView("tv2", "Text 2")
        
        view1.set_size(100, 50)
        view2.set_size(100, 50)
        
        linear_layout.add_view(view1)
        linear_layout.add_view(view2)
        
        linear_layout.arrange_children()
        
        # Second view should be positioned below first view
        assert view2.y > view1.y
        assert view1.x == view2.x  # Same x position in vertical layout


class TestRelativeLayout:
    """Test cases for RelativeLayout class."""
    
    def test_relative_layout_creation(self):
        """Test creating a relative layout."""
        layout = RelativeLayout("test_layout")
        assert layout.layout_id == "test_layout"
    
    def test_relative_layout_render(self):
        """Test rendering relative layout."""
        layout = RelativeLayout("test_layout")
        view = TextView("tv1", "Test")
        layout.add_view(view)
        
        rendered = layout.render()
        assert rendered["type"] == "RelativeLayout"
        assert len(rendered["children"]) == 1


class TestWidget:
    """Test cases for Widget helper class."""
    
    def test_create_text_view(self):
        """Test creating text view via Widget."""
        tv = Widget.create_text_view("test", "Text")
        assert isinstance(tv, TextView)
        assert tv.view_id == "test"
        assert tv.text == "Text"
    
    def test_create_button(self):
        """Test creating button via Widget."""
        btn = Widget.create_button("test", "Button")
        assert isinstance(btn, Button)
        assert btn.view_id == "test"
        assert btn.text == "Button"
    
    def test_create_button_with_callback(self):
        """Test creating button with click callback."""
        clicked = []
        
        def on_click(view):
            clicked.append(True)
        
        btn = Widget.create_button("test", "Button", on_click=on_click)
        btn.on_click()
        
        assert len(clicked) == 1
    
    def test_create_edit_text(self):
        """Test creating edit text via Widget."""
        et = Widget.create_edit_text("test", "Hint")
        assert isinstance(et, EditText)
        assert et.view_id == "test"
        assert et.hint == "Hint"
