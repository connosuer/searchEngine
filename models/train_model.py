from hybrid_relevance_model import HybridRelevanceModel
from storage import DBStorage
import joblib

def train_model():
    # Load data
    storage = DBStorage()
    data = storage.get_relevance_data()
    
    # Prepare data
    X = data['title'] + ' ' + data['snippet']
    y = data['relevance']
    
    # Initialize and train the model
    model = HybridRelevanceModel()
    model.train(X, y)
    
    # Save the model
    joblib.dump(model, 'hybrid_relevance_model.joblib')

if __name__ == "__main__":
    train_model()