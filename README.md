# VisVeretas Football Data Visualization Tool

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[GitHub repository](https://github.com/timyuk/football_django)

Here is a Python Django implementation of the VisVeretas visualization tool accompanied by the Jupyter Notebook containing the preprocessing functions used for data aggregation, etc. It is not possible to rerun the preprocessing as the intermediate datasets used are not present to decrease the repository size. It is possible to run the Python Django code, and it is also hosted at [this link](http://viz-timyuk.pythonanywhere.com/), the website is not responsive on small screens as it was not implemented.

All the necessary data for the visualization tool is stored and queried from an SQLite database. The HTML, CSS, and JS code is located in index.html in the templates folder. Most of the visualization tool content is generated with pure JavaScript only. A JS library "Chart.js" with an additional module "chartjs-chart-sankey" was used for more advanced idioms such as a Radar Chart, Scatterplot, and Sankey Diagram.





<!-- GETTING STARTED -->
## Getting Started

Follow these steps in order to host the visualization tool locally

### Installation

1. Clone the repository
   ```sh
   git clone git@github.com:timyuk/football_django.git
   ```
2. Install requirements
   ```sh
   pip install -r /path/to/requirements.txt
   ```
3. Possibly migrate 
   ```sh
   python /path/to/manage.py migrate
   ```
4. Run the local server
   ```sh
   python /path/to/manage.py runserver
   ```


