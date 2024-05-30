#!/usr/bin/python3
'''basic Python script to fetch posts from JSONPlaceholder'''

import requests
import csv


def fetch_and_print_posts():
    '''fetch  all post from the url'''
    url = f"https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print("Status Code:", response.status_code)

    # Check if the response is successful
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["title"])


def fetch_and_save_posts():
    '''fetch all post from the url'''
    url = f"https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()
        with open("posts.csv", "w",  encoding="utf-8", newline="") as csvFile:
            fieldnames = ['id', 'title', 'body']
            csvWriter = csv.DictWriter(csvFile, fieldnames=fieldnames)
            csvWriter.writeheader()
            for post in posts:
                csvWriter.writerow(
                    {'id': post['id'], 'title': post['title'], 'body': post['body']})
