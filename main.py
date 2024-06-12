from controller.ConvertVideoController import app
from config import config

configurations = config['development']
app.config.from_object(configurations)

if __name__ == "__main__":
    app.run(debug=True)