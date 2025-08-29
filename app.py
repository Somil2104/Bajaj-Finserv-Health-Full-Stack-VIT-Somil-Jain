from flask import Flask, request, jsonify

app = Flask(__name__)

USER_ID = "somil_jain_21042004"
EMAIL = "somiljain2104@gmail.com"
ROLL_NUMBER = "22BCE10387"

@app.route('/', methods=['GET'])
def home():
    return jsonify({
        "message": "Flask server is running. Use POST /bfhl with JSON data."
    })

@app.route('/bfhl', methods=['POST'])
def bfhl():
    data = request.get_json().get('data', [])

    odd_numbers = []
    even_numbers = []
    alphabets = []
    special_characters = []
    total_sum = 0
    alpha_concat = []

    for el in data:
        if str(el).isnumeric():
            num_val = int(el)
            total_sum += num_val
            if num_val % 2 == 0:
                even_numbers.append(str(el))
            else:
                odd_numbers.append(str(el))
        elif isinstance(el, str) and el.isalpha():
            alphabets.append(el.upper())
            alpha_concat.extend(list(el))
        else:
            special_characters.append(el)

    concat_chars = alpha_concat[::-1]
    concat_string = ""
    flag_upper = True
    for ch in concat_chars:
        concat_string += ch.upper() if flag_upper else ch.lower()
        flag_upper = not flag_upper

    response = {
        "is_success": True,
        "user_id": USER_ID,
        "email": EMAIL,
        "roll_number": ROLL_NUMBER,
        "odd_numbers": odd_numbers,
        "even_numbers": even_numbers,
        "alphabets": alphabets,
        "special_characters": special_characters,
        "sum": str(total_sum),
        "concat_string": concat_string
    }

    return jsonify(response), 200

if __name__ == '__main__':
    app.run()
