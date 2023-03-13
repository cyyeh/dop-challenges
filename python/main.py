import typing

from schema import LibraryData

import pydantic


# challenge #1: retrieve a piece of information
def get_book_property(
    library_data: LibraryData, isbn: str, field_name: str
) -> typing.Any:
    """
    Returns the value of the field for the book with the given ISBN
    """
    books = library_data.catalog.books_by_isbn
    return books[isbn].dict()[field_name]


# challenge #2: search information
def books_info(library_data: LibraryData, query: str) -> str:
    """
    Returns a JSON string that contains book information about the books
    whose title contains the given string, in a case-insensitive way.
    Book information is made of: title, isbn, author full names
    """
    import json

    return json.dumps(
        [
            {
                "isbn": book_info.isbn,
                "title": book_info.title,
                "publication_year": book_info.publication_year,
                "authors": [
                    library_data.catalog.authors_by_id[author_id].name
                    for author_id in book_info.author_ids
                ],
            }
            for book_info in library_data.catalog.books_by_isbn.values()
            if query.lower() in book_info.title.lower()
        ]
    )


# challenge #3: add a piece of information
def block_member(library_data: LibraryData, email: str) -> LibraryData:
    new_library_data = LibraryData(**library_data.dict())
    new_library_data.user_management.members[email].is_blocked = True

    return new_library_data


# challenge #4: rename keys in a data entity
def rename_keys(
    data_entity: dict[str, typing.Any], key_mappings: dict[str, str]
) -> dict[str, typing.Any]:
    from copy import deepcopy

    new_data_entity = deepcopy(data_entity)
    for key, value in key_mappings.items():
        if key in new_data_entity:
            new_data_entity[value] = new_data_entity[key]
            del new_data_entity[key]

    return new_data_entity


# challenge #5: merge pieces of information
def merge_and_serialize():
    pass


# challenge #6: compare versions of data
def diff():
    pass


library_data = pydantic.parse_file_as(path="../library_data.json", type_=LibraryData)

# challenge #1
print(get_book_property(library_data, "978-1779501127", "title"))

# challenge #2
print(books_info(library_data, "watch"))

# challenge #3
print(block_member(library_data, "samantha@gmail.com"))
print(library_data)

# challenge #4
original_data_entity = {"a": 1, "b": 2}
print(rename_keys(original_data_entity, {"a": "c", "b": "d"}))
print(original_data_entity)

# challenge #5

# challenge #6
