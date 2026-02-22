from flask import Flask, request, render_template
from operators import add, subtract, multiply, divide

app = Flask(__name__)

OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculate(expr: str):
    """
    Cette fonction calcule le résultat d'une expression mathématique simple donnée sous forme de chaîne de caractères.

    Parameters:
        expr (str): L'expression mathématique à calculer, par exemple "3 + 4".

    Returns:
        float: Le résultat du calcul de l'expression.
    """
    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")

    s = expr.replace(" ", "")

    op_pos = -1
    op_char = None

    ## Assigner le caractère de l'opérateur et sa position pour pouvoir séparer les opérandes ensuite
    for i, ch in enumerate(s):
        if ch in OPS:
            if op_pos != -1:
                raise ValueError("only one operator is allowed")
            op_pos = i
            op_char = ch

    if op_pos <= 0 or op_pos >= len(s) - 1:
        # operator at start/end or not found
        raise ValueError("invalid expression format")

    left = s[:op_pos]
    right = s[op_pos+1:]

    try:
        a = float(left)
        b = float(right)
    except ValueError:
        raise ValueError("operands must be numbers")

    return OPS[op_char](a, b) ## Transforme l'opérateur trouvé en fonction

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Retourne la page d'accueil de la calculatrice. 
    Si une expression est soumise via POST, elle est calculée et le résultat est affiché.
    """
    result = ""
    if request.method == 'POST':
        expression = request.form.get('display', '')
        try:
            result = calculate(expression)
        except Exception as e:
            result = f"Error: {e}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)