from django.shortcuts import render
import requests
import time
import random

def get_time_span():
    span = random.uniform(0, 0.1)
    print("        Time span (To avoid anti-scraper): ", span)
    return span

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36"}

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
    print(">> Fetching headphones...")
    if brand == "":
        brand = ['uiisii', 'remax', 'qkz', 'awei']
        brand_index = 0
        for page in range(1, 5):
            time_span = get_time_span()
            time.sleep(time_span)
            url = 'https://www.daraz.com.bd/headphones-headsets/'+brand[brand_index]+'/?ajax=true&page='+str(page)
            data = requests.get(url, headers=headers).json()
            pages.append(data['mods']['listItems'])
            brand_index += 1
    else:
        for page in range(1, 3):
            time_span = get_time_span()
            time.sleep(time_span)
            url = 'https://www.daraz.com.bd/headphones-headsets/'+brand+'/?ajax=true&page='+str(page)
            data = requests.get(url,  headers=headers).json()
            pages.append(data['mods']['listItems'])

    data = list()
    data = formater(pages)
    print(">> Headphones fetched!")
    return data

def get_smart_watch(brand=""):
    pages = list()
    print(">> Fetching smart watches...")
    if brand == "":
        brand = ['xiaomi', 'havit', 'huawei', 'lenovo']
        brand_index = 0
        for page in range(1, 5):
            time_span = get_time_span()
            time.sleep(time_span)
            url = 'https://www.daraz.com.bd/smart-watches/'+brand[brand_index]+'/?ajax=true&page='+str(page)
            data = requests.get(url,  headers=headers).json()
            pages.append(data['mods']['listItems'])
            brand_index += 1
    else:
        for page in range(1, 3):
            time_span = get_time_span()
            time.sleep(time_span)
            url = 'https://www.daraz.com.bd/smart-watches/'+brand+'/?ajax=true&page='+str(page)
            data = requests.get(url,  headers=headers).json()
            pages.append(data['mods']['listItems'])

    data = list()
    data = formater(pages)
    print(">> Smart watches fetched!")
    return data

def get_keyboard(brand=""):
    pages = list()
    print(">> Fetching keyboards...")
    if brand == "":
        brand = ['havit', 'logitech', 'a4tech', 'RAZER']
        brand_index = 0
        for page in range(1, 5):
            time_span = get_time_span()
            time.sleep(time_span)
            url = 'https://www.daraz.com.bd/keyboard/'+brand[brand_index]+'/?ajax=true&page='+str(page)
            data = requests.get(url,  headers=headers).json()
            pages.append(data['mods']['listItems'])
            brand_index += 1
    else:
        for page in range(1, 3):
            # time_span = random.randint(time_range['upper'], time_range['lower'])
            time_span = get_time_span()
            time.sleep(time_span)
            url = 'https://www.daraz.com.bd/keyboard/'+brand+'/?ajax=true&page='+str(page)
            data = requests.get(url,  headers=headers).json()
            pages.append(data['mods']['listItems'])

    data = list()
    data = formater(pages)
    print(">> Keyboards fetched!")
    return data

def get_mouse(brand=""):
    pages = list()
    print(">> Fetching mice...")
    if brand == "":
        brand = ['havit', 'logitech', 'a4tech', 'RAZER']
        brand_index = 0
        for page in range(1, 5):
            time_span = get_time_span()
            time.sleep(time_span)
            url = 'https://www.daraz.com.bd/computer-accessories-mouse/'+brand[brand_index]+'/?ajax=true&page='+str(page)
            data = requests.get(url,  headers=headers).json()
            pages.append(data['mods']['listItems'])
            brand_index += 1
    else:
        for page in range(1, 3):
            time_span = get_time_span()
            time.sleep(time_span)
            url = 'https://www.daraz.com.bd/computer-accessories-mouse/'+brand+'/?ajax=true&page='+str(page)
            data = requests.get(url,  headers=headers).json()
            pages.append(data['mods']['listItems'])

    data = list()
    data = formater(pages)
    print(">> Mice fetched!")
    return data


def get_spectacles(brand=""):
    print(">> Fetching spectacles...")
    pages = list()
    if brand == "":
        brand_index = 0
        for page in range(1, 5):
            time_span = get_time_span()
            time.sleep(time_span)
            url = 'https://www.daraz.com.bd/mens-eyeglasses/?ajax=true&page='+str(page)
            data = requests.get(url,  headers=headers).json()
            pages.append(data['mods']['listItems'])
            brand_index += 1
    else:
        for page in range(1, 3):
            time_span = get_time_span()
            time.sleep(time_span)
            url = 'https://www.daraz.com.bd/mens-eyeglasses/'+brand+'/?ajax=true&page='+str(page)
            data = requests.get(url, headers=headers).json()
            pages.append(data['mods']['listItems'])

    data = list()
    data = formater(pages)
    print(">> Spectacles fetched!")
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
