# Multimodal Fetal Health Risk Prediction System

## 📌 Project Overview

This project presents a multimodal artificial intelligence system for fetal health risk prediction by combining **ultrasound image analysis** with **maternal blood and clinical parameters**. The system uses two independent prediction pathways: a CNN-based ultrasound risk prediction module and a machine-learning-based nutrition risk prediction module. The outputs of these two pathways are then combined using **meta-model-level fusion** to determine the final fetal health risk level as **Low, Medium, or High**. Based on the maternal condition and final risk, the system also generates a personalized food and nutrition recommendation plan.

## 🎯 Objectives

- Analyze ultrasound images using deep learning.
- Identify the relevant ultrasound plane/classification information.
- Predict ultrasound-based fetal health risk.
- Analyze maternal clinical and nutrition-related parameters.
- Predict maternal nutrition risk using a machine learning model.
- Combine ultrasound and nutrition risks through meta-model fusion.
- Generate a final fetal health risk level.
- Provide personalized food and diet recommendations.
- Present the complete prediction workflow through an interactive Streamlit dashboard.

## 💡 Novelty

The key novelty of the project is the integration of **two complementary modalities—ultrasound image information and maternal clinical/nutrition information—within a single fetal health risk prediction framework**. Instead of depending only on ultrasound images or only on maternal parameters, the system independently estimates ultrasound risk and nutrition risk and subsequently combines these outputs using a meta-model fusion approach. The final risk decision therefore considers information from both modalities. An additional personalized food recommendation module connects the prediction outcome with practical dietary guidance based on the identified maternal nutritional condition.

## 🔄 Methodology

### 1. Ultrasound Risk Prediction

Ultrasound images are provided as the first input modality. The images undergo preprocessing before being passed to the trained CNN model. The CNN extracts relevant visual features and performs the required plane/classification analysis. The resulting ultrasound information is converted into an ultrasound risk category:

- **LOW**
- **MEDIUM**
- **HIGH**

### 2. Nutrition Risk Prediction

Maternal data is provided as the second input modality. The data is preprocessed and supplied to the trained machine learning model. The nutrition pathway produces a nutrition risk category:

- **Low**
- **Moderate**
- **High**

The project also analyzes nutritional conditions using parameters such as BMI, blood sugar, and systolic blood pressure for recommendation generation.

### 3. Meta-Model-Level Fusion

The ultrasound risk and nutrition risk outputs are converted into numerical risk levels and combined using a meta-model. The implemented fusion stage uses **multinomial Logistic Regression**.

The risk mapping used in the implementation is:

| Risk Level | Numerical Value |
|---|---:|
| Low | 0 |
| Medium / Mid | 1 |
| High | 2 |

The fusion model receives:

```text
Ultrasonic_Risk
Nutrition_Risk
```

and predicts:

```text
Final_Risk
```

The resulting final risk is categorized as:

- **LOW**
- **MID**
- **HIGH**

### 4. Personalized Food Recommendation

The recommendation module first identifies a nutrition-related condition from maternal parameters.

The current condition rules include:

| Condition | Rule |
|---|---|
| Obese | BMI ≥ 30 |
| Underweight | BMI < 18.5 |
| High Sugar | Blood sugar ≥ 140 |
| High BP | Systolic BP ≥ 140 |
| Normal | Otherwise |

The recommendation system then combines the final fetal health risk with the identified nutrition condition to generate an appropriate food plan.

## 🧠 Models Used

### CNN Model

A trained CNN-based deep learning model is used for ultrasound image analysis and risk prediction. The model processes ultrasound images and performs the required image classification tasks before producing ultrasound-related risk information.

### Random Forest Model

A Random Forest-based machine learning model is used in the nutrition risk prediction pathway to analyze maternal data and classify nutrition risk.

### Logistic Regression Meta Model

A multinomial Logistic Regression model is used at the fusion stage. It receives the ultrasound and nutrition risk outputs and predicts the final combined risk category.

## 📊 Meta-Model Evaluation

The implemented meta-model was evaluated using accuracy, precision, recall, and F1-score.

**Overall Fusion Accuracy: 90.74%**

| Class | Precision | Recall | F1-Score | Support |
|---|---:|---:|---:|---:|
| LOW | 0.83 | 1.00 | 0.91 | 60 |
| MID | 1.00 | 0.50 | 0.67 | 24 |
| HIGH | 1.00 | 1.00 | 1.00 | 24 |

These evaluation measures help assess how effectively the fusion model identifies each final risk category. In particular, recall indicates the proportion of actual samples of a risk category correctly identified, precision indicates the reliability of predictions assigned to that category, and F1-score provides a combined measure of precision and recall.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| TensorFlow / Keras | CNN-based ultrasound analysis |
| Scikit-learn | Machine learning and evaluation |
| Random Forest | Nutrition risk prediction |
| Logistic Regression | Meta-model fusion |
| Pandas | Data processing |
| NumPy | Numerical operations |
| Pillow | Image processing |
| Joblib | Saving/loading machine learning models |
| Streamlit | Interactive web application |

