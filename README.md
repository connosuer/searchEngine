flask --debug run --port 5001


sqlite3 links.db 
select query, link, relevance from results where relevance is not null
------
todo:
mark relevant result in search and store in database
get enough training data for machine learning

building filters that query data from the database, train a model, and filter based on that model
