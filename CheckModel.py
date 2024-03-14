import torch
from transformers import BertTokenizer, BertForSequenceClassification

# Загрузка обученной модели
model = BertForSequenceClassification.from_pretrained('C:/Users/Acer ASPIRE 5/OneDrive/Рабочий стол/погром/курсовая/ResumeParser/bert_model')

# Инициализация токенизатора BERT
tokenizer = BertTokenizer.from_pretrained("dslim/bert-base-NER")

# Подготовка новых данных
new_text = "msasdad@email.com"
encoding = tokenizer(new_text, truncation=True, padding='max_length', max_length=128, return_tensors='pt')

# Применение модели к новым данным
input_ids = encoding['input_ids']
attention_mask = encoding['attention_mask']
with torch.no_grad():
    outputs = model(input_ids, attention_mask=attention_mask)

# Обработка выхода модели
_, predicted = torch.max(outputs.logits, dim=1)
predicted_label = predicted.item()

print(f"Predicted label: {predicted_label}")