## 💻 Software Requirements

- Python 3.x
- Jupyter Notebook / Google Colab for model development
- Visual Studio Code or another Python IDE
- TensorFlow / Keras
- Scikit-learn
- Pandas
- NumPy
- Pillow
- Joblib
- Streamlit
- Git and GitHub for version control and deployment

## 🖥️ Hardware Requirements

- Modern laptop or desktop computer
- Minimum 8 GB RAM recommended
- Multi-core processor
- Sufficient storage for the CNN model and datasets
- Internet connection for installation, GitHub, and cloud deployment
- GPU is beneficial during CNN training but is not mandatory for basic application execution

## 📂 Project Structure

```text
fetal-health-risk-prediction/
│
├── app.py
├── requirements.txt
│
├── final_saved_model/
│   ├── saved_model.pb
│   ├── variables/
│   │   ├── variables.data-00000-of-00001
│   │   └── variables.index
│   └── assets/
│
└── README.md
```

> The nutrition model files should be included only if they are loaded by the current version of `app.py`.

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/Krishnasaikmv/fetal-health-risk-prediction.git
```

Move into the project directory:

```bash
cd fetal-health-risk-prediction
```

Create a virtual environment:

```bash
python -m venv fetal_env
```

Activate it on Windows:

```powershell
fetal_env\Scripts\activate
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

## ▶️ Running the Application

Start the Streamlit application using:

```bash
streamlit run app.py
```

The application will open in the browser through the local Streamlit address.

## 🌐 Deployment

The application is designed as a Streamlit application and can be deployed using **Streamlit Community Cloud**.

General deployment workflow:

```text
Local Project
     ↓
GitHub Repository
     ↓
Streamlit Community Cloud
     ↓
Public Web Application
```

The large TensorFlow model files can be stored using **Git Large File Storage (Git LFS)** when required.

## 🧪 Testing

The application can be tested at different levels:

### Unit Testing
Individual functions such as nutrition condition identification and food recommendation generation can be tested independently.

### Model Testing
The CNN, Random Forest, and meta-model predictions can be evaluated using appropriate test datasets.

### Integration Testing
The complete flow from ultrasound input and maternal data through final risk prediction and food recommendation can be tested.

### Interface Testing
The Streamlit dashboard can be tested for image upload, input validation, prediction display, and recommendation output.

### Performance Evaluation
Accuracy, precision, recall, and F1-score can be used to evaluate classification performance.

## 📈 Results

The developed system integrates ultrasound image analysis and maternal nutrition-related information into a unified prediction workflow. The CNN pathway provides ultrasound-based risk information, while the nutrition pathway evaluates maternal data and produces nutrition risk information. These two outputs are combined through the meta-model fusion stage to produce a final risk category. The implemented Logistic Regression fusion model achieved an overall accuracy of **90.74%** on the evaluated fusion test set. The classification report showed an F1-score of 0.91 for LOW risk, 0.67 for MID risk, and 1.00 for HIGH risk. The application further uses the identified maternal condition and final risk level to generate personalized food recommendations, providing an additional practical component to the overall system.

## ⭐ Key Features

- Multimodal fetal health risk prediction
- Ultrasound image-based analysis
- CNN-based image classification
- Maternal data-based nutrition risk prediction
- Random Forest machine learning
- Meta-model-level fusion
- Final Low / Mid / High risk classification
- BMI, blood sugar, and blood pressure condition analysis
- Personalized food recommendations
- Interactive Streamlit dashboard
- GitHub-based deployment workflow

## 🔮 Future Enhancements

Future development can extend the system by training the models on larger and more diverse clinical datasets, improving ultrasound image preprocessing and segmentation, incorporating additional maternal and fetal parameters, and experimenting with advanced CNN architectures and ensemble learning techniques. The fusion stage can be enhanced using more sophisticated multimodal learning approaches and probability-level fusion rather than relying only on categorical risk outputs. The nutrition module can be expanded with additional dietary, demographic, and clinical parameters, while the recommendation engine can generate more detailed meal plans based on individual nutritional requirements. Explainable AI techniques could also be incorporated to provide visual and textual explanations for model predictions. Further improvements may include secure database integration, user authentication, cloud-based model serving, mobile accessibility, multilingual support, and continuous monitoring of model performance after deployment.

## ⚠️ Disclaimer

This project is intended for **academic, research, and demonstration purposes only**. The predictions and food recommendations generated by the system should not be considered a medical diagnosis or a substitute for professional medical advice. Clinical decisions should always be made by qualified healthcare professionals using appropriate medical evaluation and validated clinical information.

## 👨‍💻 Project

**Project:** Multimodal Fetal Health Risk Prediction Using Ultrasound Image Analysis and Maternal Blood Parameters with Meta Model-Level Fusion

**Repository:** `Krishnasaikmv/fetal-health-risk-prediction`

---

### Acknowledgement

This project was developed as an academic final-year project demonstrating the application of deep learning, machine learning, multimodal fusion, and interactive web technologies for fetal health risk prediction.
