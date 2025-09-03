from app import app

def test_home():
    # Create a test client
    client = app.test_client()
    
    # Send GET request to home page
    response = client.get('/')
    
    # Assert that status code is 200
    assert response.status_code == 200
    
    # Optional: Check response content
    assert b"Hello this is CI/CD" in response.data
