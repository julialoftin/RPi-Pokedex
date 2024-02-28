""" Contains all external API calls """

import requests
from api_urls import GENERATION_API_URL

def fetch_generation_data():
    """Calls API for generation data"""
    try:
        response = requests.get(GENERATION_API_URL)
        if response.status_code == 200:
            generation_data = response.json().get("results", [])
            return generation_data, generation_data.length
        print(f"Failed to get Generations data. Status code: {response.status_code}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"An error occured: {e}")
        return None


def fetch_generation_i_data():
    """Calls API for generation 1 data"""
    try:
        response = requests.get(GENERATION_API_URL + "/1/")
        if response.status_code == 200:
            data = response.json()
            return data
        print(f"Failed to get Generations data. Status code: {response.status_code}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"An error occured: {e}")
        return None


def fetch_generation_ii_data():
    """Calls API for generation 2 data"""
    try:
        response = requests.get(GENERATION_API_URL + "/2/")
        if response.status_code == 200:
            data = response.json()
            return data
        print(f"Failed to get Generations data. Status code: {response.status_code}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"An error occured: {e}")
        return None


def fetch_generation_iii_data():
    """Calls API for generation 3 data"""
    try:
        response = requests.get(GENERATION_API_URL + "/3/")
        if response.status_code == 200:
            data = response.json()
            return data
        print(f"Failed to get Generations data. Status code: {response.status_code}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"An error occured: {e}")
        return None


def fetch_generation_iv_data():
    """Calls API for generation 4 data"""
    try:
        response = requests.get(GENERATION_API_URL + "/4/")
        if response.status_code == 200:
            data = response.json()
            return data
        print(f"Failed to get Generations data. Status code: {response.status_code}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"An error occured: {e}")
        return None


def fetch_generation_v_data():
    """Calls API for generation 5 data"""
    try:
        response = requests.get(GENERATION_API_URL + "/5/")
        if response.status_code == 200:
            data = response.json()
            return data
        print(f"Failed to get Generations data. Status code: {response.status_code}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"An error occured: {e}")
        return None


def fetch_generation_vi_data():
    """Calls API for generation 6 data"""
    try:
        response = requests.get(GENERATION_API_URL + "/6/")
        if response.status_code == 200:
            data = response.json()
            return data
        print(f"Failed to get Generations data. Status code: {response.status_code}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"An error occured: {e}")
        return None


def fetch_generation_vii_data():
    """Calls API for generation 7 data"""
    try:
        response = requests.get(GENERATION_API_URL + "/7/")
        if response.status_code == 200:
            data = response.json()
            return data
        print(f"Failed to get Generations data. Status code: {response.status_code}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"An error occured: {e}")
        return None


def fetch_generation_viii_data():
    """Calls API for generation 8 data"""
    try:
        response = requests.get(GENERATION_API_URL + "/8/")
        if response.status_code == 200:
            data = response.json()
            return data
        print(f"Failed to get Generations data. Status code: {response.status_code}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"An error occured: {e}")
        return None


def fetch_generation_ix_data():
    """Calls API for generation 9 data"""
    try:
        response = requests.get(GENERATION_API_URL + "/9/")
        if response.status_code == 200:
            data = response.json()
            return data
        print(f"Failed to get Generations data. Status code: {response.status_code}")
        return None
    except requests.exceptions.RequestException as e:
        print(f"An error occured: {e}")
        return None
