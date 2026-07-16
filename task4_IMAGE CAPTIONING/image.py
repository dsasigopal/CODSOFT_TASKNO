import torch
import torch.nn as nn
import torchvision.models as models

# 1. ENCODER: Extract features from images using ResNet
class EncoderCNN(nn.Module):
    def __init__(self):
        super(EncoderCNN, self).__init__()
        resnet = models.resnet50(pretrained=True)
        # Remove the final classification layer
        self.resnet = nn.Sequential(*list(resnet.children())[:-1])
        
    def forward(self, images):
        features = self.resnet(images)
        return features.reshape(features.size(0), -1)

# 2. DECODER: Generate captions using an RNN/LSTM
class DecoderRNN(nn.Module):
    def __init__(self, embed_size, hidden_size, vocab_size):
        super(DecoderRNN, self).__init__()
        self.embedding = nn.Embedding(vocab_size, embed_size)
        self.lstm = nn.LSTM(embed_size, hidden_size, batch_first=True)
        self.fc = nn.Linear(hidden_size, vocab_size)

    def forward(self, features, captions):
        embeddings = self.embedding(captions)
        # Combine image features with word embeddings
        x = torch.cat((features.unsqueeze(1), embeddings), dim=1)
        hiddens, _ = self.lstm(x)
        outputs = self.fc(hiddens)
        return outputs

# 3. INITIALIZATION
encoder = EncoderCNN()
decoder = DecoderRNN(embed_size=256, hidden_size=512, vocab_size=1000)
