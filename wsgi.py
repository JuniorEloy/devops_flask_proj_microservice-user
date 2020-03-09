from app import create_app as application

app = application("production")

if __name__ == "__main__":
    app.run(port=3030, host="0.0.0.0")