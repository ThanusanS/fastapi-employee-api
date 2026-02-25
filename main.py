from fastapi import FastAPI

app=FastAPI()




@app.get("/")
def home():
    return {"massage":"mmnnnkkkli"}



@app.get("/display/{idn}")
def show_id(idn):
    return f"myId: {idn}"








emp=[

    {"id":1234,"name":"vinoth","place":"Tamilnadu"},
    {"id":5678,"name":"Kamal","place":"Canada"}
]

# Path Parameter

@app.get("/dis/{idmy}")
def view(idmy:int):
    for details in emp:
        if details['id']==idmy:
            return details




# Query Parameter



@app.get("/dis")
def view(idmy:int):
    for details in emp:
        if details['id']==idmy:
            return details
        