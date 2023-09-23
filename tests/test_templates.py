import pytest
from dashboard_builder import get_template

def test_get_existing_template():
    # Assuming "base.html" exists in your templates directory
    template_content = get_template("base.html")
    # A simple assertion to check if the template's content is not empty
    assert template_content.strip() != ""

def test_get_nonexistent_template():
    # This test will check if fetching a non-existent template raises a FileNotFoundError
    with pytest.raises(FileNotFoundError):
        get_template("nonexistent.html")
