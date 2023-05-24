from src.core.settings import app, api
from src.core.urls import restful_api_urls


# Add api endpoints
restful_api_urls(api)

if __name__ == '__main__':
    app.run(debug=app.config.get("DEBUG"), port=5012)
