from django.shortcuts import render
import requests
import time
import random


def formater(pages):
    '''
    I need:
        name, productUrl, image, originalPrice, price
    '''
    data = list()
    for items in pages:
        for item in items:
            dict = {}
            dict['Product'] =  item['name']
            dict['Price_now'] = float(item['price'])
            x = 0
            if 'originalPrice' not in item.keys():
                dict['Old_price'] = item['price']
                x = float(item['price'])
            else:
                dict['Old_price'] = item['originalPrice']
                x = float(item['originalPrice'])
            dict['Save'] = float(x - float(item['price']))
            dict['Product_link'] =  'https:'+item['productUrl']
            dict['image'] = item['image']
            data.append(dict)
    return data


def get_headphones(brand=""):
    pages = list()
    if brand == "":
        brand = ['uiisii', 'remax', 'qkz', 'awei']
        brand_index = 0
        for page in range(1, 5):
            time_span = random.randint(4, 8)
            time.sleep(time_span)
            url = 'https://www.daraz.com.bd/headphones-headsets/'+brand[brand_index]+'?ajax=true&page='+str(page)
            data = requests.get(url).json()
            pages.append(data['mods']['listItems'])
            brand_index += 1
    else:
        for page in range(1, 2):
            time_span = random.randint(4, 10)
            time.sleep(time_span)
            url = 'https://www.daraz.com.bd/headphones-headsets/'+brand+'/?ajax=true&page='+str(page)
            data = requests.get(url).json()
            pages.append(data['mods']['listItems'])

    data = list()
    data = formater(pages)
    return data

def get_smart_watch(brand=""):
    pages = list()
    if brand == "":
        brand = ['tigers-123438037', 'abondon-123454678', 'sixfix-123454869', 'active4u-121042221']
        brand_index = 0
        for page in range(1, 4):
            time_span = random.randint(4, 8)
            time.sleep(time_span)
            url = 'https://www.daraz.com.bd/smart-watches/'+brand[brand_index]+'/?ajax=true&page='+str(page)
            data = requests.get(url).json()
            pages.append(data['mods']['listItems'])
            brand_index += 1
    else:
        for page in range(1, 2):
            time_span = random.randint(4, 10)
            time.sleep(time_span)
            url = 'https://www.daraz.com.bd/smart-watches/'+brand+'/?ajax=true&page='+str(page)
            data = requests.get(url).json()
            pages.append(data['mods']['listItems'])

    data = list()
    data = formater(pages)
    return data

def get_keyboard(brand=""):
    pages = list()
    if brand == "":
        brand = ['havit', 'jinmy-123395891', 'dealmaster-123450453', 'loftwell-123232663']
        brand_index = 0
        for page in range(1, 4):
            time_span = random.randint(4, 8)
            time.sleep(time_span)
            url = 'https://www.daraz.com.bd/keyboard/'+brand[brand_index]+'/?ajax=true&page='+str(page)
            data = requests.get(url).json()
            pages.append(data['mods']['listItems'])
            brand_index += 1
    else:
        for page in range(1, 2):
            time_span = random.randint(4, 10)
            time.sleep(time_span)
            url = 'https://www.daraz.com.bd/keyboard/'+brand+'/?ajax=true&page='+str(page)
            data = requests.get(url).json()
            pages.append(data['mods']['listItems'])

    data = list()
    data = formater(pages)
    return data

def get_mouse(brand=""):
    pages = list()
    if brand == "":
        brand = ['havit', 'trianglemall-123427289', 'udestiny-201122', 'quanbu-121063691']
        brand_index = 0
        for page in range(1, 4):
            time_span = random.randint(4, 8)
            time.sleep(time_span)
            url = 'https://www.daraz.com.bd/computer-accessories-mouse/'+brand[brand_index]+'/?ajax=true&page='+str(page)
            data = requests.get(url).json()
            pages.append(data['mods']['listItems'])
            brand_index += 1
    else:
        for page in range(1, 2):
            time_span = random.randint(4, 10)
            time.sleep(time_span)
            url = 'https://www.daraz.com.bd/computer-accessories-mouse/'+brand+'/?ajax=true&page='+str(page)
            data = requests.get(url).json()
            pages.append(data['mods']['listItems'])

    data = list()
    data = formater(pages)
    return data


def get_spectacles(brand=""):
    pages = list()
    if brand == "":
        brand = ['etop', 'seelight-123286279', 'new-uttara-optics', 'eye-star-optics-123332615']
        brand_index = 0
        for page in range(1, 4):
            time_span = random.randint(4, 8)
            time.sleep(time_span)
            url = 'https://www.daraz.com.bd/mens-eyeglasses/'+brand[brand_index]+'/?ajax=true&page='+str(page)
            data = requests.get(url).json()
            pages.append(data['mods']['listItems'])
            brand_index += 1
    else:
        for page in range(1, 2):
            time_span = random.randint(4, 10)
            time.sleep(time_span)
            url = 'https://www.daraz.com.bd/mens-eyeglasses/'+brand+'/?ajax=true&page='+str(page)
            data = requests.get(url).json()
            pages.append(data['mods']['listItems'])

    data = list()
    data = formater(pages)
    return data



def index(request):
    return render(request, 'spider/index.html')

def home(request):
    data = get_headphones()
    data2 = get_smart_watch()
    data3 = get_mouse()
    data4 = get_keyboard()
    data5 = get_spectacles()
    data = sorted(data, key=lambda k: k['Save'], reverse=True)[0:30]
    data2 = sorted(data2, key=lambda k: k['Save'], reverse=True)[0:30]
    data3 = sorted(data3, key=lambda k: k['Save'], reverse=True)[0:30]
    data4 = sorted(data4, key=lambda k: k['Save'], reverse=True)[0:30]
    data5 = sorted(data5, key=lambda k: k['Save'], reverse=True)[0:30]

    context = {
        'title':'home',
        'data': data,
        'data2': data2,
        'data3': data3,
        'data4': data4,
        'data5': data5
    }
    return render(request, 'spider/home.html', context)

def headphones(request, brand):
    data = get_headphones(brand)
    data = sorted(data, key=lambda k: k['Save'], reverse=True)[:16]

    context = {
        'data': data,
        'title': brand
    }
    return render(request, 'spider/headphones.html', context)


def smart_watches(request, brand):
    data = get_smart_watch()
    data = sorted(data, key=lambda k: k['Save'], reverse=True)[:16]

    context = {
        'data': data,
        'title': brand
    }
    return render(request, 'spider/smart-watches.html', context)

def mice(request, brand):
    data = get_mouse()
    data = sorted(data, key=lambda k: k['Save'], reverse=True)[:16]

    context = {
        'data': data,
        'title': brand
    }
    return render(request, 'spider/smart-watches.html', context)

def keyboards(request, brand):
    data = get_keyboard(brand)
    data = sorted(data, key=lambda k: k['Save'], reverse=True)[:16]

    context = {
        'data': data,
        'title': brand
    }
    return render(request, 'spider/keyboards.html', context)

def spectacles(request, brand):
    data = get_keyboard(brand)
    data = sorted(data, key=lambda k: k['Save'], reverse=True)[:16]

    context = {
        'data': data,
        'title': brand
    }
    return render(request, 'spider/spectacles.html', context)
