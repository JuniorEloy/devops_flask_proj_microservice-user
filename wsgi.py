from app import create_app

app = create_app("production")

app.run(port=3030, host="0.0.0.0")