from flask import Flask, render_template, request, jsonify
from expert_system.engine import ExpertSystem

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.get_json()
    goal = data['goal']
    level = data['level']
    equipment = data['equipment']

    system = ExpertSystem()
    result = system.get_recommendation(goal, level, equipment)

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
#User → index.html → app.py → engine.py → rules.json → engine.py → app.py → index.html (with output)
