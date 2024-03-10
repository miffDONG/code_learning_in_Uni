"""
전처리 기록 x 새로운 전처리 과정이 추가 될 시 이걸로 돌려야 함.
"""
# def preprocess_data(cfg, dataset, category_df):
#     logger.info('preprocess dataset...')

#     idx_to_SS = category_df.SSno.values
#     SS_to_idx = {cat:idx for idx, cat in enumerate(idx_to_SS)}

#     def preprocess_fn(example):
#         title = example['invention_title']
#         abstract = example['abstract']
#         claims = example['claims']

#         texts = f"{title} 요약: {abstract} 청구항: {claims}"
#         labels = np.zeros(len(SS_to_idx), dtype=np.bool_)

#         for SSno in example['SSnos'].split():
#             labels[SS_to_idx[SSno]] = 1

#         return {
#             'texts': texts,
#             'labels': labels,
#         }
    
#     preprocessed = dataset.map(
#         preprocess_fn,
#         remove_columns=[
#             col
#             for col in dataset.column_names
#             if col not in ['documentId']
#         ],
#     )
#     return preprocessed

# def tokenize_data(cfg, dataset, tokenizer):
#     logger.info('tokenize dataset...')
#     def batch_tokenize(batch):
#         return tokenizer(
#             batch,
#             max_length=512,
#             padding='max_length',
#             truncation=True,
#         )
#     tokenized = dataset.map(
#         batch_tokenize,
#         input_columns='texts',
#         batched=True,
#     )
#     return tokenized