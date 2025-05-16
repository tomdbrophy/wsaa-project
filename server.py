from flask import Flask, request, jsonify, render_template

app = Flask(__name__) 


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/activities', methods=['GET'])
def get_all_activities():
    return 'getting all activities'

@app.route('/staff/<staff_name>', methods=['GET'])
def staff_hours(staff_name):
    return f'getting hours for {staff_name}'

@app.route('/modules/<module_name>', methods=['GET'])
def module_allocation(module_name):
    return f'getting all allocations for {module_name}'

@app.route('/activities', methods=['POST'])
def create_activity():
    return 'creating activity'

@app.route('/activities/<activity_id>', methods=['PUT'])
def update_activity(activity_id):
    return f'updating activity {activity_id}'

@app.route('/activities/<activity_id>', methods=['DELETE'])
def delete_activity(activity_id):
    return f'deleting activity {activity_id}'

if __name__ == '__main__':
    app.run(debug=True)