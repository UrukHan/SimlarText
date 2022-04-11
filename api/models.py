# Import libraries
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import torch

# Bert classifer model
class BERT_MODEL():
    ''' info '''

    # Class initialization
    def __init__(self):
        if torch.cuda.is_available():
            self.device = torch.device('cuda')
        else:
            self.device = torch.device('cpu')
            print('CPU  CPU  CPU  CPU  CPU  CPU  CPU  CPU  CPU  CPU  CPU  CPU  CPU')

        self.BERT_NAME = 'model/'
        self.model = SentenceTransformer(self.BERT_NAME).to(self.device)

    # Predict function
    def predict(self, input):
        sentence_embeddings = self.model.encode(input)
        sentence_embeddings.shape
        prediction = cosine_similarity(
            [sentence_embeddings[0]],
            sentence_embeddings[1:]
        )[0]
        return {"prediction": prediction.tolist()}






