# SindMediTex
Develop By: Raja Vavekanand


[![SindMediTex Dataset](https://img.shields.io/badge/SindMediTex-Dataset-blue)](https://github.com/rajavavek/SindMediTex/blob/main/SindMediTex.csv)   [![Paper](https://img.shields.io/badge/SindMediTex-Paper-orange)](https://github.com/rajavavek/SindMediTex/blob/main/SindMediTex.csv)  [![Code](https://img.shields.io/badge/SindMediTex-Code-blue)](https://github.com/rajavavek/SindMediTex/tree/main/Codes)


The evolution of Natural Language Processing (NLP) has revolutionized healthcare by enabling efficient information retrieval and patient support. However, linguistic underrepresentation hinders progress for low-resource languages like Sindhi. To address this gap, we introduce SindMediTex, a 1st and largest Sindhi medical text dataset comprising 100,000 entries categorized into four classes: Condition, Treatment, Prevention, and Other. We introduce a novel dataset SindMediTex is designed to facilitate robust NLP model development for healthcare-focused applications in Sindhi. The dataset incorporates real-world variability and intentional noise to simulate challenges in medical text classification. With categories representing medical conditions, treatments, prevention strategies, and general health information, this dataset is poised to enable more efficient information retrieval and patient support. 
The dataset was synthetically generated and manually curated by native Sindhi speakers and healthcare professionals to ensure linguistic and contextual accuracy. The labels were reviewed to maintain consistency and relevance. The dataset is stored in CSV format, with two columns: Text (Sindhi medical text) and Label (category). By introducing SindMediTex, we aim to bridge the gap in Sindhi NLP resources, ultimately improving healthcare outcomes for the millions of people who speak this language.

![image](https://github.com/user-attachments/assets/b8de0d12-c8df-47b8-a530-3b3378d79559)

The SindMediTex dataset was developed using a multi-step approach. First, a team of native Sindhi speakers and healthcare professionals collaborated to create a comprehensive list of medical terms and concepts. Next, a data generation script was used to create a large corpus of Sindhi medical text. The text was then manually annotated and categorized into four classes: Condition, Treatment, Prevention, and Other. The dataset was reviewed and validated to ensure accuracy and consistency.

![image](https://github.com/user-attachments/assets/757646c5-9ac7-451b-afc3-add42cfbb2df)

The SindMediTex dataset consists of 100,000 labeled entries, divided equally among four categories: Condition, Treatment, Prevention, and Other. Each entry includes a Sindhi medical text and its corresponding label. The dataset is stored in CSV format, with two columns: Text and Label. The dataset includes a range of medical topics, including diseases, symptoms, treatments, and prevention strategies. The text is written in a clear and concise manner, making it suitable for NLP applications.

Dataset Overview

| Sindhi Text                                                                 | Label       |
|-----------------------------------------------------------------------------|-------------|
| شوگر جي مريضن ۾ اکيون خراب ٿيڻ جو امڪان وڌي سگهي ٿو.                         | Condition   |
| دل جي بيمارين کان بچڻ لاءِ روزانو هلڻ جي عادت ٺاهي.                            | Prevention  |
| بلڊ پريشر جي علاج لاءِ ڊاڪٽر تجويز ٿيل دوائون وقت تي وٺو.                      | Treatment   |
| دماغي صحت لاءِ روزانو مراقبو ڪرڻ مفيد ٿي سگهي ٿو.                             | Other       |
| جگر جي خرابي جا نشان جھڙوڪ يرقان ۽ معدي ۾ سور ٿي سگهن ٿا.                     | Condition   |
| ڪينسر کان بچڻ لاءِ سگريٽ نوشي بند ڪريو.                                     | Prevention  |
| معدي جي جلن لاءِ علاج ۾ اينٽي ايڊز دوائون تجويز ڪيون وڃن ٿيون.                | Treatment   |
| صحتمند زندگي لاءِ مناسب سمهڻ ضروري آهي.                                      | Other       |

## Labels
The dataset includes four distinct labels:

- **Condition**: Indicates a medical condition or its symptoms.
- **Prevention**: Describes preventive measures for health-related issues.
- **Treatment**: Refers to treatments or prescribed medicines.
- **Other**: General advice or unrelated health information.
  
**Note**: Ensure ethical use of this dataset, respecting the privacy and cultural sensitivity of Sindhi-speaking populations.

## Usage
This dataset can be used for various NLP tasks, such as:

- Sentiment analysis
- Text classification
- Named entity recognition (NER)
- Healthcare-specific NLP applications
