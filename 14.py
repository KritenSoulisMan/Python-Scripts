import subprocess

# Список популярных библиотек для анализа данных и машинного обучения
libraries = [
    
    'numpy',
    'pandas',
    'matplotlib',
    'scikit-learn',
    'tensorflow',
    'keras',
    'pytorch',
    'nltk',
    'seaborn',
    'plotly',
    'beautifulsoup4',
    'requests',
    'flask',
    'django',
    'sqlalchemy',
    'opencv-python',
    'pillow',
    'scapy',
    'googlesearch-python',
    'selenium'

]

# Установка каждой библиотеки
for library in libraries:
    subprocess.call(['pip', 'install', library])
