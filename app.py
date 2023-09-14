from flask import Flask, render_template, request, jsonify
from spectrum_analyzer import SpectrumAnalyzer
import base64
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/options', methods=['POST'])
def options():
    options_data = request.get_json()
    # Process the options_data and create a SpectrumAnalyzer instance with the given options
    analyzer = SpectrumAnalyzer(options_data)

    # Get the generated image and convert it to base64
    buf = io.BytesIO()
    analyzer.fig.savefig(buf, format='png')
    image_base64 = base64.b64encode(buf.getvalue()).decode('utf-8').replace('\n', '')

    return jsonify({'image': image_base64})

@app.route('/settings', methods=['GET', 'POST'])
def settings():
    if request.method == 'POST':
        # Submit settings as a POST request to the '/options' page

        #..... do that here....

        return "Settings submitted!"
    return render_template('settings.html')


if __name__ == '__main__':
    app.run(debug=True)