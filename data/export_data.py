from storage import DBStorage
import pandas as pd

def export_data():
    storage = DBStorage()
    data = storage.get_relevance_data()
    
    # Export to CSV
    data.to_csv('relevance_data.csv', index=False)

if __name__ == "__main__":
    export_data()