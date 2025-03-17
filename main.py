import csv
import io

from fastapi import FastAPI, Request, File, UploadFile
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates


app = FastAPI()
app.mount('/static', StaticFiles(directory='static'), name='static')
templates = Jinja2Templates(directory="templates")

@app.get('/', response_class=HTMLResponse)
async def index_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "csv_data": None})

@app.post('/upload')
async def upload_csv(request: Request, csv_file: UploadFile = File(...)):
    # Read the uploaded file
    contents = await csv_file.read()
    decoded_contents = contents.decode("utf-8")

    # Parse CSV data into a list
    csv_reader = csv.reader(io.StringIO(decoded_contents)) # This just takes the string data and turns it into a file like object for csv reader to handle
    csv_data = [row for row in csv_reader] # Win for list comprehensions

    # Render template with new CSV data
    return templates.TemplateResponse("index.html", {"request": request, "csv_data": csv_data})
