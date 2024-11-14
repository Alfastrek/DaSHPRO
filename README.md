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

![Screenshot (180)](https://github.com/Alfastrek/DashboardPro/assets/93537649/11b9067c-0f6b-4b66-ac6c-03537c7e1834)
![Screenshot (181)](https://github.com/Alfastrek/DashboardPro/assets/93537649/63b5aae0-983b-4588-978e-bbf6b642c9e5)
![Screenshot (182)](https://github.com/Alfastrek/DashboardPro/assets/93537649/d6d037da-198d-40cc-9ce1-e771a4fbb1c8)
![Screenshot (183)](https://github.com/Alfastrek/DashboardPro/assets/93537649/a931eead-9c24-4363-859c-e0808555febe)
![Screenshot (184)](https://github.com/Alfastrek/DashboardPro/assets/93537649/d97b9047-12f3-47b1-9a6d-c12c0948c423)
![Screenshot (185)](https://github.com/Alfastrek/DashboardPro/assets/93537649/1bd2aae6-26f8-4d27-b2cf-458c4219095d)

