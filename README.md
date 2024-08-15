flask --debug run --port 5001


sqlite3 links.db 
select query, link, relevance from results where relevance is not null