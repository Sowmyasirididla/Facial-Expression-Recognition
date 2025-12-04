# Facial Expression Recognition Using Facial Muscles  
### A Novel Muscle-Driven Computer Vision System (No Training Dataset Required)

This project introduces a **new anatomy-based method** for Facial Expression Recognition (FER).  
Instead of deep-learning classifiers or large emotion datasets, this system focuses on **actual human facial muscles** and their geometric activation.

Using:

- **MediaPipe FaceMesh (468 landmarks)**
- A custom **muscle annotation tool**
- **Vector geometry**
- **Muscle activation physics**

The system produces explainable, muscle-driven emotion detection.

---

#  Features

## Stage 1: Landmark Detection  
- Extract 468 facial landmarks from any image using MediaPipe.
- Draws and saves landmark points for downstream processing.

##  Stage 2: Interactive Muscle Annotation Tool  
A GUI tool where you click on the face to define the muscle regions:

### Currently supported muscles:

### **Upper Face Muscles**
- **Frontalis - Origin (forehead)**  
- **Frontalis - Insertion (eyebrow elevation)**  
- **Orbicularis Oculi (eye ring muscle)**  

### **Mid Face Muscles**
- **Nasalis / Levator Labii Superioris (nose compression / upper lip lift)**  
  → Strong indicator of anger, disgust, or snarl  

### **Lower Face Muscles**
- **Zygomaticus Major - Origin (cheekbone)**  
- **Zygomaticus Major - Insertion (mouth corner for smile)**  
- **Depressor Anguli Oris (mouth corner downward movement for sadness)**  

Each click you make maps the nearest MediaPipe landmark automatically.  
Undo, redo, reset, and per-muscle clearing supported.

Auto-saves to: muscles.py

---

#  Stage 3: Muscle Visualization  
The system draws anatomical muscle bands on the input image:

- Origins → Insertions  
- Circular muscles (e.g., Orbicularis Oculi)  
- Direction vectors for contraction  
- Zone highlighting  

Useful for:

- Emotion explanation  
- Visual debugging  
- Muscle-based animation  
- Understanding Action Units (AUs)

---

#  Stage 4: Muscle Activation Computation  
Each muscle’s "activation" is computed using geometric changes:

- Vector displacement  
- Shortening (contraction)  
- Stretching (relaxation)  
- Angular change  
- Symmetry measurement  

This produces a **muscle activation fingerprint (MAF)** for each face.

---

#  Stage 5: Expression Recognition (Anatomy-Based)

No ML datasets needed - emotions are inferred through muscle signatures:

| Emotion       |           Key Muscles Activated                 |
|---------------|-------------------------------------------------|
| **Happiness** | Zygomaticus Major ↑ + Orbicularis Oculi ↑       |
| **Sadness**   | Depressor Anguli Oris ↑ (mouth pulled downward) |
| **Surprise**  | Frontalis ↑ + Jaw opening                       |
| **Anger**     | Nasalis/LLS ↑ + Eyebrow contraction             |
| **Disgust**   | Nasalis ↑ + Lip lift asymmetry                  |

This makes the system **interpretable**, **scientific**, and **biologically grounded**.

---

#  Directory Structure

FER_MOS/
│
├── images/ # Input images
├── muscles.py # Auto-generated muscle definitions
├── muscle_picker.py # GUI muscle annotation tool
├── draw_muscles.py # Muscle visualization
├── get_landmarks.py # FaceMesh landmark extractor
├── run_muscle_overlay.py # Pipeline runner
├── venv311/ # Virtual env 
└── README.md


---

#  Installation

### 1. Clone the repo
```bash
git clone https://github.com/Sowmyasirididla/Facial-Expression-Recognition
cd Facial-Expression-Recognition 
```
### 2. Create Python 3.11 environment
```bash
py -3.11 -m venv venv311
.\venv311\Scripts\activate
```
### 3.Install dependencies
```bash
pip install mediapipe opencv-python numpy
```
Here is a **clean, professional, GitHub-ready version** of the section you asked for — **no emojis**, fully formatted, copy-paste ready.

---

````md
## How To Use

### Step 1 — Annotate Muscles
Run the muscle annotation tool:

```bash
python muscle_picker.py
````

### Key Controls

| Key | Muscle Being Labeled                              |
| --- | ------------------------------------------------- |
| `1` | frontalis_origin                                  |
| `2` | frontalis_insertion                               |
| `3` | orbicularis_oculi                                 |
| `4` | zygomaticus_origin                                |
| `5` | zygomaticus_insertion                             |
| `6` | depressor_anguli_oris                             |
| `7` | nasalis_lift (nasalis / levator labii superioris) |
| `U` | Undo last click                                   |
| `C` | Clear current muscle                              |
| `R` | Reset all muscles                                 |
| `Q` | Quit                                              |

All selected points are automatically saved to:

```
muscles.py
```

---

### Step 2 — Visualize Muscles

```bash
python run_muscle_overlay.py
```

This script overlays all annotated muscles on the face image using the extracted landmarks.

---

### Step 3 — Compute Activation

(Coming soon)

---

### Step 4 — Emotion Recognition

(Coming soon)

---

## Why This Project Is Unique

* Dataset-free emotion recognition
* Muscle-driven, not classifier-based
* Grounded in real facial anatomy and biomechanics
* Explainable and transparent activation mapping
* Suitable for psychology, animation, affective computing, and XR applications

---

## Contributing

Contributions are welcome. You may help by:

* Adding new muscles or refining muscle definitions
* Improving geometric activation calculations
* Implementing additional visualization tools
* Adding live webcam or real-time tracking support

```





