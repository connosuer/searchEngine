from flask import Flask, request,jsonify,abort
from search import search 
import html
from filter import Filter 
from storage import DBStorage
import csv
from datetime import datetime

app = Flask(__name__)

styles = """
<style> 
.site { 
font-size: .8rem; 
color: green; 
}

.snippet{ 
    font-size: .9rem;
    color: gray; 
    margin-bottom: 30px; 
}

.rel-button{
    cursor: pointer;
    color: blue; 
    }
</style>

<script>
const relevant = function(query, link, relevance){
    fetch("/relevant", {
        method: 'POST',
        headers: {
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            "query": query,
            "link": link,
            "relevance": relevance
        })
    });
}
</script>
"""

search_template = styles + """
<form action = "/" method="post"> 
    <input type = "text" name="query"> 
    <input type = "submit" value="Search"> 
</form>
"""

result_template = """
<p class="site">{rank}: {link} 
    <select onchange='relevant("{query}", "{link}", this.value)'>
        <option value="">Rate relevance</option>
        <option value="0">Not relevant</option>
        <option value="1">Somewhat relevant</option>
        <option value="2">Relevant</option>
        <option value="3">Highly relevant</option>
    </select>
</p>
<a href="{link}">{snippet}</a>
"""

def show_search_form(): 
    return search_template

def run_search(query):
    results = search(query)
    fi = Filter(results)
    results = fi.filter()
    rendered = search_template
    results["snippet"] = results["snippet"].apply(lambda x: html.escape(x))
    for index, row in results.iterrows(): 
        rendered += result_template.format(**row)
    return rendered

@app.route("/", methods= ["GET", "POST"])
def search_form(): 
    if request.method == "POST": 
        query = request.form["query"]
        return run_search(query)
    else: 
        return show_search_form()


from flask import Flask, request, jsonify, abort

@app.route("/relevant", methods=["POST"])
def mark_relevant():
    data = request.get_json()
    query = data["query"]
    link = data["link"]
    relevance_score = data.get("relevance", 1)  # Default to 1 if not provided
    
    storage = DBStorage()
    storage.mark_relevant(query, link, relevance_score)

    #log the feedback
    with open('feedback_log.csv', 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([datetime.utcnow(), query, link, relevance_score])

    return jsonify(success=True)