# Portfolio Website - Josmuz

This is a personal portfolio website showcasing projects, skills, and experience. Built with HTML, CSS, JavaScript, and Python (Flask), it serves as an online presence for showcasing web development and digital art projects.

## Features
- Responsive design using Bootstrap and custom CSS.
- Sections including About Me, Projects, Technologies, and Contact.
- Interactive elements and animations.
- Links to GitHub, LinkedIn, and Fiverr portfolio.
- Integrated Flask application for job listings.

## Installation
### Prerequisites
Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

### Install Required Libraries
Clone the repository and install dependencies:
```bash
git clone https://github.com/solmuz/josmuz.git
cd josmuz
pip install flask requests beautifulsoup4
```

### Running Locally
1. **Start the Flask application**:
   ```bash
   python app.py
   ```
2. **Open the portfolio website**:
   - Open `index.html` in a browser.
   - Access the Flask job listings at `http://127.0.0.1:5000/`.

## Project Structure
```
|-- index.html            # Main HTML file
|-- styles.css            # Custom styles
|-- bootstrap-grid.css    # Bootstrap grid system
|-- images/               # Project images
|-- swiper.js             # Swiper JS for image sliders
|-- app.py                # Flask application for job listings
|-- requirements.txt      # Dependencies
```

## Deployment
This website can be deployed on GitHub Pages or any static hosting service like Netlify or Vercel. The Flask app can be deployed separately using Render or PythonAnywhere.

### Deploy on GitHub Pages
1. Go to your GitHub repository settings.
2. Scroll to **GitHub Pages** and set the source to `main` branch.
3. Your site will be live at `https://solmuz.github.io/josmuz/`.

### Deploy Flask on Render
1. Push your project to GitHub.
2. Create an account on [Render](https://render.com/).
3. Create a new web service and link your repository.
4. Set up the environment:
   - Build Command: `pip install -r requirements.txt`
   - Start Command: `gunicorn app:app`
5. Deploy and access the job listings online.

## License
This project is open-source under the MIT License.

---
Feel free to contribute by submitting issues or pull requests!


### Deploy on GitHub Pages
1. Go to your GitHub repository settings.
2. Scroll to **GitHub Pages** and set the source to `main` branch.
3. Your site will be live at `https://solmuz.github.io/josmuz/`.

## License
This project is open-source under the MIT License.

---
Feel free to contribute by submitting issues or pull requests!

