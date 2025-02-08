

## Overview
This API allows you to manage a list of characters. It includes the ability to add new characters via a POST request and retrieve the full list of characters with a GET request. Each character has their name, occupation, and address stored in a list.

## Functions

### `POST /person`
- **Purpose**: Adds a new person (character) to the list of characters.
- **Request Body**:
    - `name` (string): The character's name.
    - `occupation` (string): The character's occupation.
    - `address` (string): The character's address.
- **Expected Behavior**: 
    - If all fields (`name`, `occupation`, and `address`) are provided and valid, the character is added to the list, and a success response is returned.
    - If any of the fields are missing or invalid, an error message indicating the invalid request is returned.

### `GET /person`
- **Purpose**: Retrieves the list of all characters stored in the system.
- **Expected Behavior**: 
    - Returns a list of characters, each with their name, occupation, and address. 
    - This allows the user to view the current data of all characters stored.

## Purpose of the Code
This code was written as part of a lab assignment to practice building basic API functionality using FastAPI. The task involved creating both POST and GET request handlers to manage a simple list of people, with validation for data integrity.

## Favorite Pokemon
My favorite Pokemon is **Hank Scorpio**. He is a charismatic yet unethical leader, making him both lovable and a bit of a moral grey area.
