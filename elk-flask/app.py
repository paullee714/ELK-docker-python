from flask import Flask, Blueprint

from route.elf_test_route import elk_test

app = Flask(__name__)

app.register_blueprint(elk_test)

if __name__ == '__main__':

    app.run()
