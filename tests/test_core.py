"""Tests for core PyAndroid components."""

import pytest
from pyandroid.core import (
    AndroidApp, 
    Activity, 
    Intent,
    ActivityNotFoundError,
    InvalidStateError
)
from pyandroid.ui import TextView


@pytest.fixture
def test_app():
    """Create a test app instance."""
    return AndroidApp("TestApp", "com.test.app", use_gui=False)


@pytest.fixture
def test_activity():
    """Create a test activity instance."""
    return Activity("TestActivity")


class TestAndroidApp:
    """Test cases for AndroidApp class."""
    
    def test_app_creation(self, test_app):
        """Test creating an Android app."""
        assert test_app.app_name == "TestApp"
        assert test_app.package_name == "com.test.app"
        assert test_app.use_gui is False
    
    def test_app_creation_with_gui_disabled(self):
        """Test app creation with GUI disabled (should not fail)."""
        app = AndroidApp("TestApp", "com.test.app", use_gui=False)
        assert app.renderer is None
    
    def test_register_activity(self, test_app):
        """Test registering an activity."""
        class TestActivity(Activity):
            pass
        
        test_app.register_activity("test", TestActivity)
        assert "test" in test_app.activities
    
    def test_start_activity(self, test_app):
        """Test starting an activity."""
        class TestActivity(Activity):
            pass
        
        test_app.register_activity("test", TestActivity)
        test_app.start_activity("test")
        assert test_app.current_activity is not None
        assert test_app.current_activity.state == "started"
    
    def test_start_unregistered_activity(self, test_app):
        """Test that starting an unregistered activity raises error."""
        with pytest.raises(ActivityNotFoundError) as exc_info:
            test_app.start_activity("nonexistent")
        assert "not registered" in str(exc_info.value)
    
    def test_activity_switching(self, test_app):
        """Test switching between activities."""
        class Activity1(Activity):
            pass
        
        class Activity2(Activity):
            pass
        
        test_app.register_activity("activity1", Activity1)
        test_app.register_activity("activity2", Activity2)
        
        test_app.start_activity("activity1")
        first_activity = test_app.current_activity
        
        test_app.start_activity("activity2")
        second_activity = test_app.current_activity
        
        assert first_activity.state == "destroyed"
        assert second_activity.state == "started"
        assert first_activity != second_activity


class TestActivity:
    """Test cases for Activity class."""
    
    def test_activity_creation(self, test_activity):
        """Test creating an activity."""
        assert test_activity.name == "TestActivity"
        assert test_activity.state == "created"
    
    def test_activity_lifecycle(self, test_activity):
        """Test activity lifecycle methods."""
        test_activity.start()
        assert test_activity.state == "started"
        
        test_activity.resume()
        assert test_activity.state == "resumed"
        
        test_activity.pause()
        assert test_activity.state == "paused"
        
        test_activity.stop()
        assert test_activity.state == "stopped"
        
        test_activity.destroy()
        assert test_activity.state == "destroyed"
    
    def test_invalid_state_transition(self, test_activity):
        """Test that invalid state transitions raise errors."""
        # Try to resume without starting first
        with pytest.raises(InvalidStateError):
            test_activity.resume()
        
        # Start and then try to destroy without stopping
        test_activity.start()
        with pytest.raises(InvalidStateError):
            test_activity.destroy()
    
    def test_lifecycle_callbacks(self):
        """Test that lifecycle callbacks are called."""
        called_methods = []
        
        class CustomActivity(Activity):
            def on_start(self):
                called_methods.append('on_start')
            
            def on_resume(self):
                called_methods.append('on_resume')
            
            def on_pause(self):
                called_methods.append('on_pause')
            
            def on_stop(self):
                called_methods.append('on_stop')
            
            def on_destroy(self):
                called_methods.append('on_destroy')
        
        activity = CustomActivity("TestActivity")
        activity.start()
        activity.resume()
        activity.pause()
        activity.stop()
        activity.destroy()
        
        assert called_methods == ['on_start', 'on_resume', 'on_pause', 'on_stop', 'on_destroy']
    
    def test_add_view(self, test_activity):
        """Test adding views to activity."""
        view = TextView("test_view", "Test")
        
        test_activity.add_view("test_view", view)
        assert test_activity.get_view("test_view") == view
    
    def test_get_nonexistent_view(self, test_activity):
        """Test getting a view that doesn't exist."""
        assert test_activity.get_view("nonexistent") is None
    
    def test_remove_view(self, test_activity):
        """Test removing views from activity."""
        view = TextView("test_view", "Test")
        test_activity.add_view("test_view", view)
        
        assert test_activity.remove_view("test_view") is True
        assert test_activity.get_view("test_view") is None
        
        # Try removing non-existent view
        assert test_activity.remove_view("nonexistent") is False
    
    def test_activity_with_extras(self):
        """Test activity initialization with extra arguments."""
        activity = Activity("TestActivity", user_id=123, username="alice")
        assert activity.extras["user_id"] == 123
        assert activity.extras["username"] == "alice"


class TestIntent:
    """Test cases for Intent class."""
    
    def test_intent_creation(self):
        """Test creating an intent."""
        intent = Intent("ACTION_VIEW", "MainActivity")
        assert intent.action == "ACTION_VIEW"
        assert intent.target == "MainActivity"
    
    def test_intent_without_target(self):
        """Test creating an intent without a target."""
        intent = Intent("ACTION_VIEW")
        assert intent.action == "ACTION_VIEW"
        assert intent.target is None
    
    def test_intent_extras(self):
        """Test intent extras."""
        intent = Intent("ACTION_VIEW")
        intent.put_extra("key1", "value1")
        intent.put_extra("key2", 123)
        intent.put_extra("key3", [1, 2, 3])
        
        assert intent.get_extra("key1") == "value1"
        assert intent.get_extra("key2") == 123
        assert intent.get_extra("key3") == [1, 2, 3]
        assert intent.get_extra("nonexistent", "default") == "default"
    
    def test_has_extra(self):
        """Test checking if intent has an extra."""
        intent = Intent("ACTION_VIEW")
        intent.put_extra("key1", "value1")
        
        assert intent.has_extra("key1") is True
        assert intent.has_extra("nonexistent") is False
    
    def test_get_all_extras(self):
        """Test getting all extras."""
        intent = Intent("ACTION_VIEW")
        intent.put_extra("key1", "value1")
        intent.put_extra("key2", 123)
        
        all_extras = intent.get_all_extras()
        assert all_extras == {"key1": "value1", "key2": 123}
        
        # Verify it returns a copy (modifying shouldn't affect original)
        all_extras["key3"] = "new"
        assert intent.has_extra("key3") is False
