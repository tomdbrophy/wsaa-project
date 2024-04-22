from flask import Flask, request, jsonify, render_template

app = Flask(__name__, static_url_path='', static_folder='staticpages')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bookings', methods=['GET'])
def get_all_bookings():
    return 'getting all bookings'

@app.route('/bookings/<room>', methods=['GET'])
def get_room_bookings(room):
    return f'room {room} selected'

@app.route('/bookings', methods=['POST'])
def create_waveform():
    return 'creating booking'

@app.route('/bookings', methods=['PUT'])
def update_waveform():
    return 'update booking'

if __name__ == '__main__':
    app.run(debug=True)