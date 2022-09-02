
import os

if __name__ == '__main__':
    a = []
    list_of_files = os.listdir(r'./')
    for i in list_of_files:
        if os.path.isdir(i) and (i not in ['.git', 'charts']):
            print(i)
            a.append(
                f'<li><a href="https://lighthouse-reports.github.io/EU-QAnon/{i}" target="_blank">{i}</a></li>')

    a = ''.join(a)
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

    with open('./network_list.html', 'w') as f:
        f.write(htmlstr)
