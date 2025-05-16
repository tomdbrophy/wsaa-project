from flask import Flask, request, jsonify, render_template
from dao import DAO
from config import db_config

app = Flask(__name__)

dao = DAO(host=db_config['host'],
          user=db_config['user'],
          password=db_config['password'],
          db=db_config['database'])


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/activities', methods=['GET'])
def get_all_activities():
    # Fetch all activities from the database
    query = "SELECT * FROM activities"
    activities = dao.execute_query(query)
    return jsonify(activities)

@app.route('/staff/<staff_name>', methods=['GET'])
def staff_hours(staff_name):
    query = "SELECT * FROM activities WHERE staff_name = %s"
    hours = dao.execute_query(query, (staff_name,))
    return jsonify(hours)

@app.route('/modules/<module_name>', methods=['GET'])
def module_allocation(module_name):
    query = "SELECT * FROM activities WHERE module_name = %s"
    allocations = dao.execute_query(query, (module_name,))
    return jsonify(allocations)

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