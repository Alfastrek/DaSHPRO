# 📊 DashPro - Dynamic Data Dashboard with Django & Chart.js

(Website Snapshots attached below)
## Introduction

In this Project, we have created a Visualization Dashboard to facilitate analytics, graphs, and charts for better visualization of the given dataset. This Assessment includes three pages:

- **🏠 Home**: Collection of all Charts, Graphs, and complete Analysis.
- **🔍 Filtering Zone**: Page to read and filter data from the raw dataset.
- **🔗 Portfolio**: Link to GitHub Profile.

## Technology and Libraries Used

- **🖥️ Django Framework**
- **🐍 Python** for API
- **🍃 MongoDB**
- **🎨 Bootstrap**
- **🌐 HTML**
- **🎨 CSS**
- **⚙️ JavaScript**
- **📊 Chart Libraries**:
  - Fusion Charts
  - Charts.js

## Data Visualization and Analysis

1. **📈 Line Chart (id: lineChart)**
   - Displays the average relevance by pestle.
   - Each data point represents the average relevance score for a specific pestle category.
   - Helps visualize trends or variations in relevance across different pestle categories.

2. **📊 Bar Chart (id: barchart)**
   - Represents the intensity of topics vs. countries.
   - Each bar represents the intensity of a specific topic in different countries.
   - Useful for comparing the intensity of topics across multiple countries.

3. **🍩 Doughnut Chart (id: doughnutchart)**
   - Displays the average relevance by pestle in a doughnut chart format.
   - Each segment represents the average relevance score for a specific pestle category.
   - Provides a visual overview of the distribution of relevance across different pestle categories.

4. **📉 Box and Whisker Plot (id: box-plot)**
   - Shows the statistical distribution of likelihood values by country (excluding the USA).
   - Provides information on the mean, maximum, and minimum likelihood values for each country.
   - Helps in identifying the spread and central tendency of likelihood values across different countries.

5. **🌀 Polar Area Chart (id: myPolarAreaChart)**
   - Visualizes the likelihood values for different topics in a polar area chart format.
   - Each segment represents the likelihood values for a specific topic.
   - Useful for comparing the distribution of likelihood values across different topics.

6. **📉 Area Chart (id: myAreaChart)**
   - Represents the intensity of topics (oil and energy) across different countries.
   - Each line represents the intensity values for a specific topic (oil or energy) in different countries.
   - Helps in understanding the variation in intensity values for different topics across multiple countries.

## Bash Scripts

To set up and run the project, you can use the following bash scripts.

### Setup Script

```bash
#!/bin/bash

# Update and install dependencies
sudo apt-get update
sudo apt-get install -y python3 python3-venv python3-pip mongodb

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install required Python packages
pip install django pymongo

# Navigate to the Django project directory
cd path/to/your/django/project

# Apply migrations and start the Django development server
python manage.py migrate
python manage.py runserver
```
![Screenshot (182)](https://github.com/user-attachments/assets/0532ec12-c30a-4d5a-8f9c-6ca89ac33bb2)
![Screenshot (181)](https://github.com/user-attachments/assets/ddc3d4d6-340c-4ca9-b5c2-53c7efba0c63)

![Screenshot (180)](https://github.com/user-attachments/assets/c164032b-9755-409b-ba1c-694724d57d06)

![Screenshot (185)](https://github.com/user-attachments/assets/8c1dca1f-345b-4984-8a20-d44c2b4abd3b)

![Screenshot (183)](https://github.com/user-attachments/assets/a1014471-d5e0-4e08-a49d-504424a51711)



