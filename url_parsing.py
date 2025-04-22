# input the URL and find Protocol, domain & dataset.

url = 'https://www.kaggel.com/dataset'

protocol = url[ :url.find(':')]
dot1 = url.find('.')
dot2 = url.find('.', dot1+1)
domain = url[dot1 + 1 : dot2]
page = url[url.find('/', dot2): ]

print(f'Protocol: {protocol} \nDomain: {domain} \nPage: {page}')