# 🥩 Beef Grading - Internship Research Project

**Supervisors**:  
[1] Assoc. Prof. Dr. Sunti Tuntrakool  
[2] Dr. Kunya Tuntivisoottikul  
[3] Mr. Wacharin Kongpiboon  

**Contributor**: Nikhil Gupta (Intern)

**Project Duration**: September 2019 - October 2019 (Internship)

**Location**: King Mongkut's Institute of Technology Ladkrabang, Bangkok. Thailand (On-Site)

---

## 📌 Project Overview

This project explores the **automated grading of beef** using image processing techniques. The goal is to categorize beef samples into grades based on **intermuscular fat content** (marbling) and **aging** characteristics, which are primary indicators of meat quality and tenderness.

The grading model is built using Python and employs computer vision methods to analyze beef images and determine the appropriate grade.

---

## 🧠 Beef Grading Criteria

### 1. **Intermuscular Fat**
- Flecks of fat that run through the inside of the muscle.
- More marbling generally indicates higher quality and tenderness.

### 2. **Aging**
- Determined by cartilage development and bone ossification.
- Beef less than 30 months of age (preferably closer to 24 months) is ideal.

---

## 🏷️ Beef Grades

| Grade            | Description                                                                 |
|------------------|-----------------------------------------------------------------------------|
| **Utility**       | Low intramuscular fat, darker red meat, slightly chewy. Usually > 30 months of age. |
| **Select**        | ~40% more intramuscular fat than Utility. Must be ≤ 30 months of age.       |
| **Choice**        | Comes from Black Angus breed. Good marbling and consistent quality.         |
| **Prime**         | Produced from young, well-fed cattle. High marbling.                        |
| **Wagyu (Kobe)**  | 40–60% more marbling than Prime. Highly prized for tenderness and flavor.   |

---

## 🧪 Tools and Technologies Used

- Python
- Matlab
- OpenCV
- NumPy
- PIL (Python Imaging Library)
- Matplotlib

---

## 🧾 Code Workflow

1. **Image Loading & Display**  
   Load beef image using `PIL` and display using `matplotlib`.

2. **Image Cropping**  
   Focus on a specific region of interest in the beef sample.

3. **Grayscale Conversion & Thresholding**  
   Convert the image to black & white to distinguish fat from muscle.

4. **White Pixel Calculation**  
   Count white pixels representing marbling (fat).

5. **Fat Percentage Computation**  
   Estimate marbling percentage with a 2% correction factor.

6. **Grade Classification**  
   Based on fat percentage thresholds, classify the beef into one of the defined grades.

---
