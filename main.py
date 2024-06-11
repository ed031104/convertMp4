from controller.ConvertVideoController import app
import os

if __name__ == "__main__":
    if not os.path.exists(app.config["UPLOAD_FOLDER"]):
        os.makedirs(app.config["UPLOAD_FOLDER"])
    app.run(debug=True, host="0.0.0.0", port=os.getenv("PORT", default=5000))