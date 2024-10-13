## (ICPR'2024 Oral) ConCSE: Unified Contrastive Learning and Augmentation for Code Switched Embeddings.

This repository contains the code and proposed Koglish datasets for our paper [ConCSE: Unified Contrastive Learning and Augmentation for Code-Switched Embeddings](https://arxiv.org/abs/2409.00120)

The contents of the folder are as follows : 
1. preprocessing/Koglish_dataset : This is the folder containing the koglish dataset. You can download it via“https://huggingface.co/Jangyeong”.
2. algorithms/Koglish_test_Sect5.1: Koglish dataset validation experiment performed in Section 5.1.
3. algorithms/ConCSE_test_Sect5.2: Experiments with our proposed ConCSE from Section 5.2.

### Installation ### 
We recommend setting up a conda environment for the project:
```
conda create --name=ConCSE python=3.8
conda activate ConCSE

git clone https://github.com/jjy961228/ConCSE.git
pip install -r requirements.txt
```

### Download datasets ###
* Koglish datasets are uploaded to "https://huggingface.co/Jangyeong" and can be downloaded by running download_dataset.py.
* Koglish-GLUE was used in the experiments in **section 5.1**. 
* In the **ConCSE** experiment in **section 5.2**, Koglish-STS, Koglish-SICK, and Kolgish-NLI were used: Koglish-NLI was used for training, and Koglish-STS and Koglish-SICK were used for testing.
``` python
cd preproessing/Koglish_dataset
python download_dataset.py
```
After downloading the dataset, place it in the Koglish_dataset directory.

## Model List

Our released models are listed as follows. You can download these models using the shared Google Drive.
|              Model              | Avg. STS-B |
|:-------------------------------|:--------:|
| [ [princeton-nlp/unsup-simcse-bert-base-uncased](https://huggingface.co/princeton-nlp/unsup-simcse-bert-base-uncased)](https://drive.google.com/drive/folders/10jMEpRlA9fgRaAZyC-Lw7LXKmTLpbv8B?usp=sharing) |   80.23 |
