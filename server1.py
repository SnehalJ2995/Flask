# import the Flask class from flask package
from flask import Flask, request
import pickle

# load the model from pickle file
file = open('./revenue_model.pkl', 'rb')
model = pickle.load(file)
file.close()

# create a new server with the name same as that of the module
app = Flask(__name__)


# decorator
# when the application receives a request with GET method
# and path as / root() gets called
@app.route("/", methods=["GET"])
def root():
    return """
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.1/dist/css/bootstrap.min.css" integrity="sha384-zCbKRCUGaJDkqS1kPbPd7TveP5iyJE0EjAuZQTgFLD2ylzuqKfdKlfG/eSrtxUkn" crossorigin="anonymous">
        <h1>Predict your Revenue v2</h1>
        <h3>Welcome to the application</h3>
        <form action="/predict" method="POST">
             
            Product_Category <input name="Product_Category" type="text" ><br><br>
            Sub_Category <input name="Sub_Category" type="text" ><br><br>
            Quantity <input name="Quantity" type="text" ><br><br>
            Unit_Cost <input name="Unit_Cost" type="text" ><br><br>
            Unit_Price <input name="Unit_Price" type="text" ><br><br>
            Cost <input name="Cost" type="text" ><br><br>
            
            <button>Predict Revenue</button>
            
        </form>
    """
@app.route("/predict", methods=["POST"])
def predict_revenue():

    Product_Category = float(request.form.get("Product_Category"))
    Sub_Category = float(request.form.get("Sub_Category"))
    Quantity = float(request.form.get("Quantity"))
    Unit_Cost = float(request.form.get("Unit_Cost"))
    Unit_Price = float(request.form.get("Unit_Price"))
    Cost = float(request.form.get("Cost"))
    #print(f"Unit_Cost = {Unit_Cost}, type = {type(Unit_Cost)}")
    #print(f"Unit_Price = {Unit_Price}, type = {type(Unit_Price)}")
    #print(f"Cost = {Cost}, type = {type(Cost)}")

    revenue = model.predict([[Product_Category, Sub_Category, Quantity, Unit_Cost, Unit_Price, Cost]])
    print(revenue)

    return f"<h1>Revenue = {revenue[0]}</h1>"


# start the server
# debug = True => no need to restart everytime there is a change in the code
app.run(debug=True)