from flask import Flask, request, jsonify, render_template

app = Flask(__name__, static_url_path='', static_folder='staticpages')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/waveforms', methods=['GET'])
def get_waveforms():
    return 'getting all waveforms'

@app.route('/waveforms/<waveform>', methods=['GET'])
def get_ind_waveform(waveform):
    return f'waveform {waveform} selected'

@app.route('/weather', methods=['GET'])
def get_weather():
    return 'get weather'

@app.route('/waveforms', methods=['POST'])
def create_waveform():
    return 'creating waveform'

@app.route('/waveforms', methods=['PUT'])
def update_waveform():
    return 'update waveform'

if __name__ == '__main__':
    app.run(debug=True)