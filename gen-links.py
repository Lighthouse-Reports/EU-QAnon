
from glob import glob

list_of_files = glob('./charts/*.html')

a = ''.join(f'<li><a href="https://lighthouse-reports.github.io/EU-QAnon/charts/{fname}" target="_blank">{fname[9:-5]}</a></li>'
            for fname in list_of_files)

htmlstr = f'''
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>List of Charts</title>
</head>
<body>
  <div><ol>
  {a}
  </ol></div>
</body>
</html>
'''

with open('index.html', 'w') as f:
    f.write(htmlstr)
