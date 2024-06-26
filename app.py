from flask import Flask, render_template, request, send_file
import itertools
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        words = [request.form[f'word{i}'] for i in range(1, 13)]
        permutations = list(itertools.permutations(words))

        # Permütasyonları dosyaya yaz
        file_path = 'permutations.txt'
        with open(file_path, 'w') as f:
            for perm in permutations:
                f.write(', '.join(perm) + '\n')

        return render_template('index.html', words=words, permutations=permutations[:100], file_path=file_path)

    return render_template('index.html')

@app.route('/download')
def download():
    file_path = request.args.get('file_path')
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)