from flask import Flask, render_template
from config import create_app
from controller import routes

app = create_app()


app.register_blueprint(routes)
if __name__ == '__main__':
	app.run(debug=True)