import requests


def download_from_url(url):
    try:
        response = requests.get(url)
    except:
        print('Faild download!')
    else:
        if response.status_code == '200':
            with open('file_name.jpp', 'wb') as f:
                f.write(response.content)
                print('Successfully download')
        else:
            print('Faild download!')


if __name__ == '__main__':
    download_from_url('https://avatars0.githubusercontent.com/u/29729380?s=400&v=4')
