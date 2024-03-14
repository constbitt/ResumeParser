import torch
from transformers import BertTokenizer, BertModel, AutoTokenizer, BertForTokenClassification
from torch.utils.data import Dataset, DataLoader
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from transformers import BertForSequenceClassification, AdamW
import numpy as np

# Преобразование текста в формат BERT
tokenizer = BertTokenizer.from_pretrained("dslim/bert-base-NER")
max_len = 301  # Максимальная длина входной последовательности для BERT

# Чтение данных из файла
with open("second_training.csv", "r", encoding="utf-8") as file:
    lines = file.readlines()

# Парсинг данных
texts = []
labels = []
for line in lines:
    line = line.strip()
    parts = line.split(";")
    text = parts[0]
    label = parts[2]
    texts.append(text)
    labels.append(label)

# Кодирование текста
encoded_texts = []
max_len = 0  # Переменная для хранения максимальной длины последовательности

# Проход по текстам и  токенизация
for text in texts:
    encoded_text = tokenizer.encode_plus(text, padding='max_length', truncation=True, max_length=max_len, return_tensors='pt')
    encoded_texts.append(encoded_text)
    max_len = max(max_len, len(encoded_text['input_ids'][0]))

# Объединение всех токенизированных представлений в один словарь BatchEncoding
batch_encoding = {}
for key in encoded_texts[0].keys():
    batch_encoding[key] = torch.cat([encoded_text[key] for encoded_text in encoded_texts], dim=0)

# Кодирование меток
label_encoder = LabelEncoder()
encoded_labels = label_encoder.fit_transform(labels)

# Получение уникальных меток и их соответствующих цифровых кодов
unique_labels = set(labels)
unique_codes = set(encoded_labels)

print("Уникальные метки и их соответствующие цифры:")
for label, code in zip(unique_labels, unique_codes):
    print(f"{label}: {code}")

# Разделение данных на обучающую и тестовую выборки
train_texts, test_texts, train_labels, test_labels = train_test_split(batch_encoding['input_ids'], encoded_labels, test_size=0.2, random_state=42)

# Создание Dataset для загрузки данных в DataLoader
class CustomDataset(Dataset):
    def __init__(self, texts, labels):
        self.texts = texts
        self.labels = labels

    def __len__(self):
        return len(self.texts)

    def __getitem__(self, idx):
        return {
            'input_ids': self.texts[idx],
            'labels': torch.tensor(self.labels[idx])
        }

train_labels = np.repeat(train_labels, repeats=4)
test_labels = np.repeat(test_labels, repeats=4)

train_dataset = CustomDataset(train_texts, train_labels)
test_dataset = CustomDataset(test_texts, test_labels)

# Загрузка предобученной модели BERT
model = BertForTokenClassification.from_pretrained('dslim/bert-base-NER', num_labels=len(label_encoder.classes_))

# Обучение модели
optimizer = AdamW(model.parameters(), lr=1e-5)

train_dataloader = DataLoader(train_dataset, batch_size=8, shuffle=True)

epochs = 6  # Устанавливаем количество эпох

for epoch in range(epochs):
    model.train()
    for batch in train_dataloader:
        input_ids = batch['input_ids']
        labels = batch['labels']
        optimizer.zero_grad()
        outputs = model(input_ids, labels=labels)
        loss = outputs.loss
        loss.backward()
        optimizer.step()

# Сохранение обученной модели
model.save_pretrained("./bert_model")

print("Обучение завершено. Модель сохранена.")
