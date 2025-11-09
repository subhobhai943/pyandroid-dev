"""Tests for core PyAndroid components."""

import pytest
from pyandroid.core import AndroidApp, Activity, Intent


class TestAndroidApp:
    """Test cases for AndroidApp class."""
    
    def test_app_creation(self):
        """Test creating an Android app."""
        app = AndroidApp("TestApp", "com.test.app", use_gui=False)
        assert app.app_name == "TestApp"
        assert app.package_name == "com.test.app"
        assert app.use_gui is False
    
    def test_register_activity(self):
        """Test registering an activity."""
        app = AndroidApp("TestApp", "com.test.app", use_gui=False)
        
        class TestActivity(Activity):
            pass
        
        app.register_activity("test", TestActivity)
        assert "test" in app.activities
    
    def test_start_activity(self):
        """Test starting an activity."""
        app = AndroidApp("TestApp", "com.test.app", use_gui=False)
        
        class TestActivity(Activity):
            pass
        
        app.register_activity("test", TestActivity)
        app.start_activity("test")
        assert app.current_activity is not None
        assert app.current_activity.state == "started"


class TestActivity:
    """Test cases for Activity class."""
    
    def test_activity_creation(self):
        """Test creating an activity."""
        activity = Activity("TestActivity")
        assert activity.name == "TestActivity"
        assert activity.state == "created"
    
    def test_activity_lifecycle(self):
        """Test activity lifecycle methods."""
        activity = Activity("TestActivity")
        
        activity.start()
        assert activity.state == "started"
        
        activity.resume()
        assert activity.state == "resumed"
        
        activity.pause()
        assert activity.state == "paused"
        
        activity.stop()
        assert activity.state == "stopped"
        
        activity.destroy()
        assert activity.state == "destroyed"
    
    def test_add_view(self):
        """Test adding views to activity."""
        from pyandroid.ui import TextView
        
        activity = Activity("TestActivity")
        view = TextView("test_view", "Test")
        
        activity.add_view("test_view", view)
        assert activity.get_view("test_view") == view


class TestIntent:
    """Test cases for Intent class."""
    
    def test_intent_creation(self):
        """Test creating an intent."""
        intent = Intent("ACTION_VIEW", "MainActivity")
        assert intent.action == "ACTION_VIEW"
        assert intent.target == "MainActivity"
    
    def test_intent_extras(self):
        """Test intent extras."""
        intent = Intent("ACTION_VIEW")
        intent.put_extra("key1", "value1")
        intent.put_extra("key2", 123)
        
        assert intent.get_extra("key1") == "value1"
        assert intent.get_extra("key2") == 123
        assert intent.get_extra("nonexistent", "default") == "default"
