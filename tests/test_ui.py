"""Tests for PyAndroid UI components."""

import pytest
from pyandroid.ui import TextView, Button, EditText, LinearLayout, Widget


class TestTextView:
    """Test cases for TextView class."""
    
    def test_textview_creation(self):
        """Test creating a text view."""
        tv = TextView("test_tv", "Hello World")
        assert tv.view_id == "test_tv"
        assert tv.text == "Hello World"
    
    def test_textview_styling(self):
        """Test text view styling."""
        tv = TextView("test_tv", "Test")
        tv.set_text_color("#FF0000")
        tv.set_text_size(20)
        
        assert tv.text_color == "#FF0000"
        assert tv.text_size == 20
    
    def test_textview_render(self):
        """Test rendering text view."""
        tv = TextView("test_tv", "Test")
        rendered = tv.render()
        
        assert rendered["type"] == "TextView"
        assert rendered["id"] == "test_tv"
        assert rendered["text"] == "Test"


class TestButton:
    """Test cases for Button class."""
    
    def test_button_creation(self):
        """Test creating a button."""
        btn = Button("test_btn", "Click Me")
        assert btn.view_id == "test_btn"
        assert btn.text == "Click Me"
    
    def test_button_click(self):
        """Test button click event."""
        clicked = []
        
        def on_click(view):
            clicked.append(True)
        
        btn = Button("test_btn", "Click")
        btn.set_on_click_listener(on_click)
        btn.on_click()
        
        assert len(clicked) == 1


class TestEditText:
    """Test cases for EditText class."""
    
    def test_edittext_creation(self):
        """Test creating edit text."""
        et = EditText("test_et", hint="Enter text")
        assert et.view_id == "test_et"
        assert et.hint == "Enter text"
    
    def test_edittext_text(self):
        """Test setting and getting text."""
        et = EditText("test_et")
        et.set_text("Hello")
        assert et.get_text() == "Hello"


class TestLinearLayout:
    """Test cases for LinearLayout class."""
    
    def test_layout_creation(self):
        """Test creating a layout."""
        layout = LinearLayout("test_layout", orientation="vertical")
        assert layout.layout_id == "test_layout"
        assert layout.orientation == "vertical"
    
    def test_add_remove_view(self):
        """Test adding and removing views."""
        layout = LinearLayout("test_layout")
        view = TextView("test_tv", "Test")
        
        layout.add_view(view)
        assert len(layout.children) == 1
        
        layout.remove_view(view)
        assert len(layout.children) == 0
    
    def test_find_view_by_id(self):
        """Test finding view by ID."""
        layout = LinearLayout("test_layout")
        view = TextView("test_tv", "Test")
        layout.add_view(view)
        
        found = layout.find_view_by_id("test_tv")
        assert found == view


class TestWidget:
    """Test cases for Widget helper class."""
    
    def test_create_text_view(self):
        """Test creating text view via Widget."""
        tv = Widget.create_text_view("test", "Text")
        assert isinstance(tv, TextView)
    
    def test_create_button(self):
        """Test creating button via Widget."""
        btn = Widget.create_button("test", "Button")
        assert isinstance(btn, Button)
    
    def test_create_edit_text(self):
        """Test creating edit text via Widget."""
        et = Widget.create_edit_text("test", "Hint")
        assert isinstance(et, EditText)
