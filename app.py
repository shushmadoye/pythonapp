ame__)
@app.route('/')
def hello():
 return "Hello, World!"
if __name__ == "__main__":
 app.run(host="0.0.0.0", port=5000)

